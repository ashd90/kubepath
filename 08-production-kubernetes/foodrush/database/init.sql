CREATE TABLE IF NOT EXISTS restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cuisine VARCHAR(50) NOT NULL,
    rating DECIMAL(2,1) DEFAULT 0.0,
    delivery_time INTEGER DEFAULT 30,
    is_open BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO restaurants (name, cuisine, rating, delivery_time) VALUES
    ('Spice Garden', 'Indian', 4.5, 25),
    ('Dragon Palace', 'Chinese', 4.2, 35),
    ('Pizza Roma', 'Italian', 4.7, 20),
    ('Burger Barn', 'American', 4.0, 15),
    ('Sushi Sakura', 'Japanese', 4.8, 40);
