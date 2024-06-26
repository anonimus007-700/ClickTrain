import flet as ft

class PopupColorItem(ft.PopupMenuItem):
    def __init__(self, color, name, setter):
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.icons.COLOR_LENS_OUTLINED, color=color),
                ft.Text(name),
            ],
        )
        self.on_click = self.seed_color_changed
        self.data = color
        self.setter = setter

    async def seed_color_changed(self, e):
        self.page.theme = self.page.dark_theme = ft.theme.Theme(
            color_scheme_seed=self.data
        )
        
        self.setter.write('color', self.data)
        
        await self.page.update_async()
