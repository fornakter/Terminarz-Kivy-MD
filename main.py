from kivymd.uix.picker import MDDatePicker
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.ptimary_palette = "BlueGray"
        return Builder.load_file('date.kv')

    def on_save(self, instance, value, date_range):
        self.root.ids.date_button.text = str(value)

    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = 'Anulacja'

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)
        date_dialog.open()

MainApp().run()