import engine
import pyclbr
import levels
from levels import *

def start():
	eng = engine.Engine(640, 480, 6, "Glow")
	eng.play_music("music.ogg", -1)
	eng.set_background(entity.Entity("logo.png", 0, 0))
	eng.render()
	eng.delay(1500)
	eng.clear()
	eng.set_background(entity.Entity("black.png", 0, 0))
	eng.add_entity(entity.Text("G", 72, "m46.TTF", (230, 230), (255, 0, 0)))
	eng.add_entity(entity.Text("L", 72, "m46.TTF", (270, 230), (0, 255, 0)))
	eng.add_entity(entity.Text("O", 72, "m46.TTF", (290, 230), (0, 0, 255)))
	eng.add_entity(entity.Text("W", 72, "m46.TTF", (340, 230), (255, 255, 255)))
	eng.render()
	eng.delay(2000)
	eng.clear()
	lvls = [getattr(levels, level)(eng) for level in pyclbr.readmodule("package.levels").keys() if level.startswith("Level") and len(level) > 5]
	for level in lvls:
		while not level.completed:
			level.run()
			if not level.completed:
				eng.clear()
				eng.set_background(entity.Entity("death.png", 0, 0))
				eng.render()
				eng.delay(300)

