from article_scraper import ArticleScraper
from drive_uploader import DriveUploader
from audio_generation import TextToSpeech



if __name__ == '__main__':
    article_link = input('Paste which article you want to scrape from: ')
    article = ArticleScraper(article_link)
    article.get_title()
    article.get_textbody()

    tts = TextToSpeech(article.all_text)
    match tts.software:
        case 'coqui':
            tts.coqui_to_speech(article.title)
        case 'piper':
            tts.piper_to_speech(article.title)


    drive = DriveUploader(article.title)
    drive.upload_file()
