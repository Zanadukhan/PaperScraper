from article_scraper import ArticleScraper
"""
This script scrapes an article from a given link, converts the article text to speech, 
and uploads the generated audio file to a drive.
Classes:
    ArticleScraper: A class to scrape the title and text body of an article from a given link.
    TextToSpeech: A class to convert text to speech using different software options.
    DriveUploader: A class to upload files to a drive.
Functions:
    main: The main function that orchestrates the scraping, text-to-speech conversion, and file upload.
Usage:
    Run the script and input the article link when prompted. The script will scrape the article, 
    convert the text to speech, and upload the audio file to the drive.
"""
from drive_uploader import DriveUploader
from audio_generation import TextToSpeech



if __name__ == '__main__':
    article_link = input('Paste which article you want to scrape from: ')
    article = ArticleScraper(article_link)
    article.get_title()
    article.get_textbody()
    
    print(article.all_text)

    # tts = TextToSpeech(article.all_text)
    # match tts.software:
    #     case 'coqui':
    #         tts.coqui_to_speech(article.title)
    #     case 'piper':
    #         tts.piper_to_speech(article.title)


    # drive = DriveUploader(article.title)
    # drive.upload_file()
