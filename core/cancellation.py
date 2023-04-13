import datetime

class Cancellation:
    def __init__(self, flavor, size, decorations, delivery_time):
        self.flavor = flavor
        self.size = size
        self.decorations = decorations
        self.delivery_time = delivery_time
        self.order_time = datetime.datetime.now()

    def cancel_order(self):
        cancel_time = datetime.datetime.now()
        time_diff = self.delivery_time - cancel_time
        if time_diff.days >= 1:
            print("Order cancelled.")
        else:
            print("Sorry, order cannot be cancelled less than 24 hours before delivery time.")

    def __str__(self):
        return f"Cake order for {self.size}-inch {self.flavor} cake with {self.decorations}. Scheduled for delivery at {self.delivery_time}."
