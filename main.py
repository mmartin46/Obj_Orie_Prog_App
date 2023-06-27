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
from screens.bridge import *
from screens.composite import *
from screens.decorator import *
from screens.facade import *
from screens.flyweight import *
from screens.proxy import *
from screens.chain import *
from screens.command import *
from screens.interpreter import *

d = Database()
print(d.get_listed_query("""select p_name from all_patterns"""))

# Used for the icons on the main
# screen.
class ElementCard(MDCard):
   pass

# Describes the object oriented
# programming overview.
class OOP_Screen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      self.db = Database()
      # Backdrop
      
   def on_enter(self, *args):
      self.bk_drop = MDFloatLayout()
      self.bk_drop.size_hint_y=None
      self.bk_drop.height=1900

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
      self.fp_c.fbind('on_press', self.trans_screen, scr='fmp')
      self.ap_c=ElementCard()
      self.ap_c.text='Abstract Pattern'
      self.ap_c.fbind('on_press', self.trans_screen, scr='abs')
      self.sp_c=ElementCard() 
      self.sp_c.text=str(GetDesignDesc('Single').get_name())
      self.sp_c.fbind('on_press', self.trans_screen, scr='sgl')
      self.pp_c=ElementCard()
      self.pp_c.text=str(GetDesignDesc('Proto').get_name())
      self.pp_c.fbind('on_press', self.trans_screen, scr='pp')
      self.bp_c=ElementCard()
      self.bp_c.text=str(GetDesignDesc('Builder').get_name())
      self.bp_c.fbind('on_press', self.trans_screen, scr='bp')
      self.op_p=ElementCard()
      self.op_p.text=str(GetDesignDesc('Object Pool').get_name())
      self.op_p.fbind('on_press', self.trans_screen, scr='op')
      self.ad_p=ElementCard()
      self.ad_p.text=str(GetDesignDesc('Adapter').get_name())
      self.ad_p.fbind('on_press', self.trans_screen, scr='ad')
      self.bgs_p=ElementCard()
      self.bgs_p.text=str(GetDesignDesc('Bridge').get_name())
      self.bgs_p.fbind('on_press', self.trans_screen, scr='bgs')
      self.com_p=ElementCard()
      self.com_p.text=str(GetDesignDesc('Composite').get_name())
      self.com_p.fbind('on_press', self.trans_screen, scr='com')
      self.dec_p=ElementCard()
      self.dec_p.text=str(GetDesignDesc('Decorator').get_name())
      self.dec_p.fbind('on_press', self.trans_screen, scr='dec')

      self.fac_p=ElementCard()
      self.fac_p.text=str(GetDesignDesc('Facade').get_name())
      self.fac_p.fbind('on_press', self.trans_screen, scr='fac')
      self.flw_p=ElementCard()
      self.flw_p.text=str(GetDesignDesc('Flyweight').get_name())
      self.flw_p.fbind('on_press', self.trans_screen, scr='flw')
      
      self.pro_p=ElementCard()
      self.pro_p.text=str(GetDesignDesc('Proxy').get_name())
      self.pro_p.fbind('on_press', self.trans_screen, scr='pro')
      
      self.cr_p=ElementCard()
      self.cr_p.text=str(GetDesignDesc('Chain').get_name())
      self.cr_p.fbind('on_press', self.trans_screen, scr='chs')
      
      self.cm_p=ElementCard()
      self.cm_p.text=str(GetDesignDesc('Command').get_name())
      self.cm_p.fbind('on_press', self.trans_screen, scr='cmd')
      
      self.it_p=ElementCard()
      self.it_p.text=str(GetDesignDesc('Interpreter').get_name())
      self.it_p.fbind('on_press', self.trans_screen, scr='its')
 
      print(self.ids)


      functions = [
         self.ov_c,
         self.fp_c,
         self.ap_c,
         self.pp_c,
         self.bp_c,
         self.op_p,
         self.ad_p,
         self.bgs_p,
         self.com_p,
         self.dec_p,
         self.fac_p,
         self.flw_p,
         self.pro_p,
         self.cr_p,
         self.cm_p,
         self.it_p
      ]
      
      for f in functions:
         self.grid.add_widget(f)
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

   def trans_screen(self, obj, scr):
      self.manager.current=str(scr)
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