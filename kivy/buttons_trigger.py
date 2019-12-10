
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class grid_layout(GridLayout):
    def __init__(self,**kwargs):
        super(grid_layout,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="First Name: "))
        self.fname=TextInput(multiline=False)
        self.add_widget(self.fname)
        
        self.add_widget(Label(text="Last Name: "))
        self.lname=TextInput(multiline=False)
        self.add_widget(self.lname)
        
        self.add_widget(Label(text="Email: "))
        self.email=TextInput(multiline=False)
        self.add_widget(self.email)
        
        self.submit= Button(text="Submit", font_size=40)
        self.add_widget(self.submit)
        
class myapp(App):
    def build(self):
        return grid_layout()
    
if __name__=='__main__':
    myapp().run()