from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from datetime import datetime
from kivy.clock import Clock


class ScrButton(Button):
   def __init__(self, screen, goal="first",direction="right",**kwargs):
      super().__init__(**kwargs)
      self.screen = screen
      self.goal = goal
      self.direction = direction

   def on_press(self):
      self.screen.manager.transition.direction = self.direction
      self.screen.manager.current = self.goal

class FirstScr(Screen):
   def __init__(self, name = "first"):
      super().__init__()
      self.name = name
      boxM = BoxLayout()
      boxB = BoxLayout(orientation="vertical")
      lable = Label(text="Оберіть екран")
      one = ScrButton(self,  goal="second", direction="up",text="1")
      two = ScrButton(self,  goal="third", direction="left",text="2")
      three = ScrButton(self,  goal="fourth", direction="down",text="3")
      four = ScrButton(self,  goal="fifth", direction="right",text="4")
      boxM.add_widget(lable)
      boxB.add_widget(one)
      boxB.add_widget(two)
      boxB.add_widget(three)
      boxB.add_widget(four)
      boxM.add_widget(boxB)
      self.add_widget(boxM)

class SecondScr(Screen):
   def __init__(self, name="second"):
      super().__init__()
      self.name = name
      boxM = BoxLayout(orientation='vertical',size_hint=('.5sp', '.5sp'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
      one = Button(text="Вибір1",size_hint=('.5sp', '1sp'), pos_hint={'left': 0})
      two = ScrButton(self, goal="first", direction="down",text="Назад",size_hint=('.5sp', '1sp'), pos_hint={'right': 1})
      boxM.add_widget(one)
      boxM.add_widget(two)
      self.add_widget(boxM)
class ThirdScr(Screen):
   def on_pr(self, a):
      self.label.text = self.inp.text


   def __init__(self, name="third"):
      super().__init__()
      self.name = name
      boxM = BoxLayout(orientation='vertical')
      boxI = BoxLayout(size_hint=("1sp", '.075sp'),pos_hint={'center_x': 0.5, 'center_y': 0.5})
      boxB = BoxLayout(size_hint=('.5sp', None),pos_hint={'center_x': 0.5, 'center_y': 0.5})
      self.label = Label(text="Текст:",font_size='20sp')
      one = ScrButton(self, goal="first", direction="right", text="Назад",size_hint=('.5sp', None))
      two = Button(text="Ок :)",size_hint=('.5sp', None),on_press=self.on_pr)
      self.inp = TextInput(text="", multiline=False, halign="left")
      inp_label = Label(text="Введіть текст:")
      boxB.add_widget(one)
      boxB.add_widget(two)
      boxM.add_widget(self.label)
      boxI.add_widget(inp_label)
      boxI.add_widget(self.inp)
      boxM.add_widget(boxI)
      boxM.add_widget(boxB)
      self.add_widget(boxM)

class FourthScr(Screen):
   playing=False
   sound = SoundLoader.load('mus.mp3')
   def on_pr(self, a):
      currentDateAndTime = datetime.now()
      self.label.text = self.inp.text +"    "+currentDateAndTime.strftime("%H:%M")
      self.inp.text = ""

   def pl(self):
      self.playing = True
      self.sound_pos = 0
      self.sound.play()
      self.play.text = "Stop"
      self.inp_label.text = "Введіть коментар:\n(you were rickrolled ;) )"



   def stop(self):
      self.sound.stop()
      self.play.text = "Play"

   def on_press(self,a):
      self.playing = not self.playing
      if self.playing == True:
         self.pl()
      else:
         self.stop()

   def __init__(self, name="fourth"):
      super().__init__()
      self.name = name
      boxM = BoxLayout(orientation='vertical')
      self.label = Label(size_hint_y=None,font_size="24sp",halign="center", text="")
      self.inp_label = Label(text="Введіть коментар:")
      self.inp = TextInput(text="", multiline=False, halign="left", size_hint=('.5sp', '.5sp'), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size="24sp")
      comm = Button(text="Відправити", size_hint=('.5sp', None), on_press=self.on_pr, pos_hint={'center_x': 0.5, 'center_y': 0.5})
      self.play = Button(on_press=self.on_press, text = 'Play', size_hint_y=".5sp")
      home = ScrButton(self, goal="first", direction="up", text="Назад")
      boxM.add_widget(self.play)
      boxM.add_widget(self.label)
      boxM.add_widget(self.inp_label)
      boxM.add_widget(self.inp)
      boxM.add_widget(comm)
      boxM.add_widget(home)
      self.add_widget(boxM)


class FifthScr(Screen):
   def __init__(self, name="fifth"):
      super().__init__()
      self.name = name
      boxM = BoxLayout(orientation='vertical')
      lab = Label(text="Домашне завдання:",halign="left")
      home = ScrButton(self, goal="first", direction="left", text="Назад", size_hint_y=".25sp",valign="top")
      self.label = Label(size_hint_y=None,font_size="24sp",halign="left", valign="top",
                         text="TextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextTextText")
      scroll = ScrollView(size_hint=(1,1))
      scroll.add_widget(self.label)
      self.label.bind(size=self.resize)
      boxM.add_widget(lab)
      boxM.add_widget(home)
      boxM.add_widget(scroll)
      self.add_widget(boxM)

   def resize(self,a,b):
      self.label.text_size = (self.label.width, None)
      self.label.texture_update()
      self.label.height = self.label.texture_size[1]


class MyApp(App):
   def build(self):
      self.title = '4 windows'
      scrMan = ScreenManager()
      scrMan.add_widget(FirstScr(name="first"))
      scrMan.add_widget(SecondScr(name="second"))
      scrMan.add_widget(ThirdScr(name="third"))
      scrMan.add_widget(FourthScr(name="fourth"))
      scrMan.add_widget(FifthScr(name="fifth"))
      return scrMan

app = MyApp()
app.run()