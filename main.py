import flet as ft

from menu_bar import Menu
from gallerydata import GalleryData
from pages_view import PagesView
from set_config import SetTheme
from on_keyboard import OnKeyboard

async def main(page: ft.Page):
    page.title = 'Click Train'
    page.theme_mode = ft.ThemeMode.DARK

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window_center()

    setter = SetTheme(page)
    on_keyboard = OnKeyboard(page)
    gallery = GalleryData(page, on_keyboard, setter)

    def get_route_list(route):
        route_list = [item for item in route.split('/') if item != '']
        return route_list
    
    async def route_change(e):
        route_list = get_route_list(page.route)
        if len(route_list) == 0:
            page.go('/menu')
        elif len(route_list) == 1:
            await display_controls_pages(control_group_name=route_list[0])
        else:
            print('Invalid route')
            
    async def display_controls_pages(control_group_name):
        pages_view.display(control_group_name)
        page.update()

    menu = Menu(gallery=gallery, setter=setter)
    pages_view = PagesView(gallery=gallery, setter=setter)
    
    page.add(
        ft.Row(
            [
                menu,
                ft.VerticalDivider(width=1),
                pages_view
            ],
            expand=True
        ),
    )

    page.on_keyboard_event = on_keyboard.on_keyboard
    page.on_route_change = route_change
    page.go(page.route)

    
ft.app(target=main, assets_dir='assets')
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)