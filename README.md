# Python Assignment 2
My second python assignment

QUESTION 1 Explained

GET retrieves data from a server without changing anything. Its parameters go in the URL (e.g. ?userId=1), so they appear in browser history and server logs and shouldn't carry sensitive data. It is safe and idempotent, can be cached and bookmarked, and is limited by URL length.

POST sends data in the request body to create a resource or trigger an action. The data is not in the URL and there is no practical size limit, but it still needs HTTPS. It is neither safe nor idempotent, because repeating it may create duplicates.


QUESTION 2 Explained

sqlite3.connect(path) opens the database file, creating it if it doesn't exist, and returns a Connection object that manages transactions.
The cursor (conn.cursor()) executes SQL (execute(), executemany()) and reads results (fetchone(), fetchall()).
commit() permanently saves changes from INSERT, UPDATE, DELETE and CREATE. Without it, changes are lost when the connection closes. SELECT doesn't need it.
rollback() cancels a failed transaction, and close() releases the file.
Use ? placeholders (parameterised queries) to prevent SQL injection.

QUESTION 3 Explained

A list comprehension builds a new list from an iterable in one expression. It is shorter than a loop with append() and usually faster.