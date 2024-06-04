import flet as ft
import os

from pathlib import Path

class PagesView(ft.Column):
    def __init__(self, gallery, setter):
        super().__init__()
        self.expand = True
        self.setter = setter
        self.gallery = gallery

    def display(self, story):
        # file_path = os.path.join(str(Path(__file__).parent), "pages", story, "index.py")

        for pages in self.gallery.page_groups:
            if pages.name == story:
                self.controls = [pages.returned]
                break
