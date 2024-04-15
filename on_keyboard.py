import flet as ft

class OnKeyboard:
    def __init__(self, page):
        self.page = page
        self.keykap = None

    def on_keyboard(self, e: ft.KeyboardEvent):
        self.keykap = e
        
    def keykap_changed(self):
        self.keykap = None
