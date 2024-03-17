import configparser
import os

import flet as ft

from pathlib import Path

parser = configparser.ConfigParser()

config_path = os.path.join(str(Path(__file__).parent), "assets", "conf.ini")

class SetTheme:
    def __init__(self, page):
        self.page = page
        # self.color = color
        
        if not os.path.isfile(config_path):
            self.create()
        else:
            parser.read(config_path)
            self.set_up()
    
    def create(self):
        parser.add_section("theme")
        parser.set("theme", "theme", "DARK")
        
        parser.add_section("color")
        parser.set("color", "color", "blue")

        parser.add_section("bind")
        
        with open(config_path, 'w') as configfile:
            parser.write(configfile)
    
    def set_up(self):
        self.theme = parser.get('theme', 'theme')
        self.theme_color = parser.get('color', 'color')
        
        self.page.theme_mode = getattr(ft.ThemeMode, self.theme)
        self.page.theme = self.page.dark_theme = ft.theme.Theme(
            color_scheme_seed=self.theme_color
        )
        
        self.page.update()
    
    def write(self, *args):
        for i in args[1:]:
            if args[0] == "theme" or args[0] == "color":
                parser.set(args[0], args[0], i)
            else:
                print(args[0])
        
        with open(config_path, 'w') as configfile:
            parser.write(configfile)