phrase="Hello, World"
type_id=type(phrase)
print(type_id)
name="123"
type_name=type(name)
print(type_name)

string1= 'hello, world'
string2="1234"
string3="we're #1!"
string4='isaidPutitoverbythellama'
print(string1.upper()+"/"+string2+"/" +string3+"/"+string4.lower())
print(string2)
len_id=len(string4)
print(len_id)

string5= "cat   "
print(string5.lstrip())   # by this you can remove space  from left
print(string5.strip())  # by this you can remove space from both side
print(string5.rstrip())  # by this you can remove space from right side

import calendar
yy= 2024
mm=4
print(calendar.month(yy,mm))

'''import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRTSUVWXYZ"
numbers="0123456789"
symbols="!@#$%^&*()_+?<>["
all_chars=lower+ upper+numbers+symbols
length=int(input("Enter a length: "))
password=''.join(random.sample(all_chars,length))
print("Generated Password:",password)'''

#Use of if and else fucntion#
myname="don"
if myname=="don" :
    print("Yes the name is correct ")
    print("Correct name")
else:print("NO invalid name")

'''Value=int(input("Type a number between 1 and 10:"))
if (Value >0) and (Value <=10):
    print("You typed right:", Value)
else:print('Wrong plz type a valid range of numbers')'''

print("1. Red")
print("2. orange")
print("3. Yellow")
print("4. Green")
print("5. Blue")
print("6. Purple")

"""Choice=int(input("Select your favrt color:"))
if (Choice==1):
    print("You have chose Red")
elif(Choice==2):
    print("You have chose orange!")
elif (Choice == 3):
    print("you have chose Yellow")
elif (Choice == 4):
    print("you have chose Green")
elif(Choice==5):
    print("you have chose Blue")
elif(Choice==6):
    print("you have chose Purple")
else:print("You made an invalid choice!")"""

a=9
b=10
a,b=b,a     # by this we can swap variable in python
print(a)
print(b)

'''print("1. HMT")
print("2. QMR")
print("3. BAT")
print("4. LAL")
print("5. DAL")
station=int(input("From this station :"))

if(station ==1):
    print("You are traveling from HMT and fare is 10rs")
elif(station ==2):
    print("you are traveling from QMR and fare is 8rs")
else:print("We are not servicing yet from this station")'''


# Define a dictionary to map station names to their distances from a reference point (e.g., the starting station)
'''station_distances = {
    "QMR": 0,
    "BMT": 2,
    "LAL": 4,
    "DAL": 7,
    "NAT": 10,
}
# Define a function to calculate the ticket price based on the distance between two stations
def calculate_ticket_price(station_from, station_to):
    # Get the distances of the departure and arrival stations
    distance_from = station_distances[station_from]
    distance_to = station_distances[station_to]

    # Calculate the absolute distance between the stations
    distance = abs(distance_to - distance_from)

    # Define a basic fare structure (e.g., 4 currency units per kilometer)
    price_per_km = 4

    # Calculate the price
    ticket_price = distance * price_per_km

    return ticket_price


# Example of usage
station_from = input("Enter the departure station: ")
station_to = input("Enter the destination station: ")

# Calculate the price of the ticket
ticket_price = calculate_ticket_price(station_from, station_to)

print(f"The ticket price from {station_from} to {station_to} is: {ticket_price} Rs.")'''

