from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions
import datetime

import datetime
class Cancellation:
    def __init__(self, flavor, size, decorations, delivery_time, customer_name, customer_email, customer_phone):
        """
        Creates a new CakeOrder instance.
        
        attributes:
        flavor: The flavor of the cake (e.g. chocolate, vanilla, etc.).
        size: The size of the cake in inches (e.g. 6, 8, 10).
        decorations: A string describing the desired cake decorations.
        delivery_time: A datetime object indicating the desired delivery time.
        customer_name: The name of the customer placing the order.
        customer_email: The email address of the customer placing the order.
        customer_phone: The phone number of the customer placing the order.
        """
        self.flavor = flavor
        self.size = size
        self.decorations = decorations
        self.delivery_time = delivery_time
        self.order_time = datetime.datetime.now()
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_phone = customer_phone

    def cancel_order(self):
        """
        Cancels the cake order if it was placed at least 24 hours before the delivery time.
        """
        cancel_time = datetime.datetime.now()
        time_diff = self.delivery_time - cancel_time
        if time_diff.days >= 1:
            print("Order cancelled.")
        else:
            print("Sorry, order cannot be cancelled less than 24 hours before delivery time.")

    def __str__(self):
        """
        Returns a string representation of the cake order.
        """
        return f"Cake order for {self.size}-inch {self.flavor} cake with {self.decorations}. Scheduled for delivery at {self.delivery_time}. Customer: {self.customer_name} ({self.customer_email}, {self.customer_phone})"
