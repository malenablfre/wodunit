import flet as ft
from pages.home import home
from pages.login import login
from pages.Uebersicht import Uebersicht 

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
        '/Uebersicht':ft.View(
            route='/Uebersicht',
            controls=[
                Uebersicht(page)
            ]
        )
    }