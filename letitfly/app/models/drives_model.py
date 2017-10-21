from app import db


class Rides(db.Model):
    """This table represents all the existing drives"""

    __tablename__ = 'drives'

    ride_id = db.Column(db.Integer, primary_key=True)
    # customer_id = db.relationship('Users', backref='customer', lazy=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'))
    # driver_id = db.relationship('Users', backref='driver', lazy=True)
    # driver_id = db.relationship('Users', backref='driver')
    start_location = db.Column(db.String(50))
    end_location = db.Column(db.String(50))
    time_finished = db.Column(db.String(50))

    def save(self):
        """Add ride to database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete ride from database"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Represent user by name"""
        return "{} {}".format(self.start_location, self.end_location)
