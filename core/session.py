from core.utils import calculate_total_cost
from datetime import datetime
from database.db import Database


class Order:
    """
    Order is a class that represents the user's order.

    args:
        - username: The username of the user.
        - db: The database to use.

    attributes:
        - is_Custom: A bool determining if the user wants their cake custom ordered or not
        - cake: An object containing the cake that the user ordered
        - time: the frosting they want on the cake
        - date: A dictionary of dictionaries representing the items in the user's cart.
        - total_cost: The total cost of the order.
        - date: The date the user wants their cake by
        - is_Delivery: a bool determining whether the user wants to have their cake delivered or picked up in person.
    """

    def __init__(self):
        self.is_Custom = False
        self.total_cost = 0.0
        self.time = None
        self.date = None
        self.is_Delivery = True

    def create_order(flavor, frosting, filling_1, filling_2, toppings) -> Cake:
        """
        Creates a new item to add to the user's cart.

        args:
            - id: The id of the item.
            - name: The name of the item.
            - price: The price of the item.
            - quantity: The quantity of the item.
            - discount: The discount of the item.
            - tax_rate: The tax rate of the item.

        returns:
            - None
        """
        flav = flavor
        frost = frosting
        fill_one = filling_1   
        fill_two = filling_2
        top = []
        for each topping in toppings:
            top.append(topping)
        
        new_Cake = new Cake(flav,frost,fill_one, fill_two,top)
        return new_Cake

    def update_item_quantity(self, id: str, change_to_quantity: int) -> None:
        """
        Updates the quantity of an item in the user's cart.

        args:
            - id: The id of the item.
            - quantity: The quantity of the item.
        """
        if self.cart[id]["quantity"] + change_to_quantity <= 0:
            self.remove_item(id)
        else:
            self.cart[id]["quantity"] += change_to_quantity

    def remove_item(self, id: str) -> None:
        """
        Removes an item from the user's cart.

        args:
            - id: The id of the item.
        """
        del self.cart[id]

    def update_total_cost(self) -> None:
        """
        Updates the total cost of the user's cart.
        """
        self.total_cost = calculate_total_cost(self.cart)

    def submit_cart(self) -> None:
        """
        Called when the order is submitted. Finalizes user session details.

        args:
            - None

        returns:
            - None
        """
        self.update_total_cost()
        self.date = datetime.now()

class Cake:
    
    def __init__(self, flavor: str, frosting: str, filling_one: str, filling_two: str, toppings):
        self.flavor = flavor
        self.frosting = frosting
        self.filling_one = filling_one
        self.filling_two = filling_two
        self.toppings = toppings
    
    

class Sessions:
    """
    Sessions is a class that represents the collection of active sessions.

    args:
        - None

    attributes:
        - sessions: A dictionary of user sessions.
    """

    def __init__(self):
        self.sessions = {}

    def add_new_session(self, username: str, db: Database) -> None:
        """
        Adds a new user session to the collection of sessions.

        args:
            - username: The username of the user.
            - db: The database to use.

        returns:
            - None
        """
        self.sessions[username] = UserSession(username, db)

    def get_session(self, username: str) -> UserSession:
        """
        Gets a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - The user session.
        """
        return self.sessions[username]

    def remove_session(self, username: str) -> None:
        """
        Removes a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - None
        """
        del self.sessions[username]

    def get_all_sessions(self) -> dict:
        """
        Gets all user sessions from the collection of sessions.

        args:
            - None

        returns:
            - A dictionary of user sessions.
        """
        return self.sessions
