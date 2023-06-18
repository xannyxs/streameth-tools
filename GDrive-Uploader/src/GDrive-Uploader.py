import os
import sys
import mimetypes

from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from typing import Any, Optional


def login_drive(service_account_file: str) -> Optional[Any]:
    creds = Credentials.from_service_account_file(service_account_file)
    return discovery.build('drive', 'v3', credentials=creds)


def upload_to_drive(video_name: str, video_path: str, service_account_file: str):
    try:
        drive_service = login_drive(service_account_file)

        file_metadata = {
            'name': video_name,
            'parents': [sys.argv[2]]
        }

        media = MediaFileUpload(video_path, resumable=True)

        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            supportsAllDrives=True,
            fields='id'
        ).execute()

        print('File ID: %s' % file.get('id'))
    except Exception as e:
        print(f"Failed to upload file: {e}")


def save_to_database(video_path: str, service_account_file: str) -> None:
    for root, dirs, files in os.walk(video_path):
        for file in files:
            filepath = os.path.join(root, file)
            mimetype, encoding = mimetypes.guess_type(filepath)
            if mimetype and mimetype.startswith('video'):
                upload_to_drive(file, filepath, service_account_file)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Need three arguments\n\n1. Path to video or directory\n2. GDrive Directory ID\n3. Path to service "
              "account credentials")
        sys.exit(1)

    save_to_database(sys.argv[1], sys.argv[3])
