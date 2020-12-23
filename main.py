import kivy
from kivy.app import App
#from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.modules import keybinding
import numpy as np
import matplotlib.pyplot as plt


class CalcLayout(Widget):
    def graph(self,expression):
        try:
            y = eval(expression)
            plt.plot(y)
            plt.ylabel('y') 
            plt.show()

        except Exception:
            self.display.text="Error\nMake sure all parentheses are closed"
            

    def calculate(self,expression):
        if expression:
            try:
                self.display.text=str(eval(expression))
            except Exception:
                self.display.text="Error"
        

class CalcApp(App):

    def build(self):
        
        return CalcLayout()


if __name__=='__main__':
    CalcApp().run()
