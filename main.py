# John 3:16

# Mitchell Martin
# 05/15/2023

from mods import *
from bldr import *



class Java_Descriptions(object):
   """Handles the Java Main Design Descriptions"""
   def __init__(self):
      self.design_patterns = ['Creational Design Pattern', 'Structural Design Pattern', 'Behavioral Design Pattern']

   def java_design_desc(self):
      """Returns a description of Java Design Patterns"""
      desc = "In Core Java, there are three types of Java"
      desc += "design patterns."
      return desc
      
   def get_design_patterns(self):
      return self.design_patterns
   
class Creational_Design_Patterns(Java_Descriptions):
   """Handles the Creational Design Patterns"""
   def __init__(self):
      super(Java_Descriptions, self).__init__()
      self.name = 'Creational Design Patterns\n'
   
   def java_design_desc(self):
      """Returns the description of the Creational Design Patterns"""
      desc = "Creational Design Patterns are focused with"
      desc += " the way of creating objects. The design patterns are used when"
      desc += " a decision needs to be made at the time of the instantiation of a class."
      desc += "\nCreation Design Patterns can be further broken into the following patterns."
      return desc
   
   def types_of_patterns(self):
      """Returns the patterns"""
      types='• Factory Method Pattern\n'
      types+='• Abstract Factory Pattern\n'
      types+='• Singleton Pattern\n'
      types+='• Prototype Pattern\n'
      types+='• Builder Pattern\n'
      types+='• Object Pool Pattern\n'
      return types
   
   
   def get_name(self):
      return self.name
   
      

# All screens
class MainScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # Backdrop
      self.bk_drop = MDFloatLayout()


      # Title Layout
      self.title_lout = MDFloatLayout()
      self.title_lout.size_hint_y=.11
      self.title_lout.pos_hint={ "center_y" : .95 }
      self.title_lout.md_bg_color={ 0/255, 72/255, 186/255, 1 }
      # Label for Title
      self.title_label=Label()
      self.title_label.text='Object Oriented Programming'
      self.title_label.pos_hint={'center_y': .5}
      self.title_label.halign='center'
      self.title_label.font_size='25sp'
      self.title_label.theme_text_color='Custom'
      self.title_label.text_color={ 1, 1, 1, 1 }
      
      
      self.title_lout.add_widget(self.title_label)
      
      self.back_btn=MDIconButton()
      self.back_btn.pos_hint={'center_y': .5}
      self.back_btn.icon='keyboard-backspace'
      self.back_btn.halign='left'
      self.back_btn.theme_icon_color='Custom'
      self.back_btn.icon_color=[ 1, 1, 1, 1 ]
      self.title_lout.add_widget(self.back_btn)
      
   #   # Scroll View
   #   self.view=ScrollView()
   #   self.view.size_hint_y=.77
   #   self.view.scroll_y=0
   #   self.view.pos_hint={"x":0, "y": .116}
   #   self.view.do_scroll_x=False
   #   self.view.do_scroll_y=False

      
   #   # Layout within the Scroll View
   #   self.main_lout=MDBoxLayout()
   #   self.main_lout.size_hint_y=None
   #   self.main_lout.height=2000
   #   self.main_lout.width=self.width
   #   self.main_lout.adaptive_size=True
   #   self.main_lout.size_hint=[ None, None ]
   #   self.main_lout.pos_hint={'top' : 10}
   #   self.main_lout.cols=1
   #   self.main_lout.spacing=3
      
      

      # Description Label
      self.desc_label = MDLabel()
      self.desc_label.text = str(Java_Descriptions().java_design_desc())
      self.desc_label.text_color = [23/255, 23/255, 23/255, 1 ]
      self.desc_label.halign='center'
      self.desc_label.pos_hint={'center_x': 0.5, 'center_y': 0.8}
      self.desc_label.font_size='20sp'
      
      self.bk_drop.add_widget(self.desc_label)
      
      self.ds_1 = MDLabel(
         text='• Creational Design Pattern\n' +
              '• Structural Design Pattern\n' +
              '• Behavioral Design Pattern',
         halign='center',
         pos_hint={'center_x': 0.5, 'center_y' : 0.7},
         text_color=[23/255, 23/255, 23/255, 1 ],
         font_size='10sp'
      )
      self.bk_drop.add_widget(self.ds_1)
      
      self.ds_2 = MDLabel(
         text='Creational Design Pattern\n',
         halign='center',
         pos_hint={'center_x': 0.5, 'center_y' : 0.6},
         text_color=[23/255, 23/255, 23/255, 1 ],
         font_size='20sp'
      )
      self.bk_drop.add_widget(self.ds_2)
      
      self.insert_text(Creational_Design_Patterns().java_design_desc(), '20sp', 0.5, 0.5)
      self.insert_text(Creational_Design_Patterns().types_of_patterns(), '10sp', 0.5, 0.34)


      """
      self.ds_2 = MDLabel(
         text=str(Creational_Design_Patterns().types_of_patterns()),
         halign='center',
         pos_hint={'center_x': 0.5, 'center_y': 0.6},
         text_color=[23/255, 23/255, 23/55, 1 ],
         font_size='10sp'
      )
      self.bk_drop.add_widget(self.ds_2)
      """
      
      # Adding the widgets
      # self.view.add_widget(self.main_lout)
      self.bk_drop.add_widget(self.title_lout)
      self.add_widget(self.bk_drop)
      
      return self.bk_drop   
      

   def insert_text(self, text, font_size, x, y):
      self.bk_drop.add_widget(MDLabel(
         text=str(text),
         halign='center',
         pos_hint={'center_x': x ,'center_y' : y},
         text_color=[23/255, 23/255, 23/255, 1 ],
         font_size=font_size
      ))      
   


class OOP_Screen(Screen):
   pass

# Screen Manager
# Handles all the screens


app_build = """

ScreenManager:
   MainScreen:
   OOP_Screen:
   
<MainScreen>
   name: 'main'
   
<OOP_Screen>
   name: 'oop'
  
<ElementCard@MDCard>
   id: try
   size_hint_y: None
   padding: dp(20)
   radius: dp(25)
   icon: ''
   text: ''
   md_bg_color: [ 0/255, 72/255, 186/255, 1 ]
   theme_text_color: "Custom"
   text_color: [ 1, 1, 1, 1 ]
   ripple_behavior: True
   subtext: ''
   items_remaining: ''
   height: dp(175)
   oritentation: 'vertical'
   Image:
      source:root.image
      width: 250
      size_hint_y: None
      padding: dp(10)
   MDLabel:
      halign: 'center'
      text: 0, 0, 0, 1
   MDLabel:
      halign: 'center'
      text: root.text
      font_size: 'H6'
   MDLabel:
      halign: 'center'
      text: root.items_remaining    
"""


class MainApp(MDApp):
   def build(self):
      self.root_widget = Builder.load_string(app_build)
      return self.root_widget


# Runs the application
if __name__ == '__main__':
   MainApp().run()
   
   
# Citations
"""
Object Oriented Programming
https://codeinstitute.net/global/blog/object-oriented-programming/


"""