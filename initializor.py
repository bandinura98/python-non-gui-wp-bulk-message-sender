import mysql.connector




f = open("db.ini", "r")
readedval = f.read()



#readedval = readedval.split("=")
readedval = readedval.split("\n")


ourlist = [""]

for x in readedval:
    x = x.split("=")
    print(x[1])
    ourlist.append(x[1])
print(ourlist)



try:
    mydb = mysql.connector.connect(
      host=ourlist[1],
      user=ourlist[2],
      password=ourlist[3]
    )
    #print(mydb)
except:
    print("sql error you need to run initializor.py")



mycursor = mydb.cursor()

mycursor.execute("use sys")
mycursor.execute("CREATE TABLE `new_table` (`num` varchar(22) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")


myresult = mycursor.fetchall()
