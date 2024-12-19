import flet as ft
from pages.home import home
from pages.login import login
from pages.neuesspiel import neuesspiel
from pages.spieleinstellungen import spieleinstellungen
from pages.erstelltesspiel import erstelltesspiel
from pages.aktivesspiel import aktivesspiel


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
        '/neuesspiel':ft.View(
            route='/neuesspiel',
            controls=[
                neuesspiel(page)
            ]
        ),
        '/spieleinstellungen':ft.View(
            route='/spieleinstellungen',
            controls=[
                spieleinstellungen(page)
            ]
        ),
        '/erstelltesspiel':ft.View(
            route='/erstelltesspiel',
            controls=[
                erstelltesspiel(page)
            ]
        ),
        '/aktivesspiel':ft.View(
            route='/aktivesspiel',
            controls=[
                aktivesspiel(page)
            ]
        ),
    }