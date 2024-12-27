from Scripts.article_scraper import ArticleScraper
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from yapper import PiperSpeaker, PiperVoiceUS
import re
import os
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
current_dir = os.getcwd()

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)





def generate_audio(text, title):
    tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2').to(device)
    tts.tts_to_file(
    text = text,
    speaker="Claribel Dervla",
    language="en",
    file_path=f'{title}.mp3'
    )
    print('done converting!')
    
# tts = PiperSpeaker(voice=PiperVoiceUS.LIBRITTS)
# tts.text_to_wave(all_text, f'{title}.wav')




# file1 = drive.CreateFile()
# file1.SetContentFile()
# file1.Upload()

folderName = 'articles'  # Name of folder in Google Drive that you want to upload to

def upload_file(folderName, title):
    file_path = os.path.join(current_dir, f'{title}.mp3')
    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile(metadata={"title": f"{title}", 'parents': [{'id': folder['id']}]})
            file2.SetContentFile(file_path)
            file2.Upload()

if __name__ == '__main__':
    article_link = input('Paste which article you want to scrape from: ')
    article = ArticleScraper(article_link)
    article.get_textbody()
    # generate_audio(article.all_text, article.title)
    # upload_file(folderName, article.title)
    print(article.all_text)