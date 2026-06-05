from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HelloKivyApp(App):
    def build(self):
        # Create a BoxLayout to hold the widgets
        layout = BoxLayout(orientation='vertical')

        # Create a Label
        self.label = Label(text="Hello, Kivy!")
        layout.add_widget(self.label)

        # Create a Button and bind it to the on_button_click method
        button = Button(text="Click Me!")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Change the label text when the button is clicked
        self.label.text = "Button Clicked!"

# Run the app
if __name__ == '__main__':
    HelloKivyApp().run()
