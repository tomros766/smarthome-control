# author: Tomasz Rosiek
# e-mail: trosiek@student.agh.edu.pl

from src.gui.gui import App
import json

f = open("config.json", "r")
config = json.loads(f.read())
App(config)
