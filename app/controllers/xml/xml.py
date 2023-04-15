from datetime import datetime
from pathlib import Path

import xml.etree.ElementTree as Et

from app.controllers.xml.documento import Document
from app.controllers.xml.item import Item

class Xml:
    tree : Et.ElementTree
    root : Et.Element
    file_path : Path
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = Et.parse(file_path)
        self.root = self.tree.getroot()
        
    @property
    def itens(self) -> list[Et.Element]:
        det_list_xml = self.root.findall('.infCFe/det')

        return [Item(det_xml) for det_xml in det_list_xml]
    
    @property    
    def nota_fiscal(self):
        return Document(self.root)

