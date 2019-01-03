"""Main File"""

import pyglet
import Drawer.py
import ImageAnalyzer.py

window = pyglet.window.Window()
titleTextOne = pyglet.text.Label('Kyle\'s', font_size = 24, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
titleTextTwo = pyglet.text.Label('Quick, Draw!', font_size = 36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')\

def on_draw():
    window.clear()
    titleTextOne.draw()
    titleTextTwo.draw()

pyglet.app.run()