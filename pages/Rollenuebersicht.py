import flet as ft

class Rollenuebersicht(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Container(
                ft.Column(
                spacing=0,
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.Container(
                        content=ft.Text(value="Rollenübersicht", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=5,
                        padding=5,
                    ),

                    ft.Container(
                        content=ft.Text(value="Unschuldiger", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=7,
                        padding=7,
                    ),

                    ft.Container(
                        content=ft.Text(value="Der Unschuldige ist ein normaler Teilnehmer ohne besondere Fähigkeiten. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                        margin=9,
                        padding=9,

                    ),

                    ft.Container(
                        content=ft.Text(value="Mörder", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        
                    ),

                    ft.Container(
                        content=ft.Text(value="Der Mörder kann jede andere Rolle im Spiel töten. Ziel ist es dabei unerkannt zu bleiben ", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                        padding=10,
                        
                    ),
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
            )
        return page