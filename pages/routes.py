import flet as ft
from pages.home import home
from pages.login import login
from pages.gameslots import gameslots
from pages.gamemenu import gamemenu


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
        '/gameslots':ft.View(
            route='/gameslots',
            controls=[
                gameslots(page)
            ]
        ),
        '/gamemenu':ft.View(
            route='/gamemenu',
            controls=[
                gamemenu(page)
            ]
        )
    }