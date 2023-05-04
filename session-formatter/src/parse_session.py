from typing import Any, Tuple, List
from gspread import Worksheet
from session import Session

# For now...
COLUMN_RANGE = "L2:Y2"


def get_cell_value(PRIMARY_ROW: list, row: list, index: int, expected_label: str):
    if PRIMARY_ROW[index].value == expected_label:
        return row[index].value
    return None

def parse_session(PRIMARY_ROW, row):
    attributes = ['id', 'Name', 'Description', 'StageId', 'Day', 'Start', 'End']

    for attribute in attributes:
        PRIMARY_ROW[attribute]

    id = get_cell_value(PRIMARY_ROW, row, 0, 'id')
    name = get_cell_value(PRIMARY_ROW, row, 1, 'Name')
    description = get_cell_value(PRIMARY_ROW, row, 2, 'Description')
    stage_id = get_cell_value(PRIMARY_ROW, row, 3, 'StageId')
    day = get_cell_value(PRIMARY_ROW, row, 4, 'Day')
    start = get_cell_value(PRIMARY_ROW, row, 5, 'Start')
    end = get_cell_value(PRIMARY_ROW, row, 6, 'End')
    speaker_ids = [get_cell_value(PRIMARY_ROW, row, i, f'Speaker{i - 6}Id') for i in range(7, 11)]
    video = get_cell_value(PRIMARY_ROW, row, 12, 'video')
    is_tweeted = get_cell_value(PRIMARY_ROW, row, 13, 'isTweeted')

def create_rows(cell_list, len: int):
    for cell_list in range(0, 1):
        cell_list


def parse_sessions(sheet: Worksheet, session_cell: Tuple[Any, str]) -> List[Session]:
    PRIMARY_ROW = sheet.range(COLUMN_RANGE)
    all_sessions: List[Session] = []
    max_rows = len(sheet.col_values(ord('L') - ord('A') + 1))

    cell_list = sheet.range(f'L4:Y{max_rows}')
    create_rows(cell_list, 9)
    print(cell_list)
    # for row in all_rows:
    #     parse_session(row)
    # for i in range(4, max_rows):
    #     row = sheet.range(f'L{i}:Y{i}')



    #all_sessions.append(Session(id, name, description, stage_id, day, start, end, speaker_ids, video, is_tweeted))

    #return all_sessions
