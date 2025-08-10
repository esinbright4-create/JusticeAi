from kivy.app import App
from kivy.uix.label import Label

class JusticeApp(App):
    def build(self):
        return Label(text='Justice AI - Ready!')

if __name__ == '__main__':
    JusticeApp().run()