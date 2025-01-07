import flet as ft
from pages.home import home
from pages.login import login
from pages.voting_room import voting_room
from pages.voting_result import voting_result


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
        '/vote':ft.View(
            route='/vote',
            controls=[
                voting_room(page)
            ]
        ),
        '/vote_result':ft.View(
            route='/vote_result',
            controls=[
                voting_result(page)
            ]
        ),
    }