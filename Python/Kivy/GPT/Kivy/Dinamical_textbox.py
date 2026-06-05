from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder

# Define the KV design
kv = """
<RegistrationPage>:
    orientation: "vertical"
    padding: 20
    spacing: 10

    Label:
        text: "Register Your Information"
        font_size: 24

    BoxLayout:
        orientation: "horizontal"
        size_hint_y: None
        height: 40
        Label:
            text: "Name:"
            size_hint_x: None
            width: 80
        TextInput:
            id: name_input
            hint_text: "Enter your name"

    Label:
        text: "Sports:"
        font_size: 18

    BoxLayout:
        id: sports_container
        orientation: "vertical"
        spacing: 5

    Button:
        text: "Add Another Sport"
        size_hint_y: None
        height: 40
        on_release: root.add_sport_input()

    Button:
        text: "Submit"
        size_hint_y: None
        height: 50
        on_release: root.submit_form()
"""

Builder.load_string(kv)

class RegistrationPage(BoxLayout):
    def add_sport_input(self):
        """Add a new text input field for sports."""
        new_sport_input = TextInput(hint_text="Enter a sport")
        self.ids.sports_container.add_widget(new_sport_input)

    def submit_form(self):
        """Handle the submission of the form."""
        name = self.ids.name_input.text
        sports = [widget.text for widget in self.ids.sports_container.children if isinstance(widget, TextInput)]
        print(f"Name: {name}")
        print("Sports:", sports)
        self.clear_form()

    def clear_form(self):
        """Clear the form inputs."""
        self.ids.name_input.text = ""
        self.ids.sports_container.clear_widgets()

class SportsRegistrationApp(App):
    def build(self):
        return RegistrationPage()

if __name__ == "__main__":
    SportsRegistrationApp().run()