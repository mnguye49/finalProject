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
        Creates a cake order as per the user's choice(s).

        args:
      

        returns:
            - Cake
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
    
    def calculate_price(self, cake_order):
        curr_price = 20.00
        
        if (cake_order.filling_one != "frosting"):
            curr_price += 2.00
        if (cake_order.filling_two != "noMore"):
            curr_price += 2.00
        
        for each t in cake_order.toppings:
            curr_price += 1.00
        
        if (self.isDelivery == True):
            curr_price += 3.00
        
        self.total_cost = curr_price
        
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
         
    

class Account:
    """
    Sessions is a class that represents the collection of active sessions.

    args:
        - None

    attributes:
        - orders: A dictionary of past user orders.
    """

    def __init__(self):
        self.sessions.orders = {}

    def add_order_to_history(self, username: str, db: Database, ord: Order) -> None:
        """
        Adds an order to the collection of previous orders.

        args:
            - username: The username of the user.
            - db: The database to use.

        returns:
            - None
        """
        self.sessions.append(ord) 

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
        return self.orders
