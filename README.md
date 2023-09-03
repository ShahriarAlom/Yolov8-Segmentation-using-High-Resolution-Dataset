# Automatic_Google_Drive_File_Uploader
This script allows you to upload a file to Google Drive using Python automatically.

##Prerequisites:
Python: Ensure you have Python installed. If not, download and install it from python.org.

##Google Cloud Platform (GCP) Account: You need a GCP account to create OAuth 2.0 client IDs. If you don't have one, sign up here.

#Setup
Create a Google Cloud Project:

Go to the Google Cloud Console.
Click on the project dropdown and select New Project.
Give it a name and create it.
Enable the Google Drive API:

In the GCP dashboard, navigate to APIs & Services > Library.
Search for "Google Drive API" and enable it for your project.
Create OAuth 2.0 client IDs:

Navigate to APIs & Services > Credentials.
Click on Create Credentials and select OAuth 2.0 Client IDs.
Choose Desktop App as the application type.
Click Create and download the client secret JSON file.
Rename the downloaded file to client_secret.json and place it in the same directory as the script.
Install Required Python Libraries:

Open a terminal or command prompt.
Navigate to the directory containing the script.

#Install the required libraries using pip:
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
