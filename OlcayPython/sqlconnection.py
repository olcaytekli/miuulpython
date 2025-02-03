import mysql.connector
from datetime import datetime


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="mysql123",
    database ="schooldb"

)