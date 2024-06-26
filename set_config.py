import configparser
import os

import flet as ft

from pathlib import Path

parser = configparser.ConfigParser()

config_path = os.path.join(str(Path(__file__).parent), 'assets', 'conf.ini')

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
        parser.add_section('theme')
        parser.set('theme', 'theme', 'DARK')
        
        parser.add_section('color')
        parser.set('color', 'color', 'blue')

        parser.add_section('bind')
        
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
        if args[0] == 'theme' or args[0] == 'color':
            parser.set(args[0], args[0], args[1])
        elif args[0] == 'bind':
            _key = args[2]
            _description = args[3]

            key = f'{args[1]}_key'
            description = f'{args[1]}_description'

            if _key != 'bind':
                parser.set(args[0], key, _key)
                parser.set(args[0], description, _description)
            
        
        with open(config_path, 'w') as configfile:
            parser.write(configfile)
        
    def delete(self, ID):
        key = f'{ID}_key'
        description = f'{ID}_description'

        parser.remove_option('bind', key)
        parser.remove_option('bind', description)

        with open(config_path, 'w') as configfile:
            parser.write(configfile)

    def get_binds(self):
        items = parser.items('bind')

        if items:
            sorted_data = {}
            for key, value in items:
                id_ = int(key.split('_')[0])
                field = key.split('_')[1]
                
                if id_ not in sorted_data:
                    sorted_data[id_] = {}
                    
                sorted_data[id_][field] = value

            items_grups = [{'id': id_, 'key': value['key'], 'description': value['description']} for id_, value in sorted_data.items()]

            items_grups = sorted(items_grups, key=lambda x: int(x['id']))

            return items_grups
