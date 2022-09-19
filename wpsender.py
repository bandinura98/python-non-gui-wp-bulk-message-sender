import requests
import json
import mysql.connector
import sys
import sqlite3

'''
print("////////////////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////////////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\////////////////////////\//////////////////////////////\/////////")
print("//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////")
'''

print("  __________________________________________")
print("| welcome to the wp message sender basic api |")
print("  ==========================================")
print("                                          \\")
print("                                           \\")
print("                                             ^__^")
print("                                             (oo)\\______")
print("                                             (__)\\       )\\/\\")
print("                                                 ||----w |")
print("                                                 ||     ||")


print("")

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="baba1111"
    )
    #print(mydb)
except:
    print("sql error you need to run initializor.py")


def add_sessions():
    url = 'http://127.0.0.1:8000/sessions/add'

    myobj = {'id': 'john','isLegacy':'false'}

    x = requests.post(url,json=myobj)

    print(x.text)

def sendmsg(number,text):
    url = "http://127.0.0.1:8000/chats/send?id=john"
    
    myobj = {
        "receiver": number,
        "message": 
            {"text": str(text)}
        
    }

    
    print(myobj)
    
    x = requests.post(url,json=myobj)
    
    print(x.text)

def getnums():
    mycursor = mydb.cursor()

    mycursor.execute("use sys")
    mycursor.execute("SELECT num FROM new_table")

    myresult = mycursor.fetchall()

    for num in myresult:
        print(num)
    return myresult

def send_bulk_msg(text):
    nums = getnums()
    for num in nums:
        sendmsg(''.join(num),text)
        print(''.join(num),text)

def send_potho():
    url = "http://127.0.0.1:8000/chats/send?id=john"
    
    myobj = {
        "receiver": "905422607701",
        "message": {
            "image": {
                "url": 'https://w7.pngwing.com/pngs/110/230/png-transparent-whatsapp-application-software-message-icon-whatsapp-logo-whats-app-logo-logo-grass-mobile-phones-thumbnail.png'
            },
        "caption": 'My logo'
        }
    }
    
    print(myobj)
    #https://w7.pngwing.com/pngs/110/230/png-transparent-whatsapp-application-software-message-icon-whatsapp-logo-whats-app-logo-logo-grass-mobile-phones-thumbnail.png
    
    x = requests.post(url,json=myobj)
    
    print(x.text)
def addnum(text):
    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (num) VALUES (%s)"
    val = (str(text))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def main():
    if str(sys.argv[1])=="sendmsg":
    
        number = input('Enter number:')
        
        text = input('Enter message:')
        
        sendmsg(number,text)
        
    if str(sys.argv[1])=="addses":
        add_sessions()
        
    if str(sys.argv[1])=="sendbulk":
        text = input('Enter Message:')
        send_bulk_msg(text)
        
    if str(sys.argv[1])=="addnum":
        print("4")
        
    if str(sys.argv[1])=="sendpotho":
        print("5")
    
    if str(sys.argv[1])=="addnum":
    
        number = input('Enter number:')
        addnum(number)
    
    if str(sys.argv[1])=="help":
        print("sendmsg: sends single message to the number")
        print("addses: adds a session named john")
        print("sendbulk: sends bulk message to the group of numbers")
        print("getnum: get numbers from database")
        print("sendpotho: send message with image")
        print("help: shows this message")
        
    if str(sys.argv[1])!="sendmsg" and str(sys.argv[1])!="addses" and str(sys.argv[1])!="sendbulk" and str(sys.argv[1])!="getnum" and str(sys.argv[1])!="sendpotho" and str(sys.argv[1])!="help" and str(sys.argv[1])=="addnum":
        print("the usage is wrong type")
        print("python wpsender.py help")
        print("for see the required usage")
    #sendmsg("905303988501")
    #add_sessions()
    #send_bulk_msg()
    #getnums()
    #send_potho()
if __name__ == "__main__":
    main()






'''
curl --location -g --request POST '{{base_url}}/chats/send?id=john' \
--data-raw '{
    "receiver": "628231xxxxx", 
    "message": {
        "text": "hello there!"
    }
}'
'''


"""
    input()
    
    match term:
        case 1:
            send_bulk_msg()
        case 2:
             2
        case pattern-3:
             3
        case _:
            print("not valid")
"""
