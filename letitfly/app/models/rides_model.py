from app.models.database import db


class Ride(db.Model):
    """This table represents all the existing rides"""

    __tablename__ = 'rides'

    ride_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    start_location = db.Column(db.String(50))
    end_location = db.Column(db.String(50))
    time_finished = db.Column(db.String(50))
    cost = db.Column(db.String)

    def __init__(self, ride_id, customer_id,
                 driver_id, start_location,
                 end_location, time_finished, cost):
        self.ride_id = ride_id
        self.customer_id = customer_id
        self.driver_id = driver_id
        self.start_location = start_location
        self.end_location = end_location
        self.time_finished = time_finished
        self.cost = cost

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

    def tojson(self):
        """Represent ride data as JSON object"""
        return {
            'customer_id': self.customer_id,
            'driver_id': self.driver_id,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'time_finished': self.time_finished,
            'cost': self.cost
        }
