import flet as ft

from random import choice

class TrainingApp:
    def __init__(self, page, on_keyboard, setter):
        super().__init__()
        self.page = page
        self.on_keyboard = on_keyboard
        self.setter = setter

        self.button_text = ft.Text("Press\nHello!", style=ft.TextThemeStyle.HEADLINE_MEDIUM)

        self.button = ft.AnimatedSwitcher(
            self.button_text,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=300,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        )

        self.preparation_view = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.TextField(value=20, label='Number of questions', max_length=5,
                            text_align=ft.TextAlign.CENTER, input_filter=ft.NumbersOnlyInputFilter(),
                            width=400)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                ft.Row(
                    controls=[
                        ft.TextButton('Start', on_click=self.start)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            height=500,
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.train_view = ft.Column(
            [
                ft.TextButton('Stop', on_click=self.stop),
                ft.Column(
                    [
                    ft.Row(controls=[
                            self.button
                        ],
                        alignment=ft.MainAxisAlignment.CENTER),
                    ],
                    height=500,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            visible=False,
        )
    
    def build(self):
        return ft.Column(
            controls = [
                self.preparation_view,
                self.train_view
            ],
            expand=True
        )

    def start(self, e):
        self.train_view.visible = True
        self.preparation_view.visible = False
        self.page.update()
    
    def stop(self, e):
        self.train_view.visible = False
        self.preparation_view.visible = True
        self.page.update()

def example(page, on_keyboard, setter):
    zxc = TrainingApp(page, on_keyboard, setter).build()

    return zxc
