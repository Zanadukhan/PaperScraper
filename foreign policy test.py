from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from gtts import gTTS
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


article_link = input('Paste which article you want to scrape from: ')
article_text = []
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get(article_link)

title = driver.find_element(By.CSS_SELECTOR, 'h1.hed').text
article = driver.find_element(By.CSS_SELECTOR, '.content-gated--main-article')


tts = gTTS(article.text)
tts.save(f'{title}.mp3')
print('done converting!')

file_path = fr'C:\Users\carson\PycharmProjects\NewYorkerTTS\{title}.mp3'

folderName = 'articles'  # Please set the folder name.

folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
for folder in folders:
    if folder['title'] == folderName:
        file2 = drive.CreateFile(metadata={"title": f"{title}txt", 'parents': [{'id': folder['id']}]})
        file2.SetContentFile(file_path)
        file2.Upload()