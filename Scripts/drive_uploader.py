

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


current_dir = os.getcwd()

class DriveUploader:
    """
    A class to handle uploading files to Google Drive.
    Attributes:
    -----------
    drive_folder : str
        The name of the folder in Google Drive where the file will be uploaded.
    file_path : str
        The path to the file that will be uploaded.
    Methods:
    --------
    __init__(title, drive_folder='articles'):
        Initializes the DriveUploader with the given title and drive folder.
    upload_file():
        Uploads the file to the specified Google Drive folder.
    """
    def __init__(self, title, drive_folder='articles'):
        self.drive_folder = drive_folder
        self.file_path = os.path.join(current_dir, f'{title}.mp3')
        
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)
        
    def upload_file(self):
        folders = self.drive.ListFile(
            {'q': "title='" + self.drive_folder + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        for folder in folders:
            if folder['title'] == self.drive_folder:
                file2 = self.drive.CreateFile(metadata={"title": f"{self.title}", 'parents': [{'id': folder['id']}]})
                file2.SetContentFile(self.file_path)
                file2.Upload()
        print('done uploading!')