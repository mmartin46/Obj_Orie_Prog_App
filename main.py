# John 3:16

# Mitchell Martin
# 05/15/2023


from mods import *
from bldr import *
from screens.overview import *
from screens.factory import *
from screens.abstract import *
from screens.singleton import *
from screens.prototype import *
from screens.builder import *
from screens.pool import *
from screens.adapter import *



# Used for the icons on the main
# screen.
class ElementCard(MDCard):
   pass

# Describes the object oriented
# programming overview.
class OOP_Screen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      # Backdrop
      
   def on_enter(self, *args):
      self.bk_drop = MDFloatLayout()
      self.bk_drop.size_hint_y=None
      self.bk_drop.height=1300

      # Screen Grid
      self.grid=MDGridLayout()
      self.grid.size_hint_y=.99
      self.grid.cols=2
      self.grid.padding=dp(15)
      self.grid.spacing=dp(15)

      self.ov_c=ElementCard()
      self.ov_c.text='Overview'
      self.ov_c.bind(on_press=self.trans_main_screen)
      self.fp_c=ElementCard()
      self.fp_c.text='Factory Pattern'
      self.fp_c.bind(on_press=self.trans_fact_screen)
      self.ap_c=ElementCard()
      self.ap_c.text='Abstract Pattern'
      self.ap_c.bind(on_press=self.trans_abs_screen)
      self.sp_c=ElementCard() 
      self.sp_c.text='Singleton Pattern'
      self.sp_c.bind(on_press=self.trans_sgl_screen)
      self.pp_c=ElementCard()
      self.pp_c.text='Prototype Pattern'
      self.pp_c.bind(on_press=self.trans_pp_screen)
      self.bp_c=ElementCard()
      self.bp_c.text='Builder Pattern'
      self.bp_c.bind(on_press=self.trans_bp_screen)
      self.op_p=ElementCard()
      self.op_p.text='Object Pool Pattern'
      self.op_p.bind(on_press=self.trans_op_screen)
      self.ad_p=ElementCard()
      self.ad_p.text='Adapter Pattern'
      self.ad_p.bind(on_press=self.trans_ad_screen)

      self.grid.add_widget(self.ov_c)
      self.grid.add_widget(self.fp_c)
      self.grid.add_widget(self.ap_c)
      self.grid.add_widget(self.sp_c)
      self.grid.add_widget(self.pp_c)
      self.grid.add_widget(self.bp_c)
      self.grid.add_widget(self.op_p)
      self.grid.add_widget(self.ad_p)
      self.bk_drop.add_widget(self.grid)

      # Title Layout
      self.title_lout = MDFloatLayout()
      self.title_lout.size_hint_y=.11
      self.title_lout.pos_hint={ "center_y" : .95 }
      self.title_lout.md_bg_color=COLOR_1
      # Label for Title
      self.title_label=Label()
      self.title_label.text='Object Oriented Programming Design Patterns'
      self.title_label.pos_hint={'center_y': .5}
      self.title_label.halign='center'
      self.title_label.font_size='25sp'
      self.title_label.theme_text_color='Custom'
      self.title_label.text_color={ 1, 1, 1, 1 }
      self.title_lout.add_widget(self.title_label)

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
      self.tool_lout.add_widget(self.back_btn_2)
      
      
      # Scroll View
      self.view=ScrollView()
      self.view.size_hint_y=.77
      self.view.scroll_y=1
      self.view.pos_hint={"x":0, "y": .116}
      self.view.do_scroll_x=False
      self.view.do_scroll_y=True
      

      self.add_widget(self.title_lout)
      self.view.add_widget(self.bk_drop)
      self.add_widget(self.view)
      self.add_widget(self.tool_lout)

   def trans_main_screen(self, obj):
      self.manager.current='main'
      self.manager.transition.direction='left'

   def trans_fact_screen(self, obj):
      self.manager.current='fmp'
      self.manager.transition.direction='left'

   def trans_abs_screen(self, obj):
      self.manager.current='abs'
      self.manager.transition.direction='left'

   def trans_sgl_screen(self, obj):
      self.manager.current='sgl'
      self.manager.transition.direction='left'

   def trans_pp_screen(self, obj):
      self.manager.current='pp'
      self.manager.transition.direction='left'

   def trans_bp_screen(self, obj):
      self.manager.current='bp'
      self.manager.transition.direction='left'

   def trans_op_screen(self, obj):
      self.manager.current='op'
      self.manager.transition.direction='left'

   def trans_ad_screen(self, obj):
      self.manager.current='ad'
      self.manager.transition.direction='left'

   def on_leave(self, *args):
      self.clear_widgets()      

# The Main Application object
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