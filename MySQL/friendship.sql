INSERT INTO users (first_name, last_name) VALUES
('Amy', 'Giver'),
('Eli', 'Byers'),
('Kermit', 'The Frog'),
('Big', 'Bird'),
('Marky', 'Mark'),
('Extra', 'User');

INSERT INTO friendships (user_id, friend_id) VALUES (1, 2), (1, 4), (1, 6);
INSERT INTO friendships (user_id, friend_id) VALUES (2, 1), (2, 3), (2, 5);
INSERT INTO friendships (user_id, friend_id) VALUES (3, 2), (3, 5);
INSERT INTO friendships (user_id, friend_id) VALUES (4, 3);
INSERT INTO friendships (user_id, friend_id) VALUES (5, 1), (5, 6);
INSERT INTO friendships (user_id, friend_id) VALUES (6, 2), (6, 3);

-- display realationships
SELECT 
    users.first_name, users.last_name,
    user2.first_name AS friend_first_name,
    user2.last_name AS friend_last_name
FROM users
INNER JOIN friendships ON users.id = friendships.user_id
INNER JOIN users AS user2 ON friendships.friend_id = user2.id;

-- Ninga Query1
SELECT user2.first_name, user2.last_name
FROM users
INNER JOIN friendships ON users.id = friendships.user_id
INNER JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 1;

--  Ninga Query2
SELECT COUNT(*) AS total_friendships 
FROM friendships;

-- Ninga Query3
SELECT users.first_name, users.last_name, 
       COUNT(*) AS friend_count
FROM users
INNER JOIN friendships ON users.id = friendships.user_id
GROUP BY users.id
ORDER BY friend_count DESC
LIMIT 1;

-- Ninga Query4
SELECT user2.first_name, user2.last_name
FROM users
INNER JOIN friendships ON users.id = friendships.user_id
INNER JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 3
ORDER BY user2.first_name ASC;

