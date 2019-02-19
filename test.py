import unittest
from typing import Iterator

from pypom import Page
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from core_utils import get_driver, has_long_word


class MainPage(Page):

    _TEXT = (By.CSS_SELECTOR, '[id=content] div.row div.large-10')
    _PUNISHER = (By.CSS_SELECTOR, 'img[src="/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg"]')

    def get_all_dynamic_text(self) -> Iterator[str]:
        ele = self.find_elements(*self._TEXT)
        array = []
        for i in ele:
            array.append(i.text)
        return array

    def punisher_exist(self)->bool:
        try:
            ele = self.find_element(*self._PUNISHER)
            return ele.is_displayed()
        except NoSuchElementException:
            return False


class PunisherTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def test_if_word_greater_than_10(self):
        main_page = MainPage(self.driver, "https://the-internet.herokuapp.com/dynamic_content").open()
        array = main_page.get_all_dynamic_text()
        result = " ".join(array)
        answer = has_long_word(result)
        self.assertEqual(answer, True, "We dont have any word more than 10 characters")

    def test_if_avatar_exist_or_not(self):
        main_page = MainPage(self.driver, "https://the-internet.herokuapp.com/dynamic_content").open()
        ans = main_page.punisher_exist()
        self.assertEqual(ans, False, "Punisher found on the page")

    def tearDown(self):
        self.driver.close()


