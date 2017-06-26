"""sqlite database"""
import sqlite3


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except ValueError as err:
        print(err)
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        qwe = conn.cursor()
        qwe.execute(create_table_sql)
    except ValueError as err:
        print(err)

def getTables():
   #Get a list of all tables
   conn = create_connection("gym_data.db")
   cursor = conn.cursor()
   cmd = "SELECT name FROM sqlite_master WHERE type='table'"
   cursor.execute(cmd)
   names = [row[0] for row in cursor.fetchall()]
   return names

def get_dworkouts(exercise):
    #gets all the logged workouts of a specific exercise by date in descending order
    conn = create_connection("gym_data.db")
    with conn:
        cursor = conn.cursor()
        cmd = """SELECT * FROM """ + exercise + """ ORDER BY date DESC"""
        cursor.execute(cmd)
        return cursor.fetchall()

def get_wworkouts(exercise):
    #gets all the logged workouts of a specific exercise by weight in descending order
    conn = create_connection("gym_data.db")
    with conn:
        cursor = conn.cursor()
        cmd = """SELECT * FROM """ + exercise + """ ORDER BY weight DESC"""
        cursor.execute(cmd)
        return cursor.fetchall()

def insert_exercise(conn, exercise, strn):
    """
    Log an exercise into the appropriate exercise table
    :param conn:
    :param exercise:
    :param strn: name of exercise
    :return: exercise id
    insert here a way to search through all exercises to check
    if creation of new table is needed"""
    sql = """INSERT INTO """ + strn + """(date, weight, sets, reps)
              VALUES(?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, exercise)
    return cur.lastrowid

def insert_overall(conn, overall):
    """
    Log overall exercise into overall table
    :param conn:
    :param overall:
    :return: overall id
    """
    sql = """INSERT INTO overall(exercise, date, recent_weight, recent_sets,
              recent_reps, max_weight, max_sets, max_reps)
              VALUES(?,?,?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, overall)
    conn.commit()
    return cur.lastrowid

def create_string(exercise):
    """
    Creates the necessary SQLite string for creating a new table
    used in create_exercise
    """
    return """CREATE TABLE IF NOT EXISTS """ + exercise + """ (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

def create_exercise(exercise):
    """
    Opens a new connection to the database and creates a table
    for the exercise. also adds the exercise to the overall table.
    """
    conn = create_connection("gym_data.db")
    if conn is not None:
        #tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='spwords'"
        #if not conn.execute(tb_exists).fetchone():
        create_table(conn, create_string(exercise.lower().replace(" ", "_")))
        #else:
        #return False
    with conn:
        insert_overall(conn, (exercise, None, None, None, None
                                , None, None, None))
    conn.close()
    #return True

def table_max(exercise):
    #returns max weight data of exercise
    conn = create_connection("gym_data.db")
    if conn is not None:
        query = """SELECT * FROM """ + exercise + """ ORDER BY weight DESC LIMIT 1"""
        cur = conn.cursor()
        max = cur.execute(query).fetchone()
        conn.close()
        return max
    conn.close()

def table_recent(exercise):
    #returns most recent data of exercise
    conn = create_connection("gym_data.db")
    if conn is not None:
        query = """SELECT * FROM """ + exercise + """ ORDER BY date DESC LIMIT 1"""
        cur = conn.cursor()
        recent = cur.execute(query).fetchone()
        conn.close()
        return recent
    conn.close()

def log_ex(exercise, strn):
    #creates a connection to the database and logs the appropriate exercise
    conn = create_connection("gym_data.db")
    with conn:
        insert_exercise(conn, exercise, strn)
    conn.close()

def initialize():
    #sets up basic settings if program has not been run before
    database = "gym_data.db"
    sql_create_overall_table = """CREATE TABLE IF NOT EXISTS overall (
                                    exercise text PRIMARY KEY,
                                    date text,
                                    recent_weight integer,
                                    recent_sets integer,
                                    recent_reps integer,
                                    max_weight integer,
                                    max_sets integer,
                                    max_reps integer
                                );"""

    sql_create_bench_table = """CREATE TABLE IF NOT EXISTS bench (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

    sql_create_squat_table = """CREATE TABLE IF NOT EXISTS squat (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

    sql_create_deadlift_table = """CREATE TABLE IF NOT EXISTS deadlift (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

    conn = create_connection(database)
    """if conn is not None:
        # create projects table
        create_table(conn, sql_create_overall_table)
        # create bench table
        create_table(conn, sql_create_bench_table)
        # create squat table
        create_table(conn, sql_create_squat_table)
        # create deadlift table
        create_table(conn, sql_create_deadlift_table)
    else:
        print("Error! cannot create the database connection.")"""
    create_table(conn, sql_create_overall_table)
    create_exercise('bench')
    create_exercise('squat')
    create_exercise('deadlift')


    conn.close()

def get_exercises():
    #returns a set of all exercise names stored
    conn = create_connection("gym_data.db")
    c = conn.cursor()
    s = set()
    for ex in c.execute('SELECT * FROM overall ORDER BY exercise DESC'):
        s.add(ex[0])
    conn.close()
    return s



def main():
    """main function meant for testing"""
    database = "gym_data.db"
    sql_create_overall_table = """CREATE TABLE IF NOT EXISTS overall (
                                    exercise text PRIMARY KEY,
                                    date text,
                                    recent_weight integer,
                                    recent_sets integer,
                                    recent_reps integer,
                                    max_weight integer,
                                    max_sets integer,
                                    max_reps integer
                                );"""

    sql_create_bench_table = """CREATE TABLE IF NOT EXISTS bench (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

    sql_create_squat_table = """CREATE TABLE IF NOT EXISTS squat (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

    sql_create_deadlift_table = """CREATE TABLE IF NOT EXISTS deadlift (
                                    date text,
                                    weight integer,
                                    sets integer,
                                    reps integer
                                );"""

    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_overall_table)
        # create bench table
        create_table(conn, sql_create_bench_table)
        # create squat table
        create_table(conn, sql_create_squat_table)
        # create deadlift table
        create_table(conn, sql_create_deadlift_table)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        test_o = ('bench', '2017-06-10', 1, 1, 1, 1, 1, 1)
        test_b = ('2017-06-12', 1, 1, 1)
        test_s = ('2017-06-10', 1, 1, 1)
        test_d = ('2017-06-10', 1, 1, 1)
        """insert_overall(conn, test_o)"""
        insert_exercise(conn, test_b, 'bench')
        insert_exercise(conn, test_s, 'squat')
        insert_exercise(conn, test_d, 'deadlift')
        

    conn.close()
    # test create_exercise('bicep curl')
    print(table_max('bench'))
    print(table_recent('bench'))


if __name__ == '__main__':
    main()
