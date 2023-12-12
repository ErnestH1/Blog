MVPs (Minimum Viable Products):

    User Authentication: Users can sign up, log in, and log out.
    Blog Posts: Allow users to create, view, and edit their blog posts.
    Comments: Enable users to comment on blog posts.

User Stories:

    As a user, I can sign up for a new account using my email and password.
    As a user, I can log in using my credentials to create new blog posts.
    As a user, I can comment on blog posts created by others.

Database Table Schema:

For this system, let's create three tables: Users, Posts, and Comments.
Users Table:

    user_id (Primary Key)
    username
    email
    password_hash
    created_at

Posts Table:

    post_id (Primary Key)
    user_id (Foreign Key to Users table)
    title
    content
    created_at

Comments Table:

    comment_id (Primary Key)
    user_id (Foreign Key to Users table)
    post_id (Foreign Key to Posts table)
    content
    created_at

Relationships:

    One-to-Many (Users to Posts): A user can create multiple posts, but each post is created by only one user.
    One-to-Many (Posts to Comments): A post can have multiple comments, but each comment is associated with only one post.
    Many-to-One (Users to Comments): A user can create multiple comments, but each comment is created by only one user.


## SCHEMA
-- Users Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts Table
CREATE TABLE Posts (
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Comments Table
CREATE TABLE Comments (
    comment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    post_id INTEGER REFERENCES Posts(post_id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
