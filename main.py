from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from configparser import ConfigParser
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel


Window.size = (450, 700)
Window.top = 100
Window.left = 100


class app(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = 2

    def build(self):
        self.mainLayout = MDFloatLayout(size_hint=(1, 1))
        
        self.navBar = MDFloatLayout()
        self.navBar.size_hint=(1, .06)
        self.navBar.pos_hint = {'x':0, 'y':.95}
        self.navBar.md_bg_color = "orange"

        self.navBtnWriter = MDRectangleFlatIconButton()
        self.navBtnWriter.icon="calendar-text"
        self.navBtnWriter.text = "[b]Заметки[/b]"
        self.navBtnWriter.pos_hint = {'center_x':.75, 'y':.01}
        self.navBtnWriter.size_hint = (.5, .06)
        self.navBtnWriter.line_color = "orange"
        self.navBtnWriter.text_color = "green"
        self.navBtnWriter.icon_color = "green"
        self.navBtnWriter.markup = True
        self.navBtnWriter.on_press = lambda: self.animSlider(state=2)

        self.navBtnShop = MDRectangleFlatIconButton()
        self.navBtnShop.icon="format-list-bulleted-square"
        self.navBtnShop.text = "[b]Товар[/b]"
        self.navBtnShop.pos_hint = {'center_x':.25, 'y':.01}
        self.navBtnShop.size_hint = (.5, .06)
        self.navBtnShop.line_color = "orange"
        self.navBtnShop.text_color = "green"
        self.navBtnShop.icon_color = "green"
        self.navBtnShop.markup = True
        self.navBtnShop.on_press = lambda: self.animSlider(state=1)

        self.slider = MDFloatLayout()
        self.slider.size_hint = (.5, .1)
        self.slider.pos_hint = {'center_x':.75, 'y':0}
        self.slider.md_bg_color = "red"

        self.contentWriter = MDFloatLayout()
        self.contentWriter.md_bg_color = "gray"
        self.contentWriter.size_hint = (1, .95)
        self.contentWriter.pos_hint = {"center_x":-1.5, 'center_y':.475}

        self.contentShop = MDFloatLayout()
        self.contentShop.md_bg_color = "green"
        self.contentShop.size_hint = (1, .95)
        self.contentShop.pos_hint = {"center_x":.5, 'center_y':.475}

        self.mainLayout.add_widget(self.navBar)
        self.navBar.add_widget(self.navBtnWriter)
        self.navBar.add_widget(self.navBtnShop)
        self.navBar.add_widget(self.slider)
        self.mainLayout.add_widget(self.contentWriter)
        self.mainLayout.add_widget(self.contentShop)

        return self.mainLayout
    

    def animSlider(self, state):
        if self.state == 1 and state == 1:
            pass
        elif self.state == 2 and state == 2:
            pass
        else:
            buff = 0
            if state == 1:
                buff = .25
                self.state = 1
            else:
                self.state = 2
                buff = .75
            buff1 = -1.5
            buff2 = .5
            anim = Animation(
                pos_hint={'center_x':buff},
                d=.8,
                t="in_out_back"
            )
            anim1 = Animation(
                pos_hint={'center_x':buff1},
                d=.8,
                t="in_out_back"
            )
            anim2 = Animation(
                pos_hint={'center_x':buff2},
                d=.8,
                t="in_out_back"
            )
            anim.start(self.slider)
            if state == 2:
                anim1.start(self.contentWriter)
                anim2.start(self.contentShop)
            else:
                anim1.start(self.contentShop)
                anim2.start(self.contentWriter)


app().run()