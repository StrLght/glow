import pygame,os,sys,copy
from pygame.locals import *

class Engine:
	def __init__(self,width,height,g,caption="NOPE"):
		pygame.init()
		pygame.display.set_mode((width, height))
		pygame.display.set_caption(caption)
		pygame.key.set_repeat()
		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.entities = []
		self.background = None
		self.g = g
		self.totaldelta = 0
		self.player = None
		self.exit = None
		self.sprites = pygame.sprite.RenderPlain()

	def set_background(self,background):
		self.background = background

	def get_display_rect(self):
		return pygame.display.get_surface().get_rect()

	def delay(self,time):
		pygame.time.delay(time)

	def toogle_fullscreen(self):
		pygame.display.toggle_fullscreen()

	def load_sound(self,name):
		class NoneSound:
			def play(self): pass
		if not pygame.mixer:
			return NoneSound()
		main_dir = os.path.split(os.path.abspath(__file__))[0]
		data_dir = os.path.join(main_dir, 'data')
		fullname = os.path.join(data_dir, name)
		try:
			sound = pygame.mixer.Sound(fullname)
		except pygame.error:
			sound = NoneSound
			pass
		return sound

	def play_music(self,name,repeats):
		main_dir = os.path.split(os.path.abspath(__file__))[0]
		data_dir = os.path.join(main_dir, 'data')
		fullname = os.path.join(data_dir, name)
		try:
			pygame.mixer.music.load(fullname)
			pygame.mixer.music.play(repeats)
		except pygame.error:
			pass

	def add_entity(self,entity):
		self.entities.append(entity)
		self.sprites.add(entity)
		if entity.enttype == "player":
			self.player = self.entities[-1]
		if entity.enttype == "exit":
			self.exit = self.entities[-1]

	def remove_entity(self,entity):
		self.entities.remove(entity)
		self.sprites.remove(entity)

	def gravity(self):
		entity = copy.deepcopy(self.player)
		entity.rect.y += self.g
		collision = self.check_collision(entity)
		if  len(collision) == 0:
			if self.player.jumpheight <= 0:
				self.player.rect.y += self.g
		else:
			if self.entities[collision[0]].enttype == "lift":
				if self.entities[collision[0]].dy != 0 and self.player.jumpheight > 0:
					self.player.rect.y -= self.entities[collision[0]].dy
					self.update()
					return
				if entity.rect.bottom - 5 < self.entities[collision[0]].rect.bottom and self.player.rect.top < self.entities[collision[0]].rect.top:
					self.player.rect.x += self.entities[collision[0]].dx
					self.player.rect.bottom = self.entities[collision[0]].rect.top
					self.player.jumping = False
					self.player.jumpheight = 0
					self.update()
					return
			if self.player.rect.bottom <= self.entities[collision[0]].rect.top:
				self.player.rect.bottom = self.entities[collision[0]].rect.top
				self.player.jumping = False
				self.player.jumpheight = 0
			if self.player.rect.bottom > self.entities[collision[0]].rect.top:
				self.player.rect.y += self.g
				self.player.jumpheight = 0
		self.update()

	def clear(self):
		self.entities = []
		self.sprites.empty()
		self.background = None
		self.player = None
		self.totaldelta = 0

	def check_collision(self,entity,exit = False):
		retval = []
		for collide in entity.rect.collidelistall([x.rect for x in self.entities]):
			if entity != self.entities[collide] and self.entities[collide].enttype != "player" and self.entities[collide].enttype != "text" and self.entities[collide].enttype != "exit":
				retval.append(collide)
			if len(retval) > 0:
				break
		return retval

	def check_completed_collision(self):
		return self.player.rect.colliderect(self.exit.rect)

	def check_jumpable(self):
		ent = copy.deepcopy(self.player)
		ent.rect.y += 1
		if len(self.check_collision(ent)) == 0:
			self.player.jumping = True

	def get_pressed(self):
		return pygame.key.get_pressed()

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.quit()

	def update(self):
		self.sprites.empty()
		for entity in self.entities:
			self.sprites.add(entity)

	def update_camera(self):
		if self.player.rect.x > 250:
			self.move_camera(dx = 250-self.player.rect.x)
		if self.player.rect.x < 150:
			self.move_camera(dx = 150-self.player.rect.x)
		if self.player.rect.y < 250:
			self.move_camera(dy = 250-self.player.rect.y)
		if self.player.rect.y > 420 and self.totaldelta > 0:
				self.move_camera(dy = 420-self.player.rect.y)

	def move_camera(self,dx=0,dy=0):
		self.totaldelta += dy
		for i in range(len(self.entities)):
			self.entities[i].move(dx,dy)
		self.update()

	def render(self):
		if self.background is not None:
			self.screen.blit(self.background.image,(0,0))
		self.sprites.update()
		if self.player is not None:
			self.gravity()
			self.check_jumpable()
		self.sprites.draw(self.screen)
		pygame.display.flip()

	def quit(self):
		sys.exit(0)

