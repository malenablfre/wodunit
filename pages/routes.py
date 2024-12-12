from flet import *
from views.home_view import home
from views.login_view import login


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