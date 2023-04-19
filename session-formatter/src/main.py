from typing import Any, List
from session import Session
from gspread import Worksheet
from consts import PRIMARY_KEYWORDS
from parse_session import parse_sessions
from auth_google_account import open_sheet


def get_cell_data(row: list):
    matched_columns = []

    for index, cell in enumerate(row):
        if cell in PRIMARY_KEYWORDS:
            column_letter = chr(index + ord('A'))
            matched_columns.append((cell, column_letter))

    return matched_columns


if __name__ == "__main__":
    worksheet: Worksheet = open_sheet()
    filled_columns: list[tuple[Any, str]] = get_cell_data(worksheet.row_values(1))

    # Check if it exists and if it is "Session"
    if filled_columns[2] and filled_columns[2][0] == PRIMARY_KEYWORDS[2]:
        all_sessions: List[Session] = parse_sessions(worksheet, filled_columns[2])
