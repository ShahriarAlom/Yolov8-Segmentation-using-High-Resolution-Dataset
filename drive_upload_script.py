import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request


def authenticate_with_google():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_250384027023-pta4o2d8qrt8q8ueiujomn3drb5d664v.apps.googleusercontent.com.json', ['https://www.googleapis.com/auth/drive.file'])
            creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    return creds

def upload_to_drive(file_path):
    creds = authenticate_with_google()
    service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {'name': os.path.basename(file_path)}
    media = MediaFileUpload(file_path, resumable=True)
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File ID: {file.get("id")}')

if __name__ == '__main__':
    file_path = "Enter_your_file_location"

    upload_to_drive(file_path)
