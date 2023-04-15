from datetime import datetime
from pathlib import Path

import xml.etree.ElementTree as Et

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
        return self.root.findall('.infCFe/det')
    
    @property    
    def nota_fiscal(self):
        return Document(self.root)

 
class Document:
    cfe : int
    chave : str
    data_emissao : datetime
    sat : str
    valor_total : float

    
    def __init__(self, root):
        self.cfe = self._get_cfe_xml(root)
        self.chave = self._get_chave_xml(root)
        self.data_emissao = self._get_data_emissao_xml(root)
        self.sat = self._get_sat_xml(root)
        self.valor_total = self._get_valor_total_xml(root)
        
    def _get_cfe_xml(self, root):
        return int(root.find('./infCFe/ide/nCFe').text)
    
    def _get_chave_xml(self, root):
        return root.find('./infCFe').get('Id')[3:]
    
    def _get_data_emissao_xml(self, root):
        data_xml = root.find('./infCFe/ide/dEmi').text
        return datetime.strptime(data_xml, '%Y%m%d')

    def _get_sat_xml(self, root):
        return root.find('./infCFe/ide/nserieSAT').text
    
    def _get_valor_total_xml(self, root):
        return float(root.find('./infCFe/total/vCFe').text)
