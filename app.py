from flet import *
from views.routes import views_handler

def main(page: Page):
    page.title = "Home"
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    #page.bgcolor = "#2D142C"
    
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
        page.update()


    page.on_route_change = route_change
    page.go('/')

app(target=main)