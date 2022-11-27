# import all the modules from kivy
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# creating a classes of child and parent
class childApp(GridLayout):
    def __int__(self, **kwargs):  # kwargs is use for adding unlimited arguments
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Applicant Name'))  # To create an applicant imput
        self.app_name = TextInput()  # To input applicant name
        self.add_widget(self.app_name)  # To save applicant name

        self.add_widget(Label(text='Applicant Gender'))
        self.app_gender = TextInput()
        self.add_widget(self.app_gender)

        self.add_widget(Label(text='Employment Status'))
        self.app_status = TextInput()
        self.add_widget(self.app_status)

        self.add_widget(Label(text='University Graduated'))
        self.app_uni = TextInput()
        self.add_widget(self.app_uni)

        self.add_widget(Label(text='Applicant Grade'))
        self.app_grade = TextInput()
        self.add_widget(self.app_grade)

        self.add_widget(Label(text='Graduation Year'))
        self.app_year = TextInput()
        self.add_widget(self.app_year)

        self.add_widget(Label(text='Applicant Age'))
        self.app_age = TextInput()
        self.add_widget(self.app_age)

        self.press = Button(text = 'Click Here')
        self.press.bind(on_click = self.click_here)
        self.add_widget(self.press)

    def click_here(self, instance):
        print("The name of applicant is " +self.app_name.text)
        print("The applicant gender is "+self.app_gender.text)
        print("The employment status is "+self.app_status.text)
        print("University graduated is "+self.app_uni.text)
        print("The applicant grade is "+self.app_grade.text)
        print("The graduation year is "+self.app_year.text)
        print("The applicant age is "+self.app_age.text)


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
