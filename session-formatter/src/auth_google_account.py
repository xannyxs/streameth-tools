from typing import Any

import gspread
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from gspread import Client, Spreadsheet, Worksheet

import consts


def login_drive() -> Any:
    creds = Credentials.from_service_account_file("credentials.json")
    return discovery.build('drive', 'v3', credentials=creds)


def login_gspread() -> Client:
    return gspread.service_account("credentials.json")


def open_sheet() -> Worksheet:
    gc: Client = login_gspread()
    sheet: Spreadsheet = gc.open_by_key(consts.SPREAD_ID)
    return sheet.sheet1
