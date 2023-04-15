from pathlib import Path

from peewee import *


BASE_DIR : Path = Path.cwd()

DATABASE = SqliteDatabase('my_app.db')

XML_INPUT : Path = BASE_DIR / 'xml_input'
XML_OUTPUT : Path = BASE_DIR / 'xml_output'

DATE_INITIAL : str = '15/01/2023'
DATE_FINAL : str = '28/02/2023'