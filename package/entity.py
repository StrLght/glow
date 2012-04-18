import pygame
import engine

class Entity(pygame.sprite.Sprite):
	def __init__(self, path, x, y, enttype = "static", jumpheight = 0, scale = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.load_image(path, scale)
		self.rect.topleft = (x,y)
		self.enttype = enttype
		self.jumping = False
		self.jumpheight = 0
		self.totalheight = jumpheight

	def __eq__(self, y):
		return self.rect == y.rect and self.image == y.image

	def __ne__(self, y):
		return not self.__eq__(y)

	def update(self): pass

	def move(self, dx, dy):
		self.rect.x += dx
		self.rect.y += dy

	def load_image(self, name, scale):
		fullname = engine.get_file(name)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			raise SystemExit, message
		image = image.convert_alpha()
		if scale != (0,0):
			self.image = pygame.transform.scale(image, scale)
		else:
			self.image = image
		self.rect = self.image.get_rect()

class Lift(Entity):
	def __init__(self, path, x, y, minx, maxx, miny, maxy, dx = 0, dy = 0, scale = (0, 0)):
		Entity.__init__(self, path, x, y, "lift", scale = scale)
		self.minx = minx
		self.maxx = maxx
		self.miny = miny
		self.maxy = maxy
		self.up = False
		self.right = True
		self.dx = dx
		self.dy = -dy
		self.vertical = self.maxy - self.miny > 0
		self.horizontal = self.maxx - self.minx > 0

	def move(self, dx, dy):
		Entity.move(self, dx, dy)
		self.maxx += dx
		self.minx += dx
		self.maxy += dy
		self.miny += dy

	def update(self):
		if self.vertical:
			if self.up:
				self.rect.y -= self.dy
			else:
				self.rect.y += self.dy
			if self.rect.y <= self.miny:
				self.up = False
			elif self.rect.y >= self.maxy:
				self.up = True
		if self.horizontal:
			self.rect.x += self.dx
			if self.rect.x >= self.maxx:
				self.dx = -self.dx
			elif self.rect.x <= self.minx:
				self.dx = -self.dx

class Text(Entity):
	def __init__(self, text, size, fontname, (x, y), (r, g, b)):
		pygame.sprite.Sprite.__init__(self)
		self.enttype = "text"
		self.jumpheight = 0
		self.jumping = False
		self.load_font(text, size, fontname, (r, g, b))
		self.rect.topleft = (x, y)

	def load_font(self, text, size, fontname, (r, g, b)):
		fullname = engine.get_file(fontname)
		font = pygame.font.Font(fullname, size)
		self.image = font.render(text, 1, (r, g, b))
		self.rect = self.image.get_rect()

