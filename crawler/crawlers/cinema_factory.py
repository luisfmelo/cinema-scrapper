from crawlers import CinemasNos

CINEMAS = {
    'cinemas-nos': CinemasNos()
}


def cinema_factory(cinema):
    return CINEMAS.get(cinema)
