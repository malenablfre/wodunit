import flet as ft
from pages.home import home
from pages.login import login
from pages.Emergency import Emergency


def views_handler(page):
    return {
        '/':ft.View(
            route='/',
            controls=[
                home(page)
            ]
        ),
        '/login':ft.View(
            route='/login',
            controls=[
                login(page)
            ]
        ),
        '/Emergency':ft.View(
            route='/Emergency',
            controls=[
                Emergency(page)
            ]
        )
    }