import flet as ft

class statistik(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Stack([


            ft.Container(
                # ---- background ----
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
                controls=[
                        # --- space --- 
                    ft.Container(height=50),
                    ft.Container( 
                        # --- scroll funktion ---   
                        ft.Column(
                            spacing=0,
                            scroll=ft.ScrollMode.HIDDEN,
                            controls=[
                                ft.Container(),
                                ft.Container(
                                    content=ft.Text(
                                        value="Chronik der Gefallenen", 
                                        size= 25, 
                                        font_family= "Times New Roman", 
                                        weight= "bold", 
                                        color="#C72C42"
                                    ),
                                    margin=40 
                                ),

                                # --- liste --- 
                                ft.DataTable(
                                    # ---- liste einstellungen ----
                                    width=300,
                                    border=ft.border.all(2, "#C72C41"),
                                    border_radius=10,
                                    vertical_lines=ft.BorderSide(3, "#C72C41"),
                                    horizontal_lines=ft.BorderSide(1, "#C72C41"),
                                    sort_column_index=0, 
                                    heading_row_height=50,
                                    heading_text_style=ft.TextStyle(
                                        font_family="Times New Roman", 
                                        color='#FFFFFF', 
                                        size=15
                                    ),
                                    data_text_style=ft.TextStyle(
                                        font_family= "Times New Roman",
                                        color='#C72C41', 
                                        size=15
                                    ),
                                    
                                    column_spacing=20,
                                    columns=[
                                        # ---- head row liste ----
                                        ft.DataColumn(ft.Text("Name")),
                                        ft.DataColumn(ft.Text("Rolle")),
                                        ft.DataColumn(ft.Text("Ort")),
                                    ],
                                    rows=[
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Marie")),
                                                ft.DataCell(ft.Text("")),
                                                ft.DataCell(ft.Text("")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("Jack")),
                                                ft.DataCell(ft.Text("")),
                                                ft.DataCell(ft.Text(""))                               
                                            ],
                                        ),
                                            
                                    ],
                                        
                                ),
                            ],

                            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                            ),
                        height=600, 
                    ),
                ]
            ), 

             # ------ HEADER ------
            ft.Container(
                content=
                    ft.Row(
                        controls=[
                                ft.Container(
                                    # ---- ARROW BACK ---- 
                                    content=ft.IconButton(
                                        ft.Icons.ARROW_BACK,
                                        icon_color="#EE4540",
                                        hover_color= ft.Colors.with_opacity(0.1, "#C72C42"),
                                        highlight_color= ft.Colors.with_opacity(0.5, "#C72C42"),
                                        on_click=lambda _: self.page.go("/"),  
                                    ),
                                ),
    
                                ft.Container(
                                    content=ft.Text(
                                        value="Voting",
                                        size= 30,
                                        font_family= "Times New Roman",
                                        weight= "bold",
                                        color="#EE4540"
                                    ),
                                ),
    
                                # ------ SIDE MENU ------
                                ft.Container(
                                    content=ft.PopupMenuButton(
                                        icon=ft.Icons.MENU_SHARP,
                                        icon_color="#EE4540",
                                        bgcolor="#C72C42",
                                        items=[
                                            ft.PopupMenuItem(text="Home", on_click=lambda _: self.page.go("/")),
                                            ft.PopupMenuItem(text="Rollenübersicht", on_click=lambda _: self.page.go("/")),
                                            ft.PopupMenuItem(text="Spielregeln", on_click=lambda _: self.page.go("/"))
                                        ]
                                    ),
                                )
                        ],
                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                margin=10
            )
            
                
        ])
        
        return page