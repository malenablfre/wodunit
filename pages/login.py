import flet as ft

class login(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.expand = True
        self.text_username: ft.TextField = ft.TextField(label='Benutzername',
            label_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_align=ft.TextAlign.LEFT,
            width=200,
            border_color="#510A32",
            border_radius=10,
            cursor_color="#EE4540"
            )
        self.text_password: ft.TextField = ft.TextField(label='Passwort',
            label_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_align=ft.TextAlign.LEFT,
            width=200,
            border_color="#510A32",
            border_radius=10,
            cursor_color="#EE4540",
            password=True,
            )
        self.button_submit: ft.ElevatedButton = ft.ElevatedButton(text='Anmelden',
           style=ft.ButtonStyle(
               color="#EE4540",
               bgcolor="#510A32",
               text_style=ft.TextStyle(
                   font_family= "Times New Roman",
                 color="#EE4540"
               ),
               overlay_color="#801336",
           ),
           width=200,
           disabled=True
           )
        
        self.text_username.on_change = self.validate
        self.text_password.on_change = self.validate
        self.button_submit.on_click = self.submit


    def validate(self, e: ft.ControlEvent) -> None:
        special_characters = set("/!@#$%^&*(),.?\":|<>")
        password = self.text_password.value
        # validate if username exists and password is long enough
        if all([
            self.text_username.value and
            password and
            len(password) >= 7 and
            any(char in special_characters for char in password)
            ]):
            self.button_submit.disabled = False
        else:
            self.button_submit.disabled = True
        # output error messages for password
        if len(password) < 7 and len(password) != 0:
            self.text_password.error_text = "Passwort zu kurz"
        elif not any(char in special_characters for char in password) and len(password) != 0:
            self.text_password.error_text = "Min. ein Sonderzeichen"
        else:
            self.text_password.error_text = ""
        self.update()

    def submit(self, e: ft.ControlEvent) -> None:
        print("Username:", self.text_username.value)
        print("Password:", self.text_password.value)
        self.page.go("/")


    def build(self):
        page = ft.Stack([
            # ------ BACKGROUND ------
            ft.Container(
                width=self.page.width,
                height=self.page.height,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#2D142C","#510A32"]),
                border_radius=10,
                alignment=ft.alignment.center
            ),

            # ------ CONTENT ------
            ft.Container(   
                ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            content=ft.Text(value="Whodunit?", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        ),

                        ft.Container(
                            content=ft.Text(value="Login", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        ),

                        ft.Container(
                            ft.Column(
                                controls=[
                                    self.text_username,
                                    self.text_password,
                                    self.button_submit
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER
                            ),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center
                        )
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                )     
            ),

            # ------ ARROW BACK ------
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),
                        ),
                    ],
                    alignment = ft.MainAxisAlignment.START,
                ),
                margin=10
            )
        ])

        return page