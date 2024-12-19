import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
)
print(mydb)

cr_obj=mydb.cursor()

# cr_obj.execute("Create database Employee")

cr_obj.execute("Use Employee")
studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
cr_obj.execute(studentRecord)