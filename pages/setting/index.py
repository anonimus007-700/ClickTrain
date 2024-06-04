import flet as ft


class Task(ft.UserControl):
    current_id = 0
    def __init__(self, key, description, task_delete, on_keyboard, setter):
        super().__init__()
        self.ID = Task.current_id
        Task.current_id += 1

        self.key = key
        self.description = description
        self.task_delete = task_delete

        self.on_keyboard = on_keyboard
        self.setter = setter

        self.press_dlg = ft.AlertDialog(
                title=ft.Text("Please press the key"),
                actions=[
                    ft.TextButton("Cancel", on_click=lambda e: self.close_dlg()),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: self.close_dlg(),
            )

        self.setter.write('bind', self.ID, self.key, self.description)

    def build(self):
        self.key_display = ft.Text(self.key)

        self.display_key = ft.Container(
            self.key_display,
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=5,
            border_radius=10
        )

        self.display_description = ft.Container(
            ft.Text(self.description),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=5,
            border_radius=10
        )

        if self.display_description.content.value == '':
            self.display_description.visible = False

        self.edit_key_presed = ft.Text(self.key)
        
        self.edit_key = ft.Row(controls=[
                    ft.IconButton(
                        icon=ft.icons.KEYBOARD,
                        tooltip="Set bind",
                        on_click=lambda e: self.on_presed()
                    ),
                    self.edit_key_presed
                ],
            expand=True
        )
        self.edit_description = ft.TextField(hint_text="Description", max_length=20, expand=True)

        self.display_view = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_key,
                self.display_description,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_key,
                self.edit_description,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])
    
    def on_presed(self):
        global reading
        self.open_dlg_modal(self.page)

        self.on_keyboard.keykap_changed()
        previous = self.on_keyboard.keykap

        reading = True

        while reading:
            if previous != self.on_keyboard.keykap:
                self.edit_key_presed.value = f"Seted {self.on_keyboard.keykap.key}"
                self.display_key.content.value = self.edit_key_presed.value
                self.close_dlg()
                break
            previous = self.on_keyboard.keykap

        self.update()

    def open_dlg_modal(self, *args):
        self.page.dialog = self.press_dlg
        self.press_dlg.open = True
        self.page.update()

    def close_dlg(self, *args):
        global reading
        reading = False
        self.press_dlg.open = False
        self.page.update()

    def edit_clicked(self, e):
        self.edit_description.value = self.display_description.content.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.key_display = self.edit_key_presed
        self.display_description.content.value = self.edit_description.value
        self.display_view.visible = True
        self.edit_view.visible = False

        self.setter.write('bind', self.ID, self.key_display.value, self.display_description.content.value)

        if self.display_description.content.value == '':
            self.display_description.visible = False
        else:
            self.display_description.visible = True

        self.update()

    def delete_clicked(self, e):
        self.setter.delete(self.ID)
        self.task_delete(self)


class TodoApp(ft.UserControl):
    def __init__(self, page, on_keyboard, setter):
        super().__init__()
        self.page = page
        self.on_keyboard = on_keyboard
        self.setter = setter

        self.page.banner = ft.Banner(
            bgcolor=ft.colors.PRIMARY_CONTAINER,
            leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
            content=ft.Text(
                "Please, enter a key"
            ),
            actions=[
                ft.TextButton("Ok", on_click=self.close_banner),
            ],
        )

        self.press_dlg = ft.AlertDialog(
                title=ft.Text("Please press the key"),
                actions=[
                    ft.TextButton("Cancel", on_click=lambda e: self.close_dlg(e)),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: self.close_dlg(),
            )

    def build(self):
        self.key_presed = ft.Text("Set bind")
        self.new_key = ft.Row(controls=[
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD,
                            tooltip="Set bind",
                            on_click=lambda e: self.on_presed()
                        ),
                        self.key_presed
        ])
        self.new_description = ft.TextField(hint_text="Description", max_length=20, expand=True)
        self.tasks = ft.Column()

        self.on_start()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_key,
                        self.new_description,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
            expand=True
        )

    def on_presed(self):
        global reading
        self.open_dlg_modal(self.page)

        self.on_keyboard.keykap_changed()
        previous = self.on_keyboard.keykap

        reading = True

        while reading:
            if previous != self.on_keyboard.keykap:
                self.key_presed.value = f"Seted {self.on_keyboard.keykap.key}"
                self.close_dlg()
                break
            previous = self.on_keyboard.keykap

        self.page.update()

    def show_banner(self, *args):
        self.page.banner.open = True
        self.page.update()

    def close_banner(self, *args):
        self.page.banner.open = False
        self.page.update()

    def open_dlg_modal(self, *args):
        self.page.dialog = self.press_dlg
        self.press_dlg.open = True
        self.page.update()

    def close_dlg(self, *args):
        global reading
        reading = False
        self.press_dlg.open = False
        self.page.update()

    def add_clicked(self, e):
        if self.key_presed.value == "Set bind":
            self.show_banner()
        else:
            self.close_banner()
            task = Task(self.key_presed.value, self.new_description.value,
                        self.task_delete, self.on_keyboard, self.setter)
            self.tasks.controls.append(task)
            self.new_description.value = ""
            self.key_presed.value = "Set bind"
            self.page.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.page.update()
    
    def on_start(self):
        items = self.setter.get_binds()

        if items:
            for i in items:
                Task.current_id = i['id']
                task = Task(i['key'], i['description'],
                            self.task_delete, self.on_keyboard, self.setter)
                self.tasks.controls.append(task)
                self.page.update()

reading = False

def example(page, on_keyboard, setter):
    zxc = TodoApp(page, on_keyboard, setter).build()

    return zxc
