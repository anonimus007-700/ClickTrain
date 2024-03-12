import flet as ft

name = "setting"

def example():
    return ft.Column(controls=[
            ft.TextField(
                label="Меню програми",
                icon=ft.icons.FORMAT_SIZE,
                hint_text="Type your favorite color",
                helper_text="You can type only one color",
                counter_text="0 symbols typed",
                prefix_icon=ft.icons.COLOR_LENS,
                suffix_text="...is your color",
                ),
            ft.TextField(
                label="Тут буде опис як користуватися цею програмою",
                )
            ]
        )
