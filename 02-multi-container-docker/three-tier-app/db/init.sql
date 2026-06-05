CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

-- Insert some sample data
INSERT INTO messages (message) VALUES
    ('Hello from PostgreSQL!'),
    ('Docker containers are awesome!'),
    ('3-tier architecture works!');
