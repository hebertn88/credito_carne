from peewee import CharField, DateField, FloatField, IntegerField, Model

from app.settings import DATABASE

class ItemModel(Model):
    codigo = IntegerField()
    descricao = CharField(max_length=200)
    ean = IntegerField()
    quantidade = FloatField()
    valor_icms = FloatField()
    valor_total = FloatField()

    class Meta:
        database = DATABASE