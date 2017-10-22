from datetime import datetime
from flask import jsonify
from app.models.users_model import User


def post(args):
    """
    Creates new user
    :args: user data
    """

    # validate credit card format
    potential_credit_card = args['credit_card']
    if (potential_credit_card.isdigit()) and \
       (len(potential_credit_card) is 15 or len(potential_credit_card) is 16):
        credit_card = potential_credit_card
    else:
        return None

    first_name = args['first_name']

    last_name = args['last_name']

    email = args['email']

    driver = args['driver']

    username = args['username']

    password = args['password']

    date_created = str(datetime.now())

    date_modified = date_created

    if credit_card and email and username and password \
       and first_name and last_name and driver:
            user = User(
                        first_name=first_name, last_name=last_name,
                        email=email, driver=driver, username=username,
                        password=password, date_created=date_created,
                        date_modified=date_modified
                        )

            user.save()

            return user.tojson()

    else:
        return None

def delete(args):
    """
    Deletes a user
    :args: data to find user in database
    """

    # find user
    user = User.query.filter_by(email=args['email']).first()

    if user:
        user.delete()
        return 'User deleted.'

    else:
        return None

def put(args):
    """
    Edit user info
    :args: user info
    """

    # find user in database
    user = User.query.filter_by(email=args['email']).first()

    # makes user info updates
    if user:
        for key in args:
            if hasattr(user, key):
                user.key = args[key]

    # note when user info updated
    user.date_modified = str(datetime.now())

    # save changes
    user.save()

    return user.tojson()

    else:
        return None

def get(args):
    """
    Gets user
    :args: user email
    """
    user = User.query.filter_by(email=args['email']).first()

    if user:
        return user.json()
    else:
        return None


# map which method to carry out
user_request = {
    "CREATE": post,
    "REMOVE": delete,
    "EDIT": put,
    "RETRIEVE": get
}


def manipulation(args):
    """
    Selects correct method via dict
    :args: arguments
    """
    response = user_request[args['type']](args)
    return response
