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
        - total_cost: The total cost of the order.
        - date: The date the user wants their cake by
        - time: The time they want want the cake by
        - is_Delivery: a bool determining whether the user wants to have their cake delivered or picked up in person.
        - order_time: the time in which the user ordered the cake
    """

    def __init__(self, name, email, phone):
        self.is_Custom = False
        self.total_cost = 0.0
        self.time = None
        self.date = None
        self.is_Delivery = True
        self.order = None
        self.order_time = datetime.now()
        self.name = name
        self.email = email
        self.phone = phone

    def create_order(size, flavor, frosting, filling_1, filling_2, toppings) -> None:
        """
        Creates a cake order as per the user's choice(s).

        args:
      

        returns:
            - Cake
        """
        cake_size = size
        flav = flavor
        frost = frosting
        fill_one = filling_1   
        fill_two = filling_2
        top = []
        for each topping in toppings:
            top.append(topping)
        
        new_Cake = new Cake(flav,frost,fill_one, fill_two,top)
        self.order = new_Cake
    
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
        self.orders = {}

    def add_order_to_history(self, username: str, db: Database, ord: Order) -> None:
        """
        Adds an order to the collection of previous orders.

        args:
            - username: The username of the user.
            - db: The database to use.

        returns:
            - None
        """
        self.orders[username] = ord

    def get_all_sessions(self) -> dict:
        """
        Gets all user sessions from the collection of sessions.

        args:
            - None

        returns:
            - A dictionary of user sessions.
        """
        return self.orders
    
    def cancel_order(self, username: str, ord: Order) -> str:
        """
        Removes a user session from the collection of sessions.
        args:
            - username: The username of the user.
        returns:
            - None
        """
        canceled = 'Order Cancelled'
        cancellation_failed = 'Sorry, order cannot be cancelled after 24 hours since ordering'
        cancel_time = datetime.now()
        time_diff = ord.order_time - cancel_time
        
        if time_diff.days <= 1:
            del self.orders[username]
            return canceled
        else:
            return cancellation_failed
               
    def show_rewards(username):
        reward = 0
        current_rewards = []
        with open("core/orderCount.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.split(":")[0] == username:
                    count = line.split(":")[1]
                    reward = int(count)
                
        with open("core/orderCount.txt","r") as files:
            file_reader = files.readlines()
            for fr in file_reader:
                splitted_num = fr.split(":")[0]
                reward_num = int(splitted_num)
                reward_str = fr.split(":")[1]
                if r <= reward:
                    current_rewards.append(reward_str)
        
        return current_rewards                
            
    def update_rewards(username: str):
        
        with open("core/orderCount.txt", "r") as file:
            lines = file.readlines()
        with open("core/orderCount.txt", "w") as file:
            found = False
            for line in lines:
                if line.split(":")[0] == username:
                    found = True
                    count = line.split(":")[1]
                    currOrders = int(count)
                    updated = count+1
                    updatedOrders = str(updated)
                    file.write(f"{username}:{updatedOrders}")
                else:
                    file.write(line)
            if not found:
                file.write(f"\n{username}:1")
                
  
