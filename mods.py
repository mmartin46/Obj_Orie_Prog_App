# The modules that are
# aimed to be used for the
# application.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import os
# Here are some useful modules for
# experimenting with the kivy interface.
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.lang.builder import Builder
from kivy.lang import Builder
from datetime import datetime
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import MDList, TwoLineListItem, ThreeLineIconListItem, TwoLineAvatarListItem,ThreeLineIconListItem, IconLeftWidget, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix import *
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import *
from kivy.uix.recycleview import RecycleView
import mysql.connector
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Color, Canvas, Line, RoundedRectangle
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from threading import Event
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.clock import Clock
import webbrowser
import time
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivy.uix.image import Image, AsyncImage
import os
os.environ['KIVY_IMAGE'] = 'pil'