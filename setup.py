from distutils.core import setup

files = ["data/*"]

setup(name = "Forever Glow",
	version = "1.0",
	description = "LudumDare entry",
	author = "StarLight",
	author_email = "ohaistarlight@gmail.com",
	url = "http://strlght.ru",
	packages = ['package'],
	package_data = {'package' : files },
	scripts = ["glow"],
	long_description = """StarLight's LudumDare 22 Entry!"""
)
