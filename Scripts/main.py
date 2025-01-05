from article_scraper import ArticleScraper
from drive_uploader import DriveUploader
from audio_generation import TextToSpeech
from tqdm import tqdm
import validators


def return_links():
    """
    Prompts the user to enter a file name or a link. If a valid URL is entered, it is added to a list.
    If a file name is entered, the file is read line by line, and valid URLs are added to the list.

    Returns:
        list: A list of valid URLs.
    """
    links= []
    if validators.url(article_link := input('Enter a file name containing URLs or an URL: ')):
        links.append(article_link)
    else:
        with open(article_link) as file:
            while line := file.readline():
                if validators.url(line.rstrip()):
                    links.append(line.rstrip())
                else:
                    continue
    return links



def main():
    """
    Main function to scrape an article, convert its text to speech, and upload the result to a drive.
    Steps:
    1. Scrape an article using ArticleScraper.
    2. Retrieve the title and text body of the article.
    3. Convert the article text to speech using TextToSpeech with specified software ('coqui' or 'piper').
    4. Upload the resulting file to a drive using DriveUploader.
    Classes used:
    - ArticleScraper: Handles scraping of the article.
    - TextToSpeech: Converts text to speech.
    - DriveUploader: Uploads files to a drive.
    Note:
    - The `return_links` function is assumed to provide the necessary links for scraping.
    - The `article.all_text` and `article.title` are used for text-to-speech conversion and file naming respectively.
    """
    drive = DriveUploader()
    
    for link in tqdm(return_links()):
        article = ArticleScraper(link)
        article.get_title()
        article.get_textbody()

        tts = TextToSpeech(article.all_text, software='piper')
        match tts.software:
            case 'coqui':
                tts.coqui_to_speech(article.title)
            case 'piper':
                tts.piper_to_speech(article.title)


        
        drive.upload_file(article.title)

if __name__ == '__main__':
    main()

