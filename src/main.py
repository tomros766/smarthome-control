from src.gui.gui import App
import json

f = open("sample.json", "r")
list1 = json.loads(f.read())
App(list1)
input()
