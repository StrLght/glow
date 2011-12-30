import   copy
from pygame.locals import *
from package import entity

class Level:
	def __init__(self,engine):
		self.eng = engine
		self.going = True
		self.completed = False
		self.jumpsound = engine.load_sound('jump.wav')

	def handle_input(self):
		entity = copy.deepcopy(self.eng.player)
		pressed = self.eng.get_pressed()
		if pressed[K_LEFT] == 1 or pressed[ord('a')] == 1:
			entity.rect.x -= 5
			collision = self.eng.check_collision(entity)
			if len(collision)==1:
				self.eng.player.rect.x -= 5
			else:
				if self.eng.entities[collision[1]].enttype != "lift":
					if self.eng.entities[collision[1]].rect.bottom < self.eng.entities[collision[1]].rect.top:
						self.eng.player.rect.left = self.eng.entities[collision[1]].rect.right
		if pressed[K_RIGHT] == 1 or pressed[ord('d')] == 1:
			entity.rect.x += 5
			collision = self.eng.check_collision(entity)
			if len(collision) == 1:
				self.eng.player.rect.x += 5
			else:
				if self.eng.entities[collision[1]].enttype != "lift":
					if self.eng.entities[collision[1]].rect.bottom < self.eng.entities[collision[1]].rect.top:
						self.eng.player.rect.right = self.eng.entities[collision[1]].rect.left
		if pressed[K_UP] == 1 or pressed[K_SPACE] == 1 or pressed[ord('w')] == 1:
			if not self.eng.player.jumping:
				self.jumpsound.play()
				self.eng.player.jumpheight = self.eng.player.totalheight
				self.eng.player.jumping = True
		if pressed[K_ESCAPE] == 1:
			self.eng.player.rect.top = 481

	def jump(self):
		if self.eng.player.jumpheight > 0:
			self.eng.player.rect.y -= self.eng.g + 3
			self.eng.player.jumpheight -= self.eng.g + 3
		else:
			self.eng.player.jumpheight = 0

	def needs_respawn(self):
		if not self.eng.player.rect.colliderect(self.eng.get_display_rect()):
			self.going = False

	def run(self):
		pass

