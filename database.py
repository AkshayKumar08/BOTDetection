import numpy as np
import MySQLdb
import re
from sklearn.preprocessing import LabelEncoder
import joblib

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="socialnetworking")
    cursor = _conn.cursor()
    return cursor, _conn

# -------------------------------Registration-----------------------------------------------------------------

def user_registration(uname, pword, mail, gender, dob, mobile, adrs):
    try:
        cursor, conn = db_connect()
        iterator = cursor.execute("insert into user(id, name, password, mail, gender, dob, mobile, address) values+" + 
        " ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format('0', uname, pword, mail, gender, dob, mobile, adrs))
        conn.commit()
        conn.close()
        return iterator 
    except Exception as e:
        return(str(e))
        
def bot_check(uname, post):
    b = re.search("(?P<url>https?://[^\s]+)", post).group("url")
    cursor, conn = db_connect()
    cursor.execute("select * from predict where username='{}'".format(uname))
    a, _, c, d, e, f, g, h, i, j, username = cursor.fetchone()
    conn.close()

    df = np.array([a, b, c, d, e, f, g, h, i, j]).reshape(1, -1)

    Labelx=LabelEncoder()
    df[:, 1]=Labelx.fit_transform(df[:, 1])
    df[:, 6]=Labelx.fit_transform(df[:, 6])
    df[:, 8]=Labelx.fit_transform(df[:, 8])
    df[:, 9]=Labelx.fit_transform(df[:, 9])


    model = open("model.pkl", 'rb')
    clf = joblib.load(model)

    cursor, conn = db_connect()
    result = clf.predict(df[[0]])
    output = "this is bot message"
    if result == 0:
        output="this is not a bot message"
    j = cursor.execute("insert into result (username, prediction) values ('{}', '{}')".format(username, output))
    conn.commit()
    conn.close()
    return result

def add_post(uname, post):
    try:
        cursor, conn = db_connect()
        iterator = cursor.execute("insert into post (name, post) values ('{}', '{}')".format(uname, post))
        conn.commit()
        conn.close()
        return iterator
    except Exception as e:
        return(str(e))
 
def friend_request(uname,fname):
    try:
        cursor, conn = db_connect()
        iterator = cursor.execute("insert into frequest(uname, fname, status) values ('{}', '{}', '{}')".format(uname, fname, 'Pending'))
        conn.commit()
        conn.close()
        return iterator
    except Exception as e:
        return(str(e))

def get_users_data():
    cursor, conn = db_connect()
    cursor.execute("select * from user")
    result = cursor.fetchall()
    conn.close()
    return result


def search_friend(friend):
    cursor, conn = db_connect()
    cursor.execute("select * from user where name like '{}'".format(friend))
    result = cursor.fetchall()
    conn.close()
    return result
              
def accept(uname,fname):
    cursor, conn = db_connect()
    iterator = cursor.execute("update frequest set status='{}' where fname='{}'".format("Accepted", uname))
    conn.commit()
    conn.close()
    return iterator

def reject(uname,fname):
    cursor, conn = db_connect()
    iterator = cursor.execute("update frequest set status='{}' where fname='{}'".format("Rejected", uname))
    conn.commit()
    conn.close()
    return iterator

def view_requests(uname):
    cursor, conn = db_connect()
    cursor.execute("select * from frequest where fname='{}'".format(uname))
    result = cursor.fetchall()
    conn.close()
    return result

def view_posts(username):
    cursor, conn = db_connect()
    cursor.execute("select * from post")
    result = cursor.fetchall()
    conn.close()
    return result

def view_predict(username):
    cursor, conn = db_connect()
    cursor.execute("select * from predict")
    result = cursor.fetchall()
    conn.close()
    return result

def analysis(username):
    cursor, conn = db_connect()
    cursor.execute("select * from result")
    result = cursor.fetchall()
    conn.close()
    return result

# # -------------------------------Registration End-----------------------------------------------------------------
# # -------------------------------Login Start-----------------------------------------------------------------

def admin_login(uname, pwd):
    try:
        cursor, conn = db_connect()
        iterator = cursor.execute("select * from admin where username='{}' and password='{}'".format(uname, pwd))
        cursor.fetchall()
        conn.close()
        return iterator
    except Exception as e:
        return(str(e))

def user_login(uname, pwd):
    try:
        cursor, conn = db_connect()
        iterator = cursor.execute("select * from user where username='{}' and password='{}'".format(uname, pwd))
        cursor.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())
