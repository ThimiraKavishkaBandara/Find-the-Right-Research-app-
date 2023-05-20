import pymysql
from neo4j import GraphDatabase



def add_university(university):
    # Connect to MySQL database
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2107",   #2107
        database="academicworld"
    )
    cursor = db.cursor()
    sql = "INSERT INTO favorite_university (name) VALUES (%s)"
    val = (university,)
    try:
        cursor.execute(sql, val)
        db.commit()
        print("University added successfully")
    except pymysql.err.OperationalError as e:
        if e.args[0] == 3819:
            print("Error: University name must contain 'university' or 'institute'")
        else:
            print("Error: " + str(e))
    finally:
        db.close()

    #get name from databse
    #connect to neo4j
    driver = GraphDatabase.driver("bolt://127.0.0.1:7687", auth=("neo4j", "12345678"), encrypted=False, database="academicworld")   #12345678
    with driver.session() as session:  
        result = session.run(f"""
            MATCH (u:INSTITUTE) WHERE u.name CONTAINS '{university}' RETURN u.name
        """)
        return [record["u.name"] for record in result]


def delete_university(university):
    # Connect to database
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2107",
        database="academicworld"
    )
    cursor = db.cursor()
    query = "DELETE FROM favorite_university WHERE name LIKE %s"
    university_pattern = f"%{university}%"
    try:
        result = cursor.execute(query, (university_pattern,))
        db.commit()
        #print(result)
    except Exception as e:
        print(e)
        db.rollback()
    cursor.close()
    db.close()



print(add_university("Harvard"))


def widget_4_query(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2107",
        database="academicworld"
    )
    cursor = db.cursor()
    query = ("select p.title from publication p\
            join faculty_publication fp on p.id=fp.publication_id\
            join faculty f on f.id=fp.faculty_id \
             where f.name like %s")

    pattern = f"%{name}%"
  
    cursor.execute(query, (pattern,))
    
    lst=[]
    lst=["** "+elm[0] for elm in cursor]
       
    db.commit()
    db.close()
    return lst



def widget_5_query(keyword):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2107",
        database="academicworld"
    )
    cursor = db.cursor()
    query="select u.name ,count(distinct f.id) as count from  university u\
    join faculty f on u.id=f.university_id \
    join faculty_keyword fk  on faculty_id= f.id\
    join keyword k on k.id=fk.keyword_id\
    where k.name like %s\
    group by u.id\
    order by count(u.name) DESC\
    limit 5;"
    pattern = f"%{keyword}%"
  
    cursor.execute(query, (pattern,))
    db.commit()
    db.close()
    x=[]
    y=[]
    for elm in cursor:
        x.append(elm[0])
        y.append(elm[1])
    
    return {'university':x,'count':y} 

def widget_6_query(faculty):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2107",
        database="academicworld"
    )
    cursor = db.cursor()
    query = ("CALL get_faculty( %s)")

    pattern = f"%{faculty}%"
  
    cursor.execute(query, (pattern,))
    for elm in cursor:
        if len(elm)>0:
            return True
        else:
            return False
def add_faculty(faculty):
    db = pymysql.connect(
        host="127.0.0.1",   #127.0.0.1
        user="root",
        password="2107",
        database="academicworld"
    )
    cursor = db.cursor()
    query = ("INSERT INTO favorite_faculty (name) VALUES (%s)")
    cursor.execute(query, (faculty,))
    db.commit()
    db.close()
    

def remove_faculty(faculty):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2107",
        database="academicworld"
    )
    cursor = db.cursor()
    query = ("delete from favorite_faculty\
            where name like %s")

    pattern = f"%{faculty}%"
  
    cursor.execute(query, (pattern,))
    db.commit()
    db.close()
    
