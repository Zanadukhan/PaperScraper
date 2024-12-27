from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from yapper import PiperSpeaker, PiperVoiceUS
import re
import os
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

article_text = []
current_dir = os.getcwd()

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

article_link = input('Paste which article you want to scrape from: ')
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get(article_link)

title_scrape = driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd').text
# needed to remove special characters from title while preserving spaces so that it can create the fiel
for k in title_scrape.split('\n'):
    title = " ".join(re.findall(r"[a-zA-Z0-9]+", k))


article = driver.find_elements(By.TAG_NAME, 'p')
header = driver.find_element(By.CSS_SELECTOR, 'h1.BaseWrap-sc-gjQpdd')

article_text.append(header.text)
for text in article:
    article_text.append(text.text)

all_text = '\n'.join(article_text)

def generate_audio(text, title):
    tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2').to(device)
    tts.tts_to_file(
    text = text,
    speaker="Claribel Dervla",
    language="en",
    file_path=f'{title}.wav'
    )
    print('done converting!')
    
# tts = PiperSpeaker(voice=PiperVoiceUS.LIBRITTS)
# tts.text_to_wave(all_text, f'{title}.wav')



file_path = os.path.join(current_dir, f'{title}.wav')
# file1 = drive.CreateFile()
# file1.SetContentFile()
# file1.Upload()

folderName = 'articles'  # Name of folder in Google Drive that you want to upload to

def upload_file(folderName, title):
    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile(metadata={"title": f"{title}", 'parents': [{'id': folder['id']}]})
            file2.SetContentFile(file_path)
            file2.Upload()

generate_audio(all_text, title)
upload_file(folderName, title)
