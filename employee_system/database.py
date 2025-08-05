import mysql.connector


def get_connection():

    return mysql.connector.connect(
        host = '',
        user = '',
        passwd = '',
        database = '',
        use_pure = True,

    )




def watcher(username,password):
    
    conn = get_connection()

    if not conn:
        print("error in connection")
        
    cursor = conn.cursor()
    query = 'select * from data WHERE username =%s and pass = %s ;'

    cursor.execute(query,(username,password))
    x = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if username == x[0] and password == x[1]:
        
        return True

    else:
        return False

    
    


def insertion(username,password):
    conn = get_connection()

    if not conn:
        print("problem in connection")



    cursor = conn.cursor()    
    query = 'INSERT INTO emplyoee.data VALUES(%s,%s)'
    values = (username,password)

    cursor.execute(query,values)
    conn.commit()
    print("sucess")
    cursor.close()
    conn.close()

    return True