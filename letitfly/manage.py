import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.database import db
from app import create_app
from app.models import rides_model
from app.models import users_model

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
