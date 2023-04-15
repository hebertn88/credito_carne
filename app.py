from datetime import datetime

from app.controllers.files.files import find_xml_files
from app.controllers.xml.xml import Xml
from app.settings import DATE_INITIAL


xml_files = find_xml_files()

for file in xml_files:
    
    document = Xml(file)
    print(document.file_path)
    print(document.nota_fiscal.cfe)
    print(document.nota_fiscal.chave)
    print(document.nota_fiscal.data_emissao)
    print(document.nota_fiscal.data_emissao > datetime.strptime(DATE_INITIAL, '%d/%m/%Y'))
    print(document.nota_fiscal.sat)
    print(document.nota_fiscal.valor_total)
    for i in document.itens:
        print(i)
    break