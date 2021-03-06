from kivy.app import App
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from random import randint

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.btn = Button(text = 'Кнопочка', font_size = '50sp', background_normal = '')

    def btn_pressed(self, *args):
        self.btn.background_color = (randint(0,255)/255, randint(0, 255)/255, randint(0,255)/255, 1)
        self.btn.color = (randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1)

    def build(self):
        box = BoxLayout()
        box.add_widget(self.btn)
        self.btn.bind(on_press=self.btn_pressed)
        return box

if __name__ == '__main__':
    MyApp().run()
