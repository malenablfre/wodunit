import flet as ft
from pages.home import home
from pages.login import login
from pages.Emergency import Emergency
from pages.Emergency2 import Emergency2


def views_handler(page):
    return {
        '/':ft.View(
            route='/',
            controls=[
                home(page)
            ]
        ),
        '/Emergency2':ft.View(
            route='/Emergency2',
            controls=[
                Emergency2(page)
            ]
        ),
        '/Emergency':ft.View(
            route='/Emergency',
            controls=[
                Emergency(page)
            ]
        )
    }