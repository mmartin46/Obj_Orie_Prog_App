# Constants
WHITE = [ 1, 1, 1, 1 ]
COLOR_1 = { 0/255, 72/255, 186/255, 1 }

# The string below represents
# the StringBuilder which is
# used to create the structure
# of the application.
app_build = """

ScreenManager:
   OverviewScreen:
   OOP_Screen:
   FactoryScreen:
   AbstractScreen:
   SingletonScreen:
   PrototypeScreen:
   
<OverviewScreen>
   name: 'main'
   
<OOP_Screen>
   name: 'oop'
   
<FactoryScreen>
   name: 'fmp'
   
<AbstractScreen>
   name: 'abs'
  
<SingletonScreen>
   name: 'sgl'
   
<PrototypeScreen>
   name: 'pp'
  
<ElementCard@MDCard>:
   id: try
   size_hint_y: None
   padding: dp(20)
   radius:dp(25)
   icon:''
   icon_size: dp(30)
   image:''
   text:""
   md_bg_color: [ 196/255, 255/255, 215/255, 1 ]
   theme_text_color: "Custom"
   text_color: 240/255, 240/255, 240/255, 1
   ripple_behavior: True
   subtext: ''
   items_remaining: ''
   height:dp(175)
   orientation: 'vertical'
   Image:
      source:root.image
      width: 250
      size_hint_y: None
      padding: dp(10)
   MDLabel:
      halign: "center"
      valign: "bottom"
      text: root.text
      theme_text_color: "Custom"
      text_color: 0, 0, 0, 1
   MDLabel:
      halign: "center"
      text: root.subtext
      font_style:"H6"
   MDLabel:
      halign: "center"
      text: root.items_remaining  
"""
