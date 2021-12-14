
from app import db





#Define models(Tables)
class URL(db.Model):
    __tablename__ = "urls"
    
    id = db.Column(db.Integer, primary_key=True) #primary_key is also auto increment
    short_name = db.Column(db.String(200), unique=True, nullable=False)
    url = db.Column(db.Text, nullable=False) #text suitable for large strings
    url_type = db.Column(db.String(10), nullable=False)

    
    #printable representation of each record
    def __repr__(self):
        return(f"<URL(id'{self.id}', short_name'{self.short_name}', url'{self.url}', url_type'{self.url_type}')>")



