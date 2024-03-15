MySQL is an open-source database management system, commonly installed as part of the popular LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack. It implements the relational model and uses Structured Query Language (better known as SQL) to manage its data.

DML statements are used to work with the data in tables. When you are connected to most multi-user databases (whether in a client program or by a connection from a Web page script), you are in effect working with a private copy of your tables that can’t be seen by anyone else until you are finished (or tell the system that you are finished). You have already seen the SELECT statement; it is considered to be part of DML even though it just retreives data rather than modifying it.

DDL statements are used to build and modify the structure of your tables and other objects in the database. When you execute a DDL statement, it takes effect immediately.

The SELECT clause allows us to specify a comma-separated list of attribute names corresponding to the columns that are to be retrieved. You can use an asterisk character, *, to retrieve all the columns.
In queries where all the data is found in one table, the FROM clause is where we specify the name of the table from which to retrieve rows. In other articles we will use it to retrieve rows from multiple tables.
The WHERE clause is used to constrain which rows to retrieve. We do this by specifying a boolean predicate that compares the values of table columns to literal values or to other columns.
The ORDER BY clause gives us a way to order the display of the rows in the result of the statement.
