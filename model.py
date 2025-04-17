from app import db 
from datetime import datetime


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)  
    title = db.Column(db.String(100), nullable=False) 
    entry_content = db.Column(db.Text, nullable=False)  

    def __init__(self, title, entry_content, date):
        self.title = title
        self.entry_content = entry_content
        self.date = date

    def __repr__(self):
        return f"Section({self.title}, {self.date}, {self.entry_content[:70]})"