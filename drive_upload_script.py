import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

def authenticate_with_google():
    # ... [rest of the code remains unchanged]

if __name__ == '__main__':
    file_path = "C:/Users/USER OS/OneDrive/Desktop/drive_upload_project/ChatGPT_Conversation_v2.pdf"
    upload_to_drive(file_path)
