from mods import *
from bldr import *
from widgets import *

class InterpreterScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # Backdrop
      self.bk_drop = MDFloatLayout()
      self.bk_drop.size_hint_y=None
      self.bk_drop.height=1600
      self.db = Database()

      # Title Layout
      self.title_lout = MDFloatLayout()
      self.title_lout.size_hint_y=.11
      self.title_lout.pos_hint={ "center_y" : .95 }
      self.title_lout.md_bg_color=COLOR_1
      # Label for Title
      self.title_label=Label()
      self.title_label.text=self.db.get_query("""SELECT p_name FROM all_patterns WHERE p_name LIKE 'Interpreter%'""")
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
      self.back_btn.bind(on_press=self.go_home) # CHANGE THIS

      self.title_lout.add_widget(self.back_btn)
      
      
      # Toolbar Layout
      self.tool_lout = MDFloatLayout()
      self.tool_lout.size_hint_y=.11
      self.tool_lout.pos_hint={'center_y': .05}
      self.tool_lout.md_bg_color=COLOR_1
         
      # Home Button
      self.home_btn=MDIconButton()
      self.home_btn.icon='home'
      self.home_btn.pos_hint={'center_x': .5, 'center_y': .5}
      self.home_btn.theme_icon_color='Custom'
      self.home_btn.icon_color=WHITE
      self.tool_lout.add_widget(self.home_btn)
      
      # Back Button
      self.back_btn_2=MDIconButton()
      self.back_btn_2.icon='backburger'
      self.back_btn_2.theme_icon_color='Custom'
      self.back_btn_2.icon_color=WHITE
      self.back_btn_2.pos_hint={'center_x': .2, 'center_y': .5}
      self.back_btn_2.bind(on_press=self.go_home) # CHANGE THIS
      self.tool_lout.add_widget(self.back_btn_2)
      
      
      # Scroll View
      self.view=ScrollView()
      self.view.size_hint_y=.77
      self.view.scroll_y=1
      self.view.pos_hint={"x":0, "y": .116}
      self.view.do_scroll_x=False
      self.view.do_scroll_y=True

      
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
      self.desc_label.text = str(GetDesignDesc('Interpreter').java_design_desc())
      self.desc_label.text_color = [23/255, 23/255, 23/255, 1 ]
      self.desc_label.halign='center'
      self.desc_label.pos_hint={'center_x': 0.5, 'center_y': 0.95}
      self.desc_label.font_size='20sp'
      
      self.bk_drop.add_widget(self.desc_label)
      
      self.img = Image(source='code_imgs\\interpreter_0.PNG')
      self.img.pos_hint={'center_x': 0.5, 'center_y': 0.86}
      self.img.size_hint_y=.8
      self.img.size_hint_x=.8
      self.bk_drop.add_widget(self.img)
            
      self.img_2 = Image(source='code_imgs\\interpreter_1.PNG')
      self.img_2.pos_hint={'center_x': 0.5, 'center_y': 0.78}
      self.img_2.size_hint_y=.6
      self.img_2.size_hint_x=.6
      self.bk_drop.add_widget(self.img_2)

      self.img_3 = Image(source='code_imgs\\interpreter_2.PNG')
      self.img_3.pos_hint={'center_x': 0.5, 'center_y': 0.63}
      self.img_3.size_hint_y=.8
      self.img_3.size_hint_x=.8
      self.bk_drop.add_widget(self.img_3)

      self.img_4 = Image(source='code_imgs\\interpreter_3.PNG')
      self.img_4.pos_hint={'center_x': 0.5, 'center_y': 0.43}
      self.img_4.size_hint_y=.8
      self.img_4.size_hint_x=.8
      self.bk_drop.add_widget(self.img_4)

      self.img_5 = Image(source='code_imgs\\interpreter_4.PNG')
      self.img_5.pos_hint={'center_x': 0.5, 'center_y': 0.33}
      self.img_5.size_hint_y=.8
      self.img_5.size_hint_x=.8
      self.bk_drop.add_widget(self.img_5)

      OFFSET=1.2
      
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
      self.add_widget(self.title_lout)
      self.view.add_widget(self.bk_drop)
      self.add_widget(self.view)
      self.add_widget(self.tool_lout)
      
      return self.bk_drop   
      
   def go_home(self, obj):
      self.manager.current='oop'
      self.manager.transition.direction='right'

   def insert_text(self, text, font_size, x, y, font_style='Body1'):
      """Inserts an MDLabel to the backdrop."""
      self.bk_drop.add_widget(MDLabel(
         text=str(text),
         halign='center',
         pos_hint={'center_x': x ,'center_y' : y},
         text_color=[23/255, 23/255, 23/255, 1 ],
         font_size=font_size,
         font_style=font_style
      ))   
   def on_leave(self, *args):
      self.clear_widgets()
      
      
