import os
import unittest
from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
# DO NOT remove this like
# Needed to make flask-migration work
from app.models import drives_model, users_model

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# define our command for testing called "test"
# Usage: python manage.py test
@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
