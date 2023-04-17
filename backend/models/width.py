from public.config import *


class Width(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Text)
    css_width_reference = db.Column(db.Text)
    css_dungarees_reference = db.Column(db.Text)

    def __str__(self):
        return f"{self.id}, {self.width}, {self.css_width_reference}, {self.css_dungarees_reference}"
    
    def json(self):
        return {
            "id": self.id,
            "width": self.width,
            "css_width": self.css_width_reference,
            "css_dungarees": self.css_dungarees_reference
        }