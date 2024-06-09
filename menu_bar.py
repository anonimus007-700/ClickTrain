import flet as ft
from popup_color_item import PopupColorItem

class Menu(ft.Column):
    def __init__(self, gallery, setter):
        super().__init__()
        self.gallery = gallery
        self.setter = setter
        self.rail = ft.NavigationRail(
            extended=True,
            expand=True,
            selected_index=0,
            min_width=100,
            min_extended_width=200,
            group_alignment=-0.9,
            destinations=self.get_destinations(),
            on_change=self.control_group_selected,
        )

        try:
            if self.setter.theme == 'DARK':
                self.dark_light_text = ft.Text('Dark theme')
            else:
                self.dark_light_text = ft.Text('Light theme')
        except:
            self.dark_light_text = ft.Text('Dark theme')
        
        self.controls = [
            self.rail,
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_2_OUTLINED,
                                tooltip='Toggle brightness',
                                on_click=self.theme_changed,
                            ),
                            self.dark_light_text,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.PopupMenuButton(
                                icon=ft.icons.COLOR_LENS_OUTLINED,
                                items=[
                                    PopupColorItem(color='deeppurple', name='Deep purple', setter=self.setter),
                                    PopupColorItem(color='indigo', name='Indigo', setter=self.setter),
                                    PopupColorItem(color='blue', name='Blue (default)', setter=self.setter),
                                    PopupColorItem(color='teal', name='Teal', setter=self.setter),
                                    PopupColorItem(color='green', name='Green', setter=self.setter),
                                    PopupColorItem(color='yellow', name='Yellow', setter=self.setter),
                                    PopupColorItem(color='orange', name='Orange', setter=self.setter),
                                    PopupColorItem(color='deeporange', name='Deep orange', setter=self.setter),
                                    PopupColorItem(color='pink', name='Pink', setter=self.setter),
                                ],
                            ),
                            ft.Text('Seed color'),
                        ]
                    ),
                ]
            ),
        ]
        
    def get_destinations(self):
        destinations = []
        for destination in self.gallery.destinations_list:
            destinations.append(
                ft.NavigationRailDestination(
                    icon=destination.icon,
                    selected_icon=destination.selected_icon,
                    label=destination.label,
                )
            )
        return destinations

    async def control_group_selected(self, e):
        control_group_name = self.gallery.destinations_list[
            e.control.selected_index
        ].name
        await self.page.go_async(f'/{control_group_name}')

    async def theme_changed(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.dark_light_text.value = 'Dark theme'
            self.setter.write('theme', 'DARK')
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.dark_light_text.value = 'Light theme'
            self.setter.write('theme', 'LIGHT')
        await self.page.update_async()
