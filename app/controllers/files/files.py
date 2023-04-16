import shutil

from app.settings import XML_INPUT, XML_OUTPUT


def find_xml_files():
    return XML_INPUT.glob('**/*.[xX][mM][lL]')


def copy_xml_file(source, target):
    try:
        shutil.copy(source, target)
    except Exception as e:
        print(f'Erro ao copiar arquivo.[{e}]')

    