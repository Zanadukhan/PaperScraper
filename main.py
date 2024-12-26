from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from gtts import gTTS
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import re

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

article_link = input('Paste which article you want to scrape from: ')
article_text = []
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get(article_link)

title_scrape = driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd').text
# needed to remove special characters from title while preserving spaces so that it can create the fiel
for k in title_scrape.split('\n'):
    title = " ".join(re.findall(r"[a-zA-Z0-9]+", k))


article = driver.find_elements(By.CLASS_NAME, 'paywall')
header = driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd')

article_text.append(header.text)
for text in article:
    article_text.append(text.text)

all_text = '\n'.join(article_text)

tts = gTTS(all_text)
tts.save(f'{title}.mp3')
print('done converting!')

file_path = fr'C:\Users\carson\PycharmProjects\NewYorkerTTS\{title}.mp3'
# file1 = drive.CreateFile()
# file1.SetContentFile()
# file1.Upload()

folderName = 'articles'  # Please set the folder name.

folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
for folder in folders:
    if folder['title'] == folderName:
        file2 = drive.CreateFile(metadata={"title": f"{title}", 'parents': [{'id': folder['id']}]})
        file2.SetContentFile(file_path)
        file2.Upload()

