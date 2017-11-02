from datetime import datetime
from app.models.users_model import Ride


def post(args):
    """
    Creates new uride
    :args: ride
    """

    customer_id = args['customer_id']

    driver_id = args['driver_id']

    start_location = args['start_location']

    time_started = args['time_started']

    if customer_id and driver_id and start_location:
            ride = Ride(
                        customer_id=customer_id,
                        driver_id=driver_id,
                        start_location=start_location,
                        end_location=start_location,
                        time_finished=str(datetime.now()),
                        time_started=str(datetime.now()),
                        cost='$0.00'
                        )

            ride.save()

            return ride.tojson()

    else:
        return None


def put(args):
    """
    Edit user info
    :args: user info
    """

    # find user in database
    ride = Ride.query.filter_by(
                                customer_id=args['customer_id'],
                                driver_id=args['driver_id'],
                                start_location=args['start_location'],
                                time_started=args['time_started']
                                ).first()

    # makes user info updates
    if ride:
        for key in args:
            if hasattr(ride, key):
                ride.key = args[key]

    # note when ride info updated
    ride.date_modified = str(datetime.now())

    # save changes
    ride.save()

    return ride.tojson()

    else:
        return None


# map which method to carry out
ride_request = {
    "CREATE": post,
    "EDIT": put
}


def manipulation(args):
    """
    Selects correct method via dict
    :args: arguments
    """
    response = ride_request[args['request']](args) # need args to include http request
    return response
