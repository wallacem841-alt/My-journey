from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Define the screens before loading KV
class MainPage(Screen):
    pass

class SecondPage(Screen):
    pass

# Define the main app
class MyKivyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name="main"))
        sm.add_widget(SecondPage(name="second"))
        return sm

# Run the app
if __name__ == "__main__":
    MyKivyApp().run()