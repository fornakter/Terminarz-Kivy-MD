from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass


class ScanScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanScreen())


class Scanner(MDApp):
    def build(self):
        return Builder.load_file('date.kv')

    def on_save(self, instance, value, date_range):
        self.root.ids.date_button.text = str(value)

    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = 'Anulacja'

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


Scanner().run()
