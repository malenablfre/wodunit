import flet as ft
from pages.home import home
from pages.login import login
from pages.signup import signup
from pages.gameslots import gameslots
from pages.uebersicht import uebersicht 
from pages.rollenuebersicht import rollenuebersicht
from pages.spielregeln import spielregeln
from pages.gamemenu import gamemenu
from pages.emergencycalled import emergencycalled
from pages.emergencyblocked import emergencyblocked


def views_handler(page):
    return {
        '/':ft.View(
            route='/',
            controls=[
                home(page) #neuer name: "startseite"
            ]
        ),
        '/login':ft.View(
            route='/login',
            controls=[
                login(page)
            ]
        ),
        '/signup':ft.View(
            route='/signup',
            controls=[
                signup(page)
            ]
        ),
        '/gameslots':ft.View(
            route='/gameslots',
            controls=[
                gameslots(page)
            ]
        ),
        '/uebersicht':ft.View(
            route='/uebersicht',
            controls=[
                uebersicht(page)
            ]
        ), 
        '/rollenuebersicht':ft.View(
            route='/rollenuebersicht',
            controls=[
                rollenuebersicht(page)
            ]
        ), 
        '/spielregeln':ft.View(
            route='/spielregeln',
            controls=[
                spielregeln(page)
            ]
        ),
        '/gamemenu':ft.View(
            route='/gamemenu',
            controls=[
                gamemenu(page) #neuer name: "home"
            ]
        ),
        '/emergencycalled':ft.View(
            route='/emergencycalled',
            controls=[
                emergencycalled(page)
            ]
        ),
        '/emergencyblocked':ft.View(
            route='/emergencyblocked',
            controls=[
                emergencyblocked(page)
            ]
        )
    }