class Level1(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Text("Press arrows or WASD to move",42,"m46.TTF",(60,265),(255,255,255)))
		self.eng.add_entity(entity.Text("Exit ->",34,"m46.TTF",(500,400),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',-20,440,scale=(680,80)))
		self.eng.add_entity(entity.Entity('exit.png',605,396,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			# self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level2(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Text("Press up or space to jump",42,"m46.TTF",(105,265),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',-20,440,scale=(680,80)))
		self.eng.add_entity(entity.Entity('pic2.png',500,420,scale=(50,20)))
		self.eng.add_entity(entity.Entity('pic2.png',550,400,scale=(50,40)))
		self.eng.add_entity(entity.Entity('pic2.png',590,380,scale=(50,60)))
		self.eng.add_entity(entity.Entity('exit.png',605,336,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			# self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level3(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Text("OMG IT'S MOVING!",42,"m46.TTF",(160,265),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(100,80)))
		self.eng.add_entity(entity.Lift('platform.png',270,440,110,455,440,440,-3))
		self.eng.add_entity(entity.Entity('pic2.png',551,440,scale=(100,80)))
		self.eng.add_entity(entity.Entity('exit.png',605,396,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			# self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level4(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = True
		for i in range(7):
			self.eng.clear()
			if i%2:
				self.eng.set_background(entity.Entity('black.png',0,0))
			else:
				self.eng.set_background(entity.Entity('white.png',0,0))
			self.eng.render()
			self.eng.delay(200)

class Level5(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('moon.png',0,0))
		self.eng.add_entity(entity.Text("What happend?",36,"m46.TTF",(0,265),(255,255,255)))
		self.eng.add_entity(entity.Text("Where am I?",36,"m46.TTF",(180,-36),(255,255,255)))
		self.eng.add_entity(entity.Text("Where is everyone?",36,"m46.TTF",(500,93),(255,255,255)))
		self.eng.add_entity(entity.Text("It was a day a minute ago...",36,"m46.TTF",(480,-20),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(100,80)))
		self.eng.add_entity(entity.Lift('platform.png',110,400,110,110,110,445,dy=-3))
		self.eng.add_entity(entity.Entity('pic2.png',195,115,scale=(200,60)))
		self.eng.add_entity(entity.Entity('pic2.png',325,95,scale=(35,20)))
		self.eng.add_entity(entity.Entity('pic2.png',360,75,scale=(35,40)))
		self.eng.add_entity(entity.Lift('platform.png',401,75,400,740,75,75,3))
		self.eng.add_entity(entity.Entity('pic2.png',845,75,scale=(100,30)))
		self.eng.add_entity(entity.Entity('exit.png',910,31,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level6(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('moon.png',0,0))
		self.eng.add_entity(entity.Text("Hello?",36,"m46.TTF",(50,320),(255,255,255)))
		self.eng.add_entity(entity.Text("Anybody?...",36,"m46.TTF",(480,-40),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(150,80)))
		self.eng.add_entity(entity.Lift('platform.png',480,440,155,480,0,0,-3))
		self.eng.add_entity(entity.Lift('platform.png',570,440,0,0,115,440,dy=-3))
		self.eng.add_entity(entity.Lift('platform.png',1000,120,675,1000,0,0,-3))
		self.eng.add_entity(entity.Lift('platform.png',1105,120,1105,1430,0,0,3))
		self.eng.add_entity(entity.Entity('pic2.png',1530,120,scale=(150,40)))
		self.eng.add_entity(entity.Entity('exit.png',1647,76,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level7(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Text("This world is strange",36,"m46.TTF",(50,220),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',50,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(130,30)))
		self.eng.add_entity(entity.Entity('pic2.png',100,410,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',150,380,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',230,360,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',310,340,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',410,330,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',410,330,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',550,350,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',650,330,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',760,330,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',880,340,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',1020,350,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',1130,335,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',1230,315,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',1330,300,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',1430,285,scale=(30,30)))
		self.eng.add_entity(entity.Entity('pic2.png',1430,285,scale=(130,30)))
		self.eng.add_entity(entity.Entity('exit.png',1525,241,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level8(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('far.png',0,0))
		self.eng.add_entity(entity.Text("Wait",36,"m46.TTF",(80,320),(255,255,255)))
		self.eng.add_entity(entity.Text("Far far away",36,"m46.TTF",(350,290),(255,255,255)))
		self.eng.add_entity(entity.Text("Is it...?",36,"m46.TTF",(670,265),(255,255,255)))
		self.eng.add_entity(entity.Text("I need to get there as soon as I can!",36,"m46.TTF",(900,265),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',50,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(300,80)))
		self.eng.add_entity(entity.Entity('pic2.png',300,410,scale=(300,110)))
		self.eng.add_entity(entity.Entity('pic2.png',600,380,scale=(300,140)))
		self.eng.add_entity(entity.Entity('pic2.png',900,360,scale=(520,160)))
		self.eng.add_entity(entity.Lift('platform.png',1425,360,1420,1570,0,0,-3))
		self.eng.add_entity(entity.Entity('pic2.png',1655,360,scale=(150,160)))
		self.eng.add_entity(entity.Entity('exit.png',1770,316,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level9(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Entity('hero.png',30,195,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,240,scale=(150,80)))
		self.eng.add_entity(entity.Entity('pic2.png',200,260,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',290,280,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',380,300,scale=(40,40)))
		self.eng.add_entity(entity.Lift('platform.png',430,300,430,600,0,0,3))
		self.eng.add_entity(entity.Entity('pic2.png',690,300,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',780,280,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',870,260,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',960,240,scale=(150,80)))
		self.eng.add_entity(entity.Entity('exit.png',1079,195,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Level10(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('moon.png',0,0))
		self.eng.add_entity(entity.Text("What the hell?",36,"m46.TTF",(490,-120),(255,255,255)))
		self.eng.add_entity(entity.Text("phew",36,"m46.TTF",(520,420),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',30,195,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,240,scale=(150,80)))
		self.eng.add_entity(entity.Entity('pic2.png',200,220,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',290,200,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',380,180,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',470,160,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',560,140,scale=(40,40)))
		self.eng.add_entity(entity.Entity('pic2.png',620,440,scale=(200,40)))
		self.eng.add_entity(entity.Lift('platform.png',825,440,825,1225,0,0,3))
		self.eng.add_entity(entity.Lift('platform.png',1325,35,0,0,35,435,0,dy=-3))
		self.eng.add_entity(entity.Entity('pic2.png',1425,30,scale=(150,40)))
		self.eng.add_entity(entity.Entity('exit.png',1540,-14,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class LevelPrelast(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('moon.png',0,0))
		self.eng.add_entity(entity.Text("I have found you!",36,"m46.TTF",(150,265),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',-20,440,scale=(680,80)))
		self.eng.add_entity(entity.Entity('black.png',595,360,"exit",scale=(10,80)))
		self.eng.add_entity(entity.Entity('fhero.png',605,396))
		while self.going and not self.completed:
			self.needs_respawn()
			# self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class LevelLast(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Text("Not again.",36,"m46.TTF",(200,200),(255,255,255)))
		self.eng.add_entity(entity.Text("Wait. It was night minute ago.",36,"m46.TTF",(450,200),(255,255,255)))
		self.eng.add_entity(entity.Text("Where's she?",36,"m46.TTF",(1050,200),(255,255,255)))
		self.eng.add_entity(entity.Text("Why this happens to me?",36,"m46.TTF",(1500,200),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(100,80)))
		self.eng.add_entity(entity.Lift('platform.png',270,440,110,1705,0,0,-3))
		self.eng.add_entity(entity.Entity('pic2.png',1800,440,scale=(100,80)))
		self.eng.add_entity(entity.Entity('exit.png',1854,396,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class LevelSrslyLast(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.going = True
		self.completed = False
		self.eng.set_background(entity.Entity('sun.png',0,0))
		self.eng.add_entity(entity.Text("I will never find her again",36,"m46.TTF",(10,200),(255,255,255)))
		self.eng.add_entity(entity.Text("Why can't I be happy for a while? :(",36,"m46.TTF",(275,-150),(255,255,255)))
		self.eng.add_entity(entity.Entity('hero.png',10,396,"player",40))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(150,80)))
		self.eng.add_entity(entity.Lift('platform.png',155,360,110,110,110,445,dy=-3))
		self.eng.add_entity(entity.Entity('pic2.png',240,115,scale=(50,60)))
		self.eng.add_entity(entity.Lift('platform.png',300,110,110,110,-40,110,dy=-3))
		self.eng.add_entity(entity.Entity('pic2.png',390,-35,scale=(150,60)))
		self.eng.add_entity(entity.Entity('exit.png',505,-79,"exit"))
		while self.going and not self.completed:
			self.needs_respawn()
			self.eng.update_camera()
			self.eng.handle_input()
			self.handle_input()
			self.eng.clock.tick(30)
			self.jump()
			self.eng.render()
			self.completed = self.eng.check_completed_collision()

class Outro(Level):
	def __init__(self,engine):
		Level.__init__(self,engine)

	def run(self):
		self.eng.clear()
		self.completed = True
		self.eng.set_background(entity.Entity('black.png',0,0))
		self.eng.add_entity(entity.Text("Many years later",42,"m46.TTF",(175,230),(255,255,255)))
		self.eng.render()
		self.eng.delay(2500)
		self.eng.clear()
		for i in range(7):
			if i%2:
				self.eng.set_background(entity.Entity('black.png',0,0))
			else:
				self.eng.set_background(entity.Entity('white.png',0,0))
			self.eng.render()
			self.eng.clear()
			self.eng.delay(200)
		self.eng.set_background(entity.Entity('black.png',0,0))
		self.eng.add_entity(entity.Entity('oldhero.png',10,396))
		self.eng.add_entity(entity.Entity('pic2.png',0,440,scale=(640,80)))
		self.eng.add_entity(entity.Entity('fhero.png',599,396))
		self.eng.add_entity(entity.Text("Is it you?",42,"m46.TTF",(235,130),(255,255,255)))
		self.eng.add_entity(entity.Text("After all this years",42,"m46.TTF",(165,230),(255,255,255)))
		self.eng.render()
		self.eng.delay(2000)
		for i in range(278):
			self.eng.entities[0].rect.x += 1
			self.eng.entities[2].rect.x -= 1
			self.eng.render()
		self.eng.render()
		self.eng.delay(2000)
		self.eng.clear()
		self.eng.set_background(entity.Entity('black.png',0,0))
		self.eng.add_entity(entity.Text("The End",42,"m46.TTF",(250,230),(255,255,255)))
		self.eng.render()
		self.eng.delay(5000)
		self.eng.clear()

