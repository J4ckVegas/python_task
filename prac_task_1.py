"""
Открыть страницу http://google.com/ncr
Выполнить поиск слова “selenide”
Проверить, что первый результат – ссылка на сайт selenide.org.
Перейти в раздел поиска изображений
Проверить, что первое изображение неким образом связано с сайтом selenide.org.
Вернуться в раздел поиска Все
Проверить, что первый результат такой же, как и на шаге 3.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):
    def setUp(self) -> None:
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.maximize_window()

    def test_search(self):
        # Открыть страницу http://google.com/ncr
        self.drv.get('https://www.google.com/ncr')
        assert 'Google' in self.drv.title

        # Выполнить поиск слова “selenide”
        search_field = self.drv.find_element_by_name('q')
        search_field.send_keys('selenide')
        search_field.send_keys(Keys.RETURN)
        assert 'No Results found' not in self.drv.page_source

        # Проверить, что первый результат – ссылка на сайт selenide.org.
        first_link = self.drv.find_element_by_xpath(xpath='(//*[@class="TbwUpd NJjxre"]/cite)[1]')
        first_url = first_link.text
        assert 'selenide.org' == first_url

        # Перейти в раздел поиска изображений
        pic_search = self.drv.find_element_by_xpath(xpath='//*[text()="Images"]')
        pic_search.click()

        # Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        first_pic_link = self.drv.find_element_by_xpath(
            xpath='//div[1]/a/div[@class="bRMDJf islir"]/img/ancestor::div[2]/a/div[@class="fxgdke"]')
        first_pic_url = first_pic_link.text
        assert 'selenide.org' in first_pic_url

        # Вернуться в раздел поиска Все
        self.drv.find_element_by_xpath(xpath='//*[text()="Все"]').click()

        # Проверить, что первый результат такой же, как и на шаге 3.
        assert first_url in first_pic_url

    def tearDown(self) -> None:
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
