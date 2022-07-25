from kivy.clock import mainthread
from kivy.properties import ObjectProperty
from kivymd.uix.picker import MDDatePicker
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from camera4kivy import Preview
from PIL import Image
from pyzbar.pyzbar import decode


class FirstWindow(Screen):
    pass


class SecoundWindow(Screen):
    def on_kv_post(self, obj):
        try:
            self.ids.preview.connect_camera(enable_analyze_pixels=True, default_zoom=0.0)
        except Exception as e:
            print(e)
            # Error: 'super' object has no attribute '__getattr__'

        else:
            self.root.get_screen('secound').ids.preview.connect_camera(enable_analyze_pixels=True, default_zoom=0.0)
            # Error: AttributeError: 'ScanScreen' object has no attribute 'root'

    @mainthread
    def got_result(self, result):
        self.ids.ti.text = str(result)


class WindowManager(ScreenManager):
    pass


class ScanAnalyze(Preview):
    extracted_data = ObjectProperty(None)

    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        pimage = Image.frombytes(mode='RGBA', size=image_size, data=pixels)
        list_of_all_barcodes = decode(pimage)

        if list_of_all_barcodes:
            if self.extracted_data:
                self.extracted_data(list_of_all_barcodes[0])
            else:
                print("Not found")


sm = ScreenManager()
sm.add_widget(FirstWindow(name='first'))
sm.add_widget(SecoundWindow(name='secound'))


class ReadQR(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.ptimary_palette = "BlueGray"
        return Builder.load_file('qrscan.kv')

    def on_save(self, instance, value, date_range):
        self.root.get_screen('first').ids.date_button.text = str(value)
        pass

    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


if __name__ == '__main__':
    ReadQR().run()
