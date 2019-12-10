import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class grid(Widget):
    fname=ObjectProperty(None)
    lname=ObjectProperty(None)
    email=ObjectProperty(None)
    
    def btnpress(self):
        print("Name: ",self.fname.text,self.lname.text)
        print("Email: ", self.email.text)
        self.fname.text=""
        self.lname.text=""
        self.email.text=""
    
    
class myapp(App):
    def build(self):
        return grid()
    
if __name__=='__main__':
    myapp().run()