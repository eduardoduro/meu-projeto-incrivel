CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    target_course VARCHAR(100),
    target_university VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);