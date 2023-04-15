from datetime import datetime

from app.controllers.xml.util import check_none


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
        return check_none(root.find('./infCFe/ide/nCFe'), int)
    
    def _get_chave_xml(self, root):
        if root.find('./infCFe'):
            return root.find('./infCFe').get('Id')[3:]
        return None
    
    def _get_data_emissao_xml(self, root):
        data_xml = check_none(root.find('./infCFe/ide/dEmi'))
        if data_xml:
            return datetime.strptime(data_xml, '%Y%m%d')
        return None

    def _get_sat_xml(self, root):
        return check_none(root.find('./infCFe/ide/nserieSAT'))
    
    def _get_valor_total_xml(self, root):
        return check_none(root.find('./infCFe/total/vCFe'), float)