import os
from dotenv import load_dotenv
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive 

IMG_DIR = 'images/'
def main():
    """ Driver function """
    folderID, secretFile, credsPath = load_env()
    drive = google_auth(secretFile, credsPath)
    testFile = IMG_DIR + 'code3.jpg'
    upload_todrive(drive, folderID, testFile)

def load_env():
    """ Load environment variables from .env """
    load_dotenv()
    folderID = os.getenv('folder_id')
    secretFile = os.getenv('client_secret')
    credsPath = os.getenv('save_path')  
    return folderID, secretFile, credsPath


def google_auth(file, path):
    """ Authenticate Google Drive using OAuth API and PyDrive. """
    gauth = GoogleAuth() 
    gauth.LoadClientConfigFile(file)
    gauth.LoadCredentialsFile(path)

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile(path)
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    drive = GoogleDrive(gauth)
    return drive


def upload_todrive(drive, folder, file):
    gfile = drive.CreateFile({'parents': [{'id': folder}]})
    gfile.SetContentFile(file)
    gfile.Upload()
    print(f"File {file} uploaded successfully.")

if __name__ == "__main__":
    main()