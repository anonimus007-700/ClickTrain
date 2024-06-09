import flet as ft
import importlib
import os

from pathlib import Path

class PageGroup:
    def __init__(self, name, returned):
        self.name = name
        self.returned = returned

class ControlGroup:
    def __init__(self, name, label, icon, selected_icon):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.grid_items = []

class GalleryData:
    def __init__(self, page, on_keyboard, setter):
        self.on_keyboard = on_keyboard
        self.page = page
        self.setter = setter
        self.import_modules()

    destinations_list = [
        ControlGroup(
            name='menu',
            label='Menu',
            icon=ft.icons.MENU,
            selected_icon=ft.icons.MENU_OPEN,
        ),
        ControlGroup(
            name='training',
            label='Training',
            icon=ft.icons.SPORTS_ESPORTS_OUTLINED,
            selected_icon=ft.icons.SPORTS_ESPORTS_ROUNDED,
        ),
        ControlGroup(
            name='setting',
            label='Setting',
            icon=ft.icons.SETTINGS_OUTLINED,
            selected_icon=ft.icons.SETTINGS,
        ),
    ]

    def import_modules(self):
        self.page_groups = []

        for name_module in self.destinations_list:
            module_path = os.path.join(str(Path(__file__).parent), 'pages', name_module.name)

            module = importlib.import_module(f'pages.{name_module.name}.index')
            
            if name_module.name != 'menu':
                returned_function = getattr(module, 'example', None)(self.page, self.on_keyboard, self.setter)
            else:
                returned_function = getattr(module, 'example', None)
                returned_function = returned_function()

            page_group = PageGroup(name=name_module.name, returned=returned_function)
            self.page_groups.append(page_group)

            
            

