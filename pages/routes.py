import flet as ft
from pages.home import home
from pages.login import login
from pages.statistik import statistik


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

        '/statistik':ft.View(
            route='/statistik',
            controls=[
            statistik(page)
            ]
        )  
    }