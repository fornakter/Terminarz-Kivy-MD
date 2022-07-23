# Qrcode Barcode Scanner using kivy ,kivymd Python

from kivy.properties import ObjectProperty
from kivy.clock import mainthread
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from camera4kivy import Preview
from PIL import Image
from pyzbar.pyzbar import decode
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class ScanScreen(MDScreen):

    def on_kv_post(self, obj):
        try:
            self.ids.preview.connect_camera(enable_analyze_pixels=True, default_zoom=0.0)
        except Exception as e:
            print(e, ' on_kv_post')
            # Error: 'super' object has no attribute '__getattr__'

        else:
            self.root.get_screen('secound').ids.preview.connect_camera(enable_analyze_pixels=True, default_zoom=0.0)
            # Error: AttributeError: 'ScanScreen' object has no attribute 'root'

    @mainthread
    def got_result(self, result):
        try:
            self.ids.ti.text = str(result)
        except Exception as e:
            print(e, ' got_result')
        else:
            self.root.get_screen('secound').ids.ti.text = str(result)
        print(result[0])


sm = ScreenManager()
sm.add_widget(FirstWindow(name='first'))
sm.add_widget(ScanScreen(name='secound'))


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


class QRScan(MDApp):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.RECORD_AUDIO])
        return ScanScreen()


if __name__ == '__main__':
    QRScan().run()
