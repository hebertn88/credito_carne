from datetime import datetime
from time import sleep

from app.controllers.files.files import find_xml_files
from app.controllers.setup.setup import start_app
from app.controllers.xml.xml import Xml
from app.settings import DATE_INITIAL, XML_INPUT

print("Para extrair as informações dos Cupons")
sleep(.3)
print("coloque os arquivos XML na pasta abaixo:")
sleep(.5)
print(f"{XML_INPUT}\n")
sleep(1)
start_app()

resp = input("Deseja verificar os arquivos agora? [S/N] ")
if (resp[0].upper() != 'S'):
    print("Encerrando sistema...")
    exit()

xml_files = find_xml_files()
for file in xml_files:
    
    arquivo = Xml(file)
    print(arquivo.file_path)
    #print(arquivo.cupom.cfe)
    #print(arquivo.cupom.chave)
    print(arquivo.cupom.data_emissao)
    #print(arquivo.cupom.data_emissao > datetime.strptime(DATE_INITIAL, '%d/%m/%Y'))
    #print(arquivo.cupom.sat)
    #print(arquivo.cupom.valor_total)
    print(f'{arquivo.aliquota_icms_existe(18)=}')
    #for i in arquivo.itens:
    #    print(i)
    arquivo.check_and_save(5.5)

print('fim')