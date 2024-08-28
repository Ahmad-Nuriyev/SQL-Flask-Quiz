from extensions import db

class Movie (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    title = db.Column (db.String(100), nullable=False)
    released = db.Column (db.DateTime)
    director = db.Column (db.String(100), nullable=False)
    genre = db.Column (db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    def __repr__(self):
        return f"<{self.title}"
    
    def save(self):
        db.session.add(self)
        db.session.commit()


