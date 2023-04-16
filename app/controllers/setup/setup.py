from pathlib import Path

from app.models.documento import DocumentoModel
from app.models.item import ItemModel
from app.settings import DATABASE_PATH, DATABASE, XML_INPUT, XML_OUTPUT

def check_database():
    DATABASE.connect()
    DATABASE.create_tables([DocumentoModel, ItemModel])

    registros = DocumentoModel.select()
    if DATABASE_PATH.exists() and registros:
        resp = input('Deseja excluir os registros já existentes no banco de Dados? [S/N] ')
        if resp[0].upper() == 'S':
            DocumentoModel.delete().execute()
            ItemModel.delete().execute()


def check_directories():
    XML_INPUT.mkdir(parents=True, exist_ok=True)
    XML_OUTPUT.mkdir(parents=True, exist_ok=True)

def start_app():
    check_database()
    check_directories()