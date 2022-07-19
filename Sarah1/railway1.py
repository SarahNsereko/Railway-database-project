from cs50 import SQL
import csv

open("railway.db","w").close() 

db = SQL("sqlite:///railway.db")
db.execute ("CREATE TABLE Passenger(passenger_id INTEGER PRIMARY KEY AUTOINCREMENT ,passenger_name TEXT,age INTEGER, bags INTEGER , seats INTEGER, amount INTEGER );")
db.execute("CREATE TABLE Train(train_id INTEGER PRIMARY KEY AUTOINCREMENT,train_no INTEGER, train_name TEXT, destination TEXT, setoff_time TEXT,arrival_time TEXT);")
db.execute("CREATE TABLE Stations(station_id INTEGER PRIMARY KEY AUTOINCREMENT , station_no INTEGER,station_name TEXT, station_location TEXT);")
db.execute("CREATE TABLE Tickets(ticket_no INTEGER PRIMARY KEY AUTOINCREMENT ,issue_date TEXT,passenger_id INTEGER , train_id INTEGER, station_id INTEGER ,FOREIGN KEY (passenger_id) REFERENCES Passenger(passenger_id), FOREIGN KEY (train_id) REFERENCES Train(train_id),FOREIGN KEY (station_id) REFERENCES Stations(station_id));")

with open("Railway csv database 1.csv", "r") as file:
    reader=csv.DictReader(file)

    for row in reader:
       
        pass_name=row["Passenger_name"]
        seat=row["Seats"]
        bag=row["Bags"]
        age=row["Age"]
        ticket=row["Ticket_no"]
        date=row["Issue_date"]
        arrival=row["Arrival_time"]
        setoff=row["Setoff_time"]
        amount=row["Amount"]
        train_no=row["Train_no"]
        
        train_name=row["Train_name"]
       
        station_name=row["Station_name"]
        station_no=row["Station_no"]
        station_location=row["Station_location"]
        destination=row["Destination"]
        
        Ids = db.execute("INSERT INTO Passenger(passenger_name,age,bags,seats,amount) VALUES (?,?,?,?,?);", pass_name,age,bag,seat,amount)
        trai=db.execute("INSERT INTO Train(train_no,train_name,destination,setoff_time,arrival_time) VALUES (?,?,?,?,?);",train_no,train_name,destination,setoff,arrival)
        stai=db.execute("INSERT INTO Stations(station_no, station_name,station_location) VALUES (?,?,?);",station_no,station_name,station_location)
        db.execute("INSERT INTO Tickets(issue_date,passenger_id,train_id,station_id) VALUES (?,(SELECT passenger_id FROM Passenger WHERE passenger_id = ?),(SELECT train_id FROM Train WHERE train_id=?),(SELECT station_id FROM Stations WHERE station_id=?));",date,Ids,trai,stai)
        
        
        
         
  
  