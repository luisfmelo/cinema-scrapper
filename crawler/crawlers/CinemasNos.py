import logging
from time import sleep

from crawlers import Crawler
from data.Cinema import Cinema
from data.Movie import Movie
from data.Session import Session
from services.slack_service import notify_slack_message


logger = logging.getLogger(__name__)


class CinemasNos(Crawler.Crawler):
    def scrap_sessions(self):
        movies = self.browser.find_element_by_class_name('items__container').find_elements_by_tag_name('article')

        movie_urls = [movie.find_element_by_class_name('item-image').get_attribute('href') for movie in movies]
        for url in movie_urls:
            self._scrap_sessions_of_a_movie(url)

        return True

    def _scrap_sessions_of_a_movie(self, url: str):
        try:
            bs = self.get_single_page(url)
        except Exception as e:
            logger.error(str(e))
            return []

        try:
            # Get Movie Info
            movie = self._get_movie_info_from_page()

            # Get sessions for each day (in selector)
            # TODO - BAD approach
            self.browser.find_element_by_class_name('day--select').click()
            n = len(self.browser.find_elements_by_class_name('dropdown-list')[1].find_elements_by_tag_name('li'))
            for i in range(n):
                elem = self.browser.find_elements_by_class_name('dropdown-list')[1].find_elements_by_tag_name('li')[i]
                try:
                    elem.click()
                except Exception as e:
                    sleep(2)
                    elem.click()

                # GET SESSIONS
                sessions_date = elem.text
                articles = self.browser.find_element_by_css_selector('section[data-id="normal {}"]'.format(sessions_date))

                for article in articles.find_elements_by_tag_name('article'):
                    cinema = Cinema(
                        name=self.trim(article.find_element_by_class_name('cinema').text),
                        city=None,
                        company=self.__class__.__name__
                    )

                    room = self.trim(article.find_element_by_class_name('room').text)

                    for hour in article.find_element_by_class_name('hours').find_elements_by_tag_name('a'):
                        session = Session(
                            movie=movie,
                            cinema=cinema,
                            room=room,
                            date=sessions_date,
                            hour=self.trim(hour.text),
                        )

                        CinemasNos.publish_new_session(session)

                self.browser.find_element_by_class_name('day--select').click()

        except Exception as e:
            logger.warn(str(e))
            import traceback
            notify_slack_message(str(traceback.format_exc()))
            notify_slack_message('CONTINUING')

        return True

    def _get_movie_info_from_page(self) -> Movie:
        info = self.browser.find_element_by_class_name('info')
        description = self.browser.find_element_by_class_name('description')

        # Movie title
        movie_title = info.find_element_by_tag_name('h1').text
        logger.info(movie_title)

        # Age Rating
        movie_age_rating = info.find_element_by_tag_name('h2').text

        # Original Title, Year, Duration, Country
        movie_original_title = ''
        movie_year = ''
        movie_duration = ''
        movie_genre = ''
        movie_country = ''
        movie_format = None
        movie_version = None
        for p in description.find_elements_by_tag_name('p'):
            split = p.text.split(':')
            placeholder = split[0]
            value = split[1]

            if placeholder == 'Título Original':
                movie_original_title = value
            elif placeholder == 'Ano':
                movie_year = value
            elif placeholder == 'Duração (minutos)':
                movie_duration = value
            elif placeholder == 'Género':
                movie_genre = value
            elif placeholder == 'País':
                movie_country = value
            elif placeholder == 'Formato':
                movie_format = value
            elif placeholder == 'Versão':
                movie_version = value
            elif placeholder in ['Data de estreia', 'Realizador', 'Actores', 'Distribuidora']:
                continue
            else:
                notify_slack_message(self.__class__.__name__ + ': New parameter found: ' + placeholder)

        # Synopsis
        movie_synopsis = self.browser.find_element_by_class_name('sinopse').find_elements_by_tag_name('div')[1].text

        # Trailer URL
        trailer = self.browser.find_elements_by_css_selector('a[class*="trailerButton"]')
        movie_trailer_url = trailer[0].get_attribute('href') if len(trailer) else None

        movie = Movie(
            title=movie_title.strip() if movie_title is not None else None,
            original_title=movie_original_title.strip() if movie_original_title is not None else None,
            year=movie_year,
            age_rating=movie_age_rating.strip() if movie_age_rating is not None else None,
            duration=movie_duration,
            genre=movie_genre.strip() if movie_genre is not None else None,
            country=movie_country.strip() if movie_country is not None else None,
            format=movie_format.strip() if movie_format is not None else None,
            version=movie_version.strip() if movie_version is not None else None,
            synopsis=movie_synopsis.strip() if movie_synopsis is not None else None,
            trailer_url=movie_trailer_url.strip() if movie_trailer_url is not None else None,
            imdb_url=None,
            rating=None,
        )

        return movie
