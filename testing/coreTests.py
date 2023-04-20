from core.session import Sessions, UserSession
from database.db import Database


def test_init_sessions() -> tuple:
    """
    Tests that the Sessions class is initialized correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    sessions = Sessions()

    if len(sessions.sessions) != 0:
        error = f"Error in test_init_sessions: Sessions dictionary is not empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is empty."


def test_add_new_session() -> tuple:
    """
    Tests that a new session is added correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)

    if len(sessions.sessions) == 0:
        error = f"Error in test_add_new_session: Sessions dictionary is empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is not empty."


def test_get_session() -> tuple:
    """
    Tests that a session is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if not isinstance(session, UserSession):
        error = f"Error in test_get_session: Session is not a UserSession object.\n  - Actual: {type(session)}"
        return False, error
    else:
        return True, "Session is a UserSession object."


def test_get_session_username() -> tuple:
    """
    Tests that a session's username is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.username != "test":
        error = f"Error in test_get_session_username: Session's username is incorrect.\n  - Expected: test\n  - Actual: {session.username}"
        return False, error
    else:
        return True, "Session's username is correct."


def test_get_session_db() -> tuple:
    """
    Tests that a session's database is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.db != db:
        error = f"Error in test_get_session_db: Session's database is incorrect.\n  - Expected: {db}\n  - Actual: {session.db}"
        return False, error
    else:
        return True, "Session's database is correct."
   
def test_create_order():
    """"
    Tests that the create_order method works
    
    args: 
    -size: the size of the cake
    -flavor: the flavor of the cake
    -frosting: the frosting used for the cake
    -filling_1: the first filling for the cake
    -filling_2: the second filling for the cake
    -toppings: toppings used for the cake
    
   
    """"
    size = 6
    flavor = "Chocolate"
    frosting = "Vanilla"
    filling_1 = "Strawberry Jam"
    filling_2 = "Chocolate Ganache"
    toppings = ["Sprinkles", "Chocolate chips"]
    expected_cake = Cake(size, flavor, frosting, filling_1, filling_2, toppings)
    assert create_order(size, flavor, frosting, filling_1, filling_2, toppings) == expected_cake

def test_calculate_price():
    
     """"
    Tests that the create_order method works
    
    args: 
    -cake_order
    """"
    size = 5
    flavor = "Chocolate"
    frosting = "Vanilla"
    filling_1 = "Strawberry Jam"
    filling_2 = "noMore"
    toppings = ["Sprinkles", "Chocolate chips"]
    cake = Cake(size, flavor, frosting, filling_1, filling_2, toppings)
    expected_price = 15.00
    assert calculate_price(cake) == expected_price

