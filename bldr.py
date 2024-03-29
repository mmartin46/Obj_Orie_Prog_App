# Constants
WHITE = [ 1, 1, 1, 1 ]
COLOR_1 = { 0/255, 72/255, 186/255, 1 }

# The string below represents
# the StringBuilder which is
# used to create the structure
# of the application.
app_build = """

ScreenManager:
   OOP_Screen:
   OverviewScreen:
   FactoryScreen:
   AbstractScreen:
   SingletonScreen:
   PrototypeScreen:
   BuilderScreen:
   ObjPoolScreen:
   AdapterScreen:
   BridgeScreen:
   CompositeScreen:
   DecoratorScreen:
   FacadeScreen:
   FlyWeightScreen:
   ProxyScreen:
   ChainScreen:
   CommandScreen:
   InterpreterScreen:
   IteratorScreen:
   MediatorScreen:
   MementoScreen:
   ObserverScreen:
   StateScreen:
   StrategyScreen:
   TemplateScreen:
   
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

<BuilderScreen>
   name: 'bp'
   
<ObjPoolScreen>
   name: 'op'
   
<AdapterScreen>
   name: 'ad'

<BridgeScreen>
   name: 'bgs'
  
<CompositeScreen>
   name: 'com'
   
<DecoratorScreen>
   name: 'dec'

<FacadeScreen>
   name: 'fac'

<FlyWeightScreen>
   name: 'flw'
   
<ProxyScreen>
   name: 'pro'   
   
<ChainScreen>
   name: 'chs'
   
<CommandScreen> 
   name: 'cmd'
   
<InterpreterScreen>   
   name: 'its'
   
<IteratorScreen>
   name: 'itr'
   
<MediatorScreen>
   name: 'med'

<MementoScreen>
   name: 'mem'
   
<ObserverScreen>
   name: 'obj'

<StateScreen>
   name: 'ste'

<StrategyScreen>
   name: 'stg'

<TemplateScreen>
   name: 'tmp'
   
<ElementCard@MDCard>:
   id: try
   size_hint_y: None
   padding: dp(20)
   radius:dp(25)
   icon:''
   icon_size: dp(30)
   image:'code_imgs/button_icon.png'
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
