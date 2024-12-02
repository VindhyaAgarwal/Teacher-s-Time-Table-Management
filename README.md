## Teacher Timetable Management System

#### This Python script manages the creation, display, update, and deletion of teachers' timetables for a week. It uses a MySQL database to store and retrieve data for each day.

## *Features*

### Timetable Creation :
Allows the entry of class schedules for each teacher for the entire week.

### Display: 
Shows the timetable for a specific day or the entire week for a teacher.
### Search : 
Retrieves details of a teacher's schedule using their unique code.
### Update: 
Modifies the existing timetable entries for a particular day or specific period.
### Delete:
Removes all timetable data for a teacher.
### Prerequisites
#### 1. Python 3.x
#### 2. MySQL Database
#### 3. MySQL Connector Library for Python Install using:

```bash 
pip install mysql-connector-python
```

### Setup
#### 1. Database Configuration:
- Create a MySQL database named ```TIMETABLE```.

- Grant access to a user with a ```username``` and ```password``` (used in the script).

#### 2. Tables:

- The script automatically creates tables for each weekday (```MONDAY```, ```TUESDAY```, etc.) when running the ```create``` function.

#### 3. Connection:

- Modify the connection parameters in the ```mysql.connect``` calls within the script to reflect your MySQL setup.

### How to Run
1. Open a terminal or command prompt.

2. Run the script:

```bash
python "Teacher's Time Table.py"
```
3. Input your MySQL credentials when prompted.

### Functions Overview
1. ``` create(user, password):```

- Prompts for a teacher's details and timetable for all days.
- Inserts the data into the database.
 
2. ```display(user, password):```

- Lists all teachers in the system with their code, name, and subject.

3. ``` search_data(user, password):```

- Retrieves a teacher's timetable using their code.
- Option to view a specific day's schedule or the entire week.
  
4. ``` update_data(user, password):```

- Updates specific periods or days in a teacher's timetable.
  
5. ```delete_data(user, password):```
- Deletes a teacher's timetable using their unique code.
  
## Example Usage
### Create a Timetable
``` bash
create('root', 'password123')
```
### Display Teachers
``` bash
display('root', 'password123')
```
### Search for a Teacher's Timetable
``` bash
search_data('root', 'password123')
```

### Update Timetable
``` bash
update_data('root', 'password123')
```

### Delete Timetable
```bash
delete_data('root', 'password123')
```

### Notes
- Enter "Null" for any period if you don't want to add a value.
- Ensure your MySQL server is running before using the script.
 


