
import pytest
from selenium.common.exceptions import NoSuchElementException
from article_scraper import ArticleScraper

def test_get_domain_newyorker():
    url = "https://www.newyorker.com/magazine/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    scraper.driver.quit()
    assert scraper.org == 'newyorker'

def test_get_domain_foreignpolicy():
    url = "https://foreignpolicy.com/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    scraper.driver.quit()
    assert scraper.org == 'foreignpolicy'

def test_get_title_newyorker(mocker):
    url = "https://www.newyorker.com/magazine/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'find_element', return_value=mocker.Mock(text="Test Title"))
    scraper.get_title()
    scraper.driver.quit()
    assert scraper.title == "Test Title"

def test_get_title_foreignpolicy(mocker):
    url = "https://foreignpolicy.com/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'find_element', return_value=mocker.Mock(text="Test Title"))
    scraper.get_title()
    scraper.driver.quit()
    assert scraper.title == "Test Title"

def test_get_title_no_element(mocker):
    url = "https://www.newyorker.com/magazine/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'find_element', side_effect=NoSuchElementException)
    with pytest.raises(NoSuchElementException):
        scraper.get_title()
    scraper.driver.quit()

def test_get_textbody_newyorker(mocker):
    url = "https://www.newyorker.com/magazine/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'find_elements', return_value=[mocker.Mock(text="Paragraph 1"), mocker.Mock(text="Paragraph 2")])
    scraper.get_textbody()
    assert scraper.all_text == "Paragraph 1\nParagraph 2"

def test_get_textbody_foreignpolicy(mocker):
    url = "https://foreignpolicy.com/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'find_elements', return_value=[mocker.Mock(text="Paragraph 1"), mocker.Mock(text="Paragraph 2")])
    scraper.get_textbody()
    assert scraper.all_text == "Paragraph 1\nParagraph 2"

def test_get_textbody_no_elements(mocker):
    url = "https://www.newyorker.com/magazine/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'find_elements', return_value=[])
    scraper.get_textbody()
    assert scraper.all_text == ""

def test_invalid_url():
    with pytest.raises(Exception):
        ArticleScraper("invalid_url")

def test_quit_driver(mocker):
    url = "https://www.newyorker.com/magazine/2021/09/20/some-article"
    scraper = ArticleScraper(url)
    mocker.patch.object(scraper.driver, 'quit')
    scraper.get_textbody()
    scraper.driver.quit.assert_called_once()