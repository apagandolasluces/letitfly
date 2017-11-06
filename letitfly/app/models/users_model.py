from app.models.database import db


class User(db.Model):
    """This class represents the customers and drivers table"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    credit_card = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    driver = db.Column(db.Boolean)
    password = db.Column(db.String(25), nullable=False)
    date_created = db.Column(db.String(50))
    date_modified = db.Column(db.String(50))

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 username,
                 password,
                 credit_card,
                 driver,
                 date_created,
                 date_modified):
        """Iniitalize with user info"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.credit_card = credit_card
        self.driver = driver
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self):
        """Add user to database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete user from database"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Represent user by name"""
        return "{} {}".format(self.first_name, self.last_name)

    def tojson(self):
        """Represent user data as JSON object"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'driver': self.driver
        }

    def is_driver(self):
        """
        Returns True if self is a driver
        False if self is a customer
        """
        return self.driver
