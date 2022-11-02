# fastapi:- which is used to give fast response from server to client and cient to server.

minimalapi using the fastapi to create a crud operations and storing the data into the sqlite3 database.
for this particular fastapi i have used maily
--vscode
--elephant plus for checking the sqlite3 database connections and tables stored in the table or not.

 requirements.txt
 -----------------
 this text file contains the packages whatever is required to implement the fastapi
 
 -fastapi
 -uvicorn
 -sqlalchemy
 
 -fastapi
 fastapi is the library (or) module which contains a large number of functions regariding the implementation of the application
 
 -in fastapi we have :
 get
 post
 put
 delete
 
 we can able perform crud operation by using the above 4 funtions in fastapi
 
 -uvicorn 
 
 which is used to handling the sever and existing port numbers and it will take care of the response of input and output
 
 -sqlalchemy
 
 sqlalchemy which is used to connect with databases like 
 1.sqlite
 2.postgresql
 3.mysql
 4.mssqlserver
 
 in this task i used to sqlite3 database to store the data in the database in the form of tables
 and retreive the data back from the database using commands in fastapi(get)
 
 in this task i have defined the user to blog relationship and blog to user relationship.
 
 
 other libraries i have used in this project is :-
 pydantic
 sqlalchemy.orm
 schemas.py(user defined module)
 database.py(user defined module)
 blog.db(it is actual database to store data.)
 
 ![1](https://user-images.githubusercontent.com/117256454/199418244-d6ac9e62-b183-4f3e-b3b3-c95c910ec8ef.PNG)

 server:- 
 it doesnt have capacity to store the data but it has little bit storage to store the programs which is defiend by (administrator) of the server.
 which is used to manage the requests and responses from client to the database.
 -server means it should contain the ram,cpu,os(automatic machanism),harddisc then only we can called it as a server.
 
 databases:-
 ----------
 1.database mainly explained into 2 types 
 1.1. structured database
 1.2. unstructured database
 
 1.1. structured database
 
 -it is used to store the data in the form of tables which contains rows & columns
 
 1.2. unstructed database
 -it is used to store data in the form json format.
 json :- javascript object notation.
 
 
 based on the above information i have built a crud operation and connecting with sqlite3 databases.
 crud oprations---- fastapi
 server-------------uvicorn
 databases----------sqlite3
 
 
