import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class example(Widget):
    layout=FloatLayout(size=(100,100))
    button=Button(text="Hello", size_hint=(.5, .25), pos=(20, 20))
    layout.add_widget(button)
    

class floatlayout(App):
    def build(self):
        return example()
    
if __name__=='__main__':
    floatlayout().run()