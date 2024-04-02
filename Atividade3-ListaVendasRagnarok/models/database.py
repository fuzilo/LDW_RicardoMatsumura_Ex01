from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#item, data, valor, ultima
class Ragnarok(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(150))
    data = db.Column(db.DateTime)
    valor = db.Column(db.Integer)
    ultima = db.Column(db.DateTime)
    
def __init__(self, item, data, valor, ultima):
    self.item = item
    self.data = data
    self.valor = valor
    self.ultima = ultima