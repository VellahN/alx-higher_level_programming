MySQL is an open-source relational database management system. It is commonly deployed as part of the LAMP stack (which stands for Linux, Apache, MySQL, and PHP) and, as of this writing, is the most popular open-source database in the world.

We have the following constraints:

NOT NULL
UNIQUE
PRIMARY KEY
FOREIGN KEY
ENUM
SET

The CREATE USER statement creates a user account with no privileges. It means that the user account can log in to the MySQL Server, but cannot do anything such as selecting a database and querying data from tables.

To enable the user account to work with database objects, you need to grant it privileges. You use the GRANT statement to assign one or more privileges to the user account.
