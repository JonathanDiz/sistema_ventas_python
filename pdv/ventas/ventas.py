from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class VentasWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def admin(self):
        print("Admin presionado")

    def signout(self):
        print("Signout presionado")

class VentasApp(App):
    def build(self):
        return VentasWindow()


if __name__ == '__main__':
    VentasApp().run()
