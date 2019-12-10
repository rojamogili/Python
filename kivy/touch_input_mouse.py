import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Touchi(Widget):
    btn= ObjectProperty(None)
    
    def on_touch_down(self, touch):
        print("Mouse Down",touch)
        print(dir(btn))
        #self.btn.opacity=0.5
    
    def on_touch_up(self, touch):
        print("Mouse Up",touch)
        #self.btn.opacity = 1
    
    def on_touch_move(self, touch):
        print("Mouse Move", touch)

class touchapp(App):
    def build(self):
        return Touchi()
    
if __name__=="__main__":
    touchapp().run()