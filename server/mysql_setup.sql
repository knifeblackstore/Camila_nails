CREATE DATABASE IF NOT EXISTS camila_nails;
USE camila_nails;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) DEFAULT '',
  username VARCHAR(100) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  passwordHash VARCHAR(255) NOT NULL,
  role VARCHAR(50) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS uploads (
  id INT AUTO_INCREMENT PRIMARY KEY,
  filename VARCHAR(255) NOT NULL,
  url VARCHAR(255) NOT NULL,
  style VARCHAR(255) DEFAULT '',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pending (
  id INT AUTO_INCREMENT PRIMARY KEY,
  page VARCHAR(255),
  content TEXT,
  author VARCHAR(255),
  date DATETIME,
  approved TINYINT DEFAULT 0
);

INSERT INTO users (name, username, email, role, passwordHash)
SELECT 'Administrador', 'admin', 'admin@admin.com', 'admin', '$2a$10$8HijBviEyXMpnMnk.XnFNefEjGjo4j9k2tBz9nZxTsXsgSEAa9kNu'
WHERE NOT EXISTS (
  SELECT 1 FROM users WHERE email = 'admin@admin.com'
);
