from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import re

class ArticleScraper:
    """
    A class used to scrape articles from a given URL using Selenium WebDriver.
    Attributes
    ----------
    driver : WebDriver
        The Selenium WebDriver instance used to interact with the web page.
    title : str
        The title of the article.
    all_text : str
        The full text of the article, including the header and all paragraphs.
    Methods
    -------
    get_title():
        Scrapes the title of the article and removes special characters.
    get_textbody():
        Scrapes the full text of the article, including the header and all paragraphs.
    """

    def __init__(self, url):
        options = FirefoxOptions()
        # options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        self.driver.get(url)
       
       
        self.title = ''
        self.all_text = ''
        
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split('.')
    
    # Handle cases with or without 'www'
        if domain_parts[0] == 'www':
            domain = domain_parts[1]
        else:
            domain = domain_parts[0]
        
        print(domain)
        self.org = domain
       
       
    def get_title(self):
        """
        Extracts and processes the title of an article based on the organization.

        This method uses Selenium to scrape the title of an article from a webpage.
        It supports different CSS selectors for different organizations (e.g., 'newyorker' and 'foreignpolicy').
        The title is then cleaned to remove special characters while preserving spaces.

        Attributes:
            self.org (str): The organization identifier to determine which CSS selector to use.
            self.driver (WebDriver): The Selenium WebDriver instance used to interact with the webpage.
            self.title (str): The cleaned title of the article.

        Raises:
            NoSuchElementException: If the specified CSS selector does not match any elements on the page.
        """
        title_scrape = ''
        if self.org == 'foreignpolicy':
            title_scrape = self.driver.find_element(By.CSS_SELECTOR, 'h1.hed').text
        elif self.org == 'newyorker':
            title_scrape = self.driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd').text   
        for k in title_scrape.split('\n'): 
            # needed to remove special characters from title while preserving spaces so that it can create the field
            self.title = " ".join(re.findall(r"[a-zA-Z0-9]+", k))
           
    def get_textbody(self):
        """
        Extracts the text body of an article from a web page.
        This method retrieves the text content of an article based on the organization
        specified in the `self.org` attribute. It supports extracting text from articles
        on 'newyorker' and 'foreignpolicy' websites.
        For 'newyorker', it finds all paragraph elements and appends their text content
        to the `article_text` list, including the article title. For 'foreignpolicy', it
        finds the first paragraph element and appends its text content to the `article_text`
        list, including the article title.
        The extracted text is then joined into a single string with newline characters
        and stored in the `self.all_text` attribute.
        Returns:
            None
        """
        article_text = []
       
        if self.org == 'newyorker':
            article = self.driver.find_elements(By.TAG_NAME, 'p')
            article_text.append(self.title)
            for p in article:
                article_text.append(p.text)
            
            self.all_text = '\n'.join(article_text)
        elif self.org == 'foreignpolicy':
            article = self.driver.find_elements(By.TAG_NAME, 'p')
            article_text.append(self.title)
            for p in article:
                article_text.append(p.text)