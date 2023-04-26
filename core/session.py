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
        - cake: An object containing the cake that the user ordered
        - frosting: the frosting they want on the cake
        - total_cost: The total cost of the order.
        - date: The date the user wants their cake by
        - time: The time they want want the cake by
        - order_time: the time in which the user ordered the cake
    """

    def __init__(self, name, email, phone):
        self.total_cost = 0.0
        self.time = None
        self.date = None
        self.cake = None
        self.order_time = datetime.now()
        self.name = name
        self.email = email
        self.phone = phone

    def create_order(size, flavor, frosting, filling_1, filling_2, toppings) -> Cake:
        """
        Creates a cake order as per the user's choice(s).

        args:
            -size: the size of the cake
            -flavor: the flavor of the cake
            -frosting: the frosting used for the cake
            -filling_1: the first filling for the cake
            -filling_2: the second filling for the cake
            -toppings: toppings used for the cake
      

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
        
        new_Cake = new Cake(size, flav,frost,fill_one, fill_two,top)
        return new_Cake
    
    def calculate_price(self, cake_order):
        """
        Calculates the price for the cake order. Costs extra money for fillings, toppings, and delivery.
        The pricing after 5 inches starts out at $18 and increases by $8 for every 2 inches 
        args:
            -cake_order: the cake that is being ordered
        returns:
            -curr_price: the price of the order
        """
        if cake_order.size <= 5:
            curr_price = 11.00
        else:
            size_diff = cake_order.size - 6
            upcharge = size_diff * 8.00
            adjustment = size_diff % 2
            adjusted = upcharge - adjustment
            curr_price = 18.00 + adjusted
        
        if cake_order.filling_one != "frosting":
            curr_price += 2.00
        if cake_order.filling_two != "noMore":
            curr_price += 2.00
        
        for each t in cake_order.toppings:
            curr_price += 1.00
        
        self.total_cost = curr_price
        
        

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
        
    def apply_reward(self, username: str, ord: Order):
        reward = 0
        toppings = ord.cake.top
        with open("core/orderCount.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.split(":")[0] == username:
                    count = line.split(":")[1]
                    reward = int(count)
        r = reward
        if reward > 100:
            r = reward % 100
        
        with open("core/rewards.txt","r") as files:
            file_reader = files.readlines()
            for fr in file_reader:
                splitted_num = fr.split(":")[0]
                reward_num = int(splitted_num)
                reward_str = fr.split(":")[1]
                if r == reward_num:
                    if r == 1:
                        discounted = ord.total_cost * 0.9
                        ord.total_cost = discounted
                    elif r == 3:
                        toppings = ord.cake
                        if len(toppings) <= 2:
                            ord.total_cost -= 2.00
                            
    def show_rewards(username):
        """
        Shows any rewards that the user has earned
        args:
            -username: the username of the user
        returns:
            -None
        """
        reward = 0
        current_rewards = []
        with open("core/orderCount.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.split(":")[0] == username:
                    count = line.split(":")[1]
                    reward = int(count)
                
        with open("core/rewards.txt","r") as files:
            file_reader = files.readlines()
            for fr in file_reader:
                splitted_num = fr.split(":")[0]
                reward_num = int(splitted_num)
                reward_str = fr.split(":")[1]
                if reward_num <= reward:
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
                
  
