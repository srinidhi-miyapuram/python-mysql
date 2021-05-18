import mysql.connector
from mysql.connector import cursor
connect_database = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "company_details")
#making connection with the database
import pandas as pd
mycursor = connect_database.cursor()
mycursor.execute("SELECT TOTAL_EMPLOYEES FROM Company WHERE COUNTRY = 'India'")#executing the query
result = mycursor.fetchall()#fetching the result from the database

final = []#initializing an empty list

#converting the tuple to list
def solution(x,y):
    for i in range(0, len(x), 1):
        y.append(list(x[i]))
solution(result,final)
 
list1 = []
list2 = []

#converting the elements in the list from list to string
def answer(y,z):
    for i in range(0, len(y), 1):
        res = y[i]
        # Function to convert  
        def listToString(y): 
            str1 = "" 
            for ele in res: 
                str1 += str(ele)  
            return str1 
        z.append(listToString(res))
answer(final,list1) #calling the function   

#converting the elements in the list from string to integer
def stringToInt(x,y):
    for i in range(0, len(x), 1):
        y.append(int(x[i]))
stringToInt(list1,list2)    

#adding the elements in the list
summation = sum(list2) 
 

mycursor.execute("SELECT CODE FROM Company WHERE COUNTRY = 'India'")
result1 = mycursor.fetchall()

list3 = []
list4 = []

solution(result1, list3)

answer(list3,list4)


list5 = []
list6 = []
list7 = []

for i in range(0, len(list4), 1):
    res = list4[i]
    mycursor.execute(f"SELECT TOTAL_EMPLOYEES FROM Department WHERE COMPANY_CODE = '{res}'")#executing the query
    result2 = mycursor.fetchall()#fetching the data from the database
    
    solution(result2, list5)
answer(list5, list6)

stringToInt(list6,list7)#calling the function to convert string to integer

summation2 = sum(list7)#adding the elements of the list


total_employees = summation + summation2#adding the total number of employees
print(f"The sum of total employees in the department table and company table, where country is India are {total_employees}")

connect_database.close()#closing the connection with database