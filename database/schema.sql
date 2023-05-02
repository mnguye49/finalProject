CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name VARCHAR(255) NOT NULL,
    flavor VARCHAR(255) NOT NULL,
    frosting VARCHAR(255) NOT NULL,
    filling1 VARCHAR(255) NOT NULL,
    filling2 VARCHAR(255) NOT NULL,
    toppings VARCHAR(255) ARRAY[20],
    price DECIMAL(10,2) NOT NULL,
    size VARCHAR(255) NOT NULL,
    image_url VARCHAR(255) NOT NULL
);

CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_date DATETIME NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (item_id) REFERENCES inventory(id)
);

