from peewee import CharField, ForeignKeyField, FloatField, IntegerField, Model

from app.models.documento import DocumentoModel
from app.settings import DATABASE


class ItemModel(Model):
    documento = ForeignKeyField(DocumentoModel, backref='itens')
    codigo = IntegerField()
    ean = IntegerField()
    descricao = CharField(max_length=200)
    quantidade = FloatField()
    valor_total = FloatField()
    aliquota_icms = FloatField()
    valor_icms = FloatField()

    class Meta:
        database = DATABASE
        table_name = 'item'