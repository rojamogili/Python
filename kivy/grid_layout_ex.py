
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class grid_layout(GridLayout):
    def __init__(self,**kwargs):
        super(grid_layout,self).__init__(**kwargs)
        
        self.grid=GridLayout()
        self.grid.cols=2
        
        self.cols=1
        self.grid.add_widget(Label(text="First Name: "))
        self.fname=TextInput(multiline=False)
        self.grid.add_widget(self.fname)
        
        self.grid.add_widget(Label(text="Last Name: "))
        self.lname=TextInput(multiline=False)
        self.grid.add_widget(self.lname)
        
        self.grid.add_widget(Label(text="Email: "))
        self.email=TextInput(multiline=False)
        self.grid.add_widget(self.email)
        
        self.add_widget(self.grid)
        #self.add_widget(TextInput(multiline=False))
        
        self.submit= Button(text="Submit", font_size=30)
        self.submit.bind(on_press=self.press_button)
        self.add_widget(self.submit)
        #self.add_widget(TextInput(multiline=False))
        
    def press_button(self, instance):
        print("Name: ", self.fname.text, self.lname.text)
        print("email: ", self.email.text)
        
        self.fname.text=""
        self.lname.text=""
        self.email.text=""
        
class myapp(App):
    def build(self):
        return grid_layout()
    
if __name__=='__main__':
    myapp().run()