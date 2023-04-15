from app.settings import XML_INPUT

def find_xml_files():
    return XML_INPUT.glob('**/*.[xX][mM][lL]')
    