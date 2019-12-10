import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color

class drawing(Widget):
    def __init__(self, **kwargs):
        #super(Touch, self).__init__(**kwargs)
        
        with self.canvas:
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50,50))
    def on_touch_down(self, touch):
        print("Mouse down", touch)
    def on_touch_move(self, touch):
        print("Mouse move", touch)
        
    def on_touch_up(self, touch):
        print("mouse up", touch)
    
class myapp(App):
    def build(self):
        return drawing()
    
if __name__=="__main__":
    myapp().run()