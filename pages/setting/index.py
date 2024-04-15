# import flet as ft
# import threading

# name = "setting"

# def example(page, on_keyboard, setter):
#     def on_presed():
#         global reading
#         on_keyboard.keykap_changed()
#         previous = on_keyboard.keykap
#         while reading:
#             if previous != on_keyboard.keykap:
#                 key_presed.value = f"Seted {on_keyboard.keykap.key}"
#                 close_dlg(1)
#                 break
#             previous = on_keyboard.keykap
#         page.update()

#     def open_dlg_modal(e):
#         page.dialog = press_dlg
#         press_dlg.open = True
#         page.update()
    
#     def close_dlg(e):
#         global reading
#         reading = False
#         press_dlg.open = False
#         page.update()

#     def open_error_dlg_modal():
#         page.dialog = error_dlg
#         error_dlg.open = True
#         page.update()
    
#     def close_error_dlg(e):
#         error_dlg.open = False
#         page.update()

#     def start_reading():
#         global reading
#         reading = True
#         t = threading.Thread(target=on_presed)
#         t.start()
#         t.join()
    
#     def add_bind(e):
#         keys = key_presed.value.split()
#         keys.pop(0)
#         keys = ' '.join(keys)

#         bi = Bind(keys, tf.value, setter)
        
#         if bi.key != "bind":
#             setter.write("bind", bi.ID, bi.key, bi.description)

#             defoult_view = ft.Row(
#                 controls=[
#                     ft.Text(keys),
#                     ft.Text(tf.value),
#                     bi.delete
#                         ]
#                     )

#             edit_view = ft.Row(
#                 controls=[
#                     ft.Text("SSSSSSSSSSSSSSS"),
#                         ]
#                     )

#             edit_view.visible = False

#             added_bind.controls.append(
#             ft.Column(
#             controls=[
#                 defoult_view,
#                 edit_view
#                 ]
#             ))
#         else:
#             open_error_dlg_modal()
#         tf.value = "there is no description"
#         key_presed.value = "Set bind"
#         view.update()

#     key_presed = ft.Text("Set bind")
#     tf = ft.TextField(label="Description", value="there is no description")
#     added_bind = ft.Column(alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
#     press_dlg = ft.AlertDialog(
#         title=ft.Text("Please press the key"),
#         actions=[
#             ft.TextButton("Cancel", on_click=lambda e: close_dlg(e)),
#         ],
#         actions_alignment=ft.MainAxisAlignment.END,
#         on_dismiss=lambda e: close_dlg(e),
#     )

#     error_dlg = ft.AlertDialog(
#         title=ft.Text("No key is assigned"),
#         actions=[
#             ft.TextButton("OK", on_click=close_error_dlg),
#         ],
#         actions_alignment=ft.MainAxisAlignment.END,
#         on_dismiss=close_error_dlg,
#     )


#     view = ft.Column(controls=[
#             ft.Row(controls=[
#                 ft.Row(controls=[
#                     ft.IconButton(
#                         icon=ft.icons.KEYBOARD,
#                         tooltip="Set bind",
#                         on_click=lambda e: (open_dlg_modal(e), start_reading())
#                     ),
#                     key_presed
#                     ]
#                 ),
#                 tf,
#                 ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_bind),
#                 ]
#             ),
#             added_bind
#             ]
#         )

#     return view

# class Bind:
#     current_id = 0
#     instances = []

#     def __init__(self, key, description, setter):
#         self.ID = Bind.current_id
#         Bind.current_id += 1
#         self.setter = setter

#         self.key = key
#         self.description = description
#         self.delete = ft.TextButton(self.ID, on_click=self.delete)

#         Bind.instances.append(self)
    
#     def delete(self, e):
#         self.setter.delete(self.ID)
import flet as ft

class Task(ft.UserControl):
    current_id = 0
    def __init__(self, key, description, task_delete):
        super().__init__()
        self.ID = Task.current_id
        Task.current_id += 1
        self.key = key
        self.description = description
        self.task_delete = task_delete
        print(self.ID, self.key, self.description, self.task_delete)

    def build(self):
        self.display_key = ft.Container(
            ft.Text(self.key),
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
        self.edit_key = ft.Row(controls=[
                    ft.IconButton(
                        icon=ft.icons.KEYBOARD,
                        tooltip="Set bind",
                        on_click=lambda e: print("zxc")
                    )
        ])
        self.edit_description = ft.TextField(expand=1)

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
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
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
                self.edit_description,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_description.value = self.display_description.content.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_description.content.value = self.edit_description.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)


class TodoApp(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.new_key = ft.Row(controls=[
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD,
                            tooltip="Set bind",
                            on_click=lambda e: print("zxc")
                        )
        ])
        self.new_description = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = ft.Column()

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

    def add_clicked(self, e):
        task = Task("zxc", self.new_description.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_description.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

zxc = TodoApp()

def example(page, on_keyboard, setter):
    return zxc.build()
