from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os, io
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = '1b0avE7pbxJFj3OY8M5f1A5iMEp8p65yh'

def authenticate_google():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

def download_documents(folder_id, target_dir='docs'):
    service = authenticate_google()
    os.makedirs(target_dir, exist_ok=True)
    query = f"'{folder_id}' in parents and trashed = false"
    results = service.files().list(q=query).execute()
    for file in results['files']:
        file_id = file['id']
        file_name = file['name']
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(target_dir, file_name), 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            _, done = downloader.next_chunk()
