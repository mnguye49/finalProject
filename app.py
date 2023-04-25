#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, is_custom, is_delivery, logged_in, account
username = 'default'
db = Database('database/storeRecords.db')
products = db.get_full_inventory()
logged_in = False
is_custom = False
is_delivery = True
global CAKE
global CONTACT_INFO

CAKE = {
    'flavor': '',
    'frosting': '',
    'size': 9,
    'filling_one': '',
    'filling_two':'',
    'toppings': []
}

CONTACT_INFO = {
    'name': '',
    'email': '',
    'num': ''
}

@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        logged_in = True
        account = Account()
        return render_template('home.html', products=products, sessions=sessions)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html')


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/storeRecords.db: adds a new user to the database
    """
    while True:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        if check_email(email) == False:
            break
        
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    return render_template('index.html')

@app.route('/orderStart', methods=['POST'])
def orderStart():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['num']
    
    CONTACT_INFO['name'] = name
    CONTACT_INFO['email'] = email
    CONTACT_INFO['num'] = phone_number

@app.route('/customization', methods=['POST'])
def customization():
    flav = request.form['flav']
    frost = request.form['frost']
    
    CAKE['flavor'] = flav
    CAKE['frosting'] = frost
    
    return render_template('customization.html', flav=flav, frost=frost)

@app.route('/payment', methods=['POST'])
def payment():
    if request.form['filling_one'] == other:
        filling1 = request.form['altOption']
    else:
        filling1 = request.form['filling_one']
        
    if request.form['filling_two'] == other2:
        filling2 = request.form['altOption2']
    else:
        filling2 = request.form['filling_two']
    
    wanted = request.form.getlist('top')
    if request.form.get('otherTop'):
        other_topping = request.form.get('altTop')
        wanted.append(other_topping)
    CAKE['filling_one']=filling1
    CAKE['filling_two']=filling2
    CAKE['toppings']=wanted

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    cake_flavor = CAKE.get['flavor']
    cake_frosting = CAKE.get['frosting']
    cake_size = CAKE.get['size']
    cake_fill1 = CAKE.get['filling_1']
    cake_fill2 = CAKE.get['filling_2']
    cake_toppings = CAKE.get['toppings']
    order_name = CONTACT_INFO.get['name']
    order_email = CONTACT_INFO.get['email']
    contact_num = CONTACT_INFO.get['num']
    order = new Order(order_name,order_email, contact_num)
    cakes = order.create_order(cake_size, cake_flavor, cake_frosting, cake_fill1, cakefill2, cake_toppings)
    order.cake = cakes
    order.calculate_price(order.cake)
    if logged_in == True:
        account.add_order_to_history(order)
        
    user_session = sessions.get_session(username)
    for item in products:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)

    user_session.submit_cart()

    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)

def cancel:
    
if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
