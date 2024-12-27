from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import re

class ArticleScraper:
    def __init__(self, url):
       self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
       self.driver.get(url)
       
       self.title = ''
       self.all_text = ''
       
       
    def get_title(self):   
       title_scrape = self.driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd').text
       for k in title_scrape.split('\n'): 
           # needed to remove special characters from title while preserving spaces so that it can create the field
           self.title = " ".join(re.findall(r"[a-zA-Z0-9]+", k))
    def get_textbody(self):
       article_text = []
       article = self.driver.find_elements(By.TAG_NAME, 'p')
       header = self.driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd')

       article_text.append(header.text)
       for text in article:
           article_text.append(text.text)
           
       self.all_text = '\n'.join(article_text)