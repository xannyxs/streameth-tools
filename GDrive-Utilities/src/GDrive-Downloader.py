import os
import io
import sys

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials


def login_drive(service_account_file: str):
    creds = Credentials.from_service_account_file(service_account_file)
    return build('drive', 'v3', credentials=creds)


def download_file(file_id, file_name, drive_service):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")


def download_directory(directory_id, local_path, drive_service):
    query = f"'{directory_id}' in parents"

    if not os.path.exists(local_path):
        os.makedirs(local_path)

    results = drive_service.files().list(q=query, supportsAllDrives=True,
                                         includeItemsFromAllDrives=True).execute()
    items = results.get('files', [])

    if not items:
        print('No files found in the directory.')
    else:
        print('Files found in the directory:')
        for item in items:
            file_name = os.path.join(local_path, item['name'])
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                print(f"Traversing into directory: {item['name']}")
                download_directory(item['id'], file_name, drive_service)
            else:
                print(f"Downloading {item['name']} ...")
                download_file(item['id'], file_name, drive_service)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Need three arguments:\n"
              "1. Google Drive Directory ID\n"
              "2. Local Path to download the directory\n"
              "3. Path to service account credentials")
        sys.exit(1)

    drive_service = login_drive(sys.argv[3])
    download_directory(sys.argv[1], sys.argv[2], drive_service)
    drive_service.close()
