import flet as ft
from pages.home import home
from pages.login import login
from pages.myrole import role
from pages.i_died import dead


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
        '/role':ft.View(
            route='/role',
            controls=[
                role(page)
            ]
        ),
        '/dead':ft.View(
            route='/dead',
            controls=[
                dead(page)
            ]
        ),
    }