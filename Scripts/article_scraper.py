from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import re
import time

class ArticleScraper:
    """
    ArticleScraper is a class designed to scrape article titles and text bodies from specified web pages.
        driver (WebDriver): The Selenium WebDriver instance used to interact with the webpage.
        title (str): The cleaned title of the article.
        all_text (str): The complete text body of the article.
        org (str): The organization identifier to determine which CSS selector to use.
    Methods:
        __init__(url):
            Initializes the ArticleScraper with the given URL, sets up the Selenium WebDriver, and determines the organization.
        get_title():
            Uses Selenium to scrape the title of an article from a webpage.
            Supports different CSS selectors for different organizations (e.g., 'newyorker' and 'foreignpolicy').
            Cleans the title to remove special characters while preserving spaces.
        get_textbody():
            Scrapes the text content of an article from a web page using Selenium WebDriver.
            Handles different organizations ('newyorker' and 'foreignpolicy') by applying specific scraping logic for each.
            Collects all paragraph elements and appends their text to the article text list.
            Includes the article title at the beginning of the text for 'newyorker'.
            Excludes specific paragraph elements (cookie message, myFP, related articles) from the text for 'foreignpolicy'.
            Joins the collected text into a single string with newline characters and stores it in the `self.all_text` attribute.
            Closes the WebDriver instance.
    """

    def __init__(self, url:str):
        options = FirefoxOptions()
        # headless causing issues with browsing context discard
        # options.add_argument("-headless")
        # needed to disable javascript to prevent paywalls from hiding elements on the page
        options.set_preference('javascript.enabled', False)
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
        
        match self.org:
            case 'foreignpolicy':
                title_scrape = self.driver.find_element(By.CSS_SELECTOR, 'h1.hed').text
            case 'newyorker':
                title_scrape = self.driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd').text   
                
        for k in title_scrape.split('\n'): 
            # needed to remove special characters from title while preserving spaces so that it can create the field
            self.title = " ".join(re.findall(r"[a-zA-Z0-9]+", k))
           
    def get_textbody(self):
        """
        Extracts the text body of an article from a web page based on the organization.
        This method scrapes the text content of an article from a web page using Selenium WebDriver.
        It handles different organizations ('newyorker' and 'foreignpolicy') by applying specific
        scraping logic for each.
        For 'newyorker':
        - Collects all paragraph elements and appends their text to the article text list.
        - Includes the article title at the beginning of the text.
        For 'foreignpolicy':
        - Excludes specific paragraph elements (cookie message, myFP, related articles) from the text.
        - Collects all other paragraph elements and appends their text to the article text list.
        The collected text is then joined into a single string and stored in the `all_text` attribute.
        The WebDriver instance is quit after the text extraction is complete.
        Attributes:
            all_text (str): The concatenated text of the article.
        """
        article_text = []

        match self.org:
            case 'newyorker':
                article = self.driver.find_elements(By.TAG_NAME, 'p')
                article_text.append(self.title)
                for p in article:
                    article_text.append(p.text)
                
            case 'foreignpolicy':
            
                # Exclude these p elements
                cookie_message = self.driver.find_element(By.CSS_SELECTOR, '.cookie_message')
                myFP = self.driver.find_element(By.CSS_SELECTOR, '.js-myfp-message')
                
                try:
                    related_articles = self.driver.find_element(By.CSS_SELECTOR, '.related-articles')
                    self.driver.execute_script("arguments[0].style.display = 'none';", related_articles)
                except NoSuchElementException:
                    pass
                
                self.driver.execute_script("arguments[0].style.display = 'none';", cookie_message)
                self.driver.execute_script("arguments[0].style.display = 'none';", myFP)
                
                
                
                article = self.driver.find_elements(By.TAG_NAME, 'p')
                # article_text.append(self.title)
                for p in article:
                    if p.text == '':
                        continue
                    article_text.append(p.text)
                
        self.all_text = '\n'.join(article_text)
        self.driver.quit()