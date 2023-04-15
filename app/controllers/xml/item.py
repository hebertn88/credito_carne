from app.controllers.xml.util import check_none

class Item:
    codigo : int
    descricao : str
    ean : int
    quantidade : float
    valor_icms : float
    valor_total : float

    def __init__(self, det_xml):
        self.codigo = self._get_codigo_xml(det_xml)
        self.descricao = self._get_descricao_xml(det_xml)
        self.ean = self._get_ean_xml(det_xml)
        self.quantidade = self._get_quantidade_xml(det_xml)
        self.valor_icms = self._get_valor_icms_xml(det_xml)
        self.valor_total = self._get_valor_total_xml(det_xml)

    def __str__(self):
        return f'{self.descricao} | {self.quantidade} | {self.valor_total} | {self.valor_icms}'
        
    def _get_codigo_xml(self, det_xml):
        return check_none(det_xml.find('./prod/cProd'), int)
    
    def _get_descricao_xml(self, det_xml):
        return check_none(det_xml.find('./prod/xProd'))
    
    def _get_ean_xml(self, det_xml):
        return check_none(det_xml.find('./prod/cEAN'), int)
    
    def _get_quantidade_xml(self, det_xml):
        return check_none(det_xml.find('./prod/qCom'), float)
    
    def _get_valor_icms_xml(self, det_xml):
        return check_none(det_xml.find('./imposto/ICMS/*/vICMS'), float)
    
    def _get_valor_total_xml(self, det_xml):
        return check_none(det_xml.find('./prod/vItem'), float)
      