import flet as ft

class Rollenuebersicht(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Stack([
            ft.Container(
                width=400,
                height=700,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#2D142C","#510A32"]),
                border_radius=10,
                alignment=ft.alignment.center
                ),
                
                ft.Column(
                    spacing=0,
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                    ft.Container(
                        content=ft.Text(value="Unschuldiger", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=7,
                    ),

                    ft.Container(
                        content=ft.Text(value="Der Unschuldige ist ein normaler Teilnehmer ohne besondere Fähigkeiten. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                        margin=9,
                    ),

                    ft.Container(
                        content=ft.Text(value="Mörder", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Der Mörder kann jede andere Rolle im Spiel töten. Ziel ist es dabei unerkannt zu bleiben ", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,  
                    ),
                ],
                    alignment = ft.MainAxisAlignment.CENTER,
                ),
                
            ft.Column(
                controls=[
                    ft.Container(),
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/Uebersicht")),),
                            ft.Container(content=ft.Text(value="Rolleübersicht", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
                            ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/Uebersicht")),),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            )
        ])

        return page