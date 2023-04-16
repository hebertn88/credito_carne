from peewee import CharField, DateField, FloatField, IntegerField, Model

from app.settings import DATABASE

class DocumentoModel(Model):
    cfe = IntegerField()
    chave = CharField(max_length=200, unique=True)
    data_emissao = DateField()
    sat = CharField(max_length=200)
    valor_total = FloatField()

    class Meta:
        database = DATABASE
        table_name = 'documento'
        indexes = (
            (('cfe', 'sat'), True),
        )

