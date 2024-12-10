from flet import *
from home_view import home
from login_view import login


def views_handler(page):
    return {
        '/':View(
            route='/',
            controls=[
                home(page)
            ]
        ),
        '/login':View(
            route='/login',
            controls=[
                login(page)
            ]
        )
    }