from datetime import datetime
from pathlib import Path

import xml.etree.ElementTree as Et

from app.controllers.files.files import copy_xml_file
from app.controllers.xml.documento import Document
from app.controllers.xml.item import Item
from app.controllers.xml.util import check_none
from app.settings import DATE_FINAL, DATE_INITIAL, DATABASE, XML_OUTPUT

class Xml:
    tree : Et.ElementTree
    root : Et.Element
    file_path : Path
    
    def __init__(self, file_path):
        self.file_path = file_path

        with open(self.file_path) as file:
            self.tree = Et.parse(file_path)

        self.root = self.tree.getroot()


    @property
    def itens(self) -> list[Et.Element]:
        det_list_xml = self.root.findall('.infCFe/det')

        return [Item(det_xml) for det_xml in det_list_xml]
    

    @property    
    def cupom(self):
        return Document(self.root)
    

    def save_xml(self):
        with DATABASE.atomic():
            documento = self.cupom.save_documento()
            
            for item_xml in self.itens:
                item_xml.save_item(documento)
        
        xml_target = XML_OUTPUT / self.file_path.name
        copy_xml_file(self.file_path, xml_target )


    def aliquota_icms_existe(self, aliquota):
        for item in self.itens:
            if aliquota == item.aliquota_icms:
                return True
        return False
    
    
    def verifica_data(self):
        data_inicial = datetime.strptime(DATE_INITIAL, '%d/%m/%Y')
        data_final = datetime.strptime(DATE_FINAL, '%d/%m/%Y')
        return data_inicial <= self.cupom.data_emissao <= data_final


    def check_and_save(self, aliquota):
        if self.aliquota_icms_existe(aliquota) and self.verifica_data():
            self.save_xml()

