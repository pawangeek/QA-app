# QA-app

## Learnings

* Work with sqlite3 data
* Migrate sqlite to postgres
* Deployment on heroku

## Difference between Sqlite3 and postgresql

* Change autoincrement(sqlite3) with serial(postgresql) in schema
* Change '?' for query with '%s'
* Change [dict_values] with (tuple,)
* Change if user[expert]=1 to if user[expert] or if user[expert] = True

### Connection in sqlite

* db = get_db()
* user_cur = db.execute('select id, name, password, admin, expert from users where name = ?', [user])
* user_result = user_cur.fetchone()

### Connection in postgresql

* db = get_db()
* db.execute('select id, name, password, admin, expert from users where name = %s', (user,))
* user_result = db.fetchone()

 