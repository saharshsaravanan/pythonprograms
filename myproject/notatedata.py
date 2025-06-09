# Write a program to get the name from the user and print the name as Hello "name". name is dynamic input from user.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import *

@api_view(['GET'])
def get_data(request):
    data = list(YourModel.objects.values())  # Convert QuerySet to list
    return Response(data)


import math

from count import *
# Connect to MySQL Database 'game'
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="game"
)
cursor = conn.cursor()

# Query to Get All HP Values
cursor.execute("SELECT name, max_hp FROM lynel ORDER BY id")
hp_values = cursor.fetchall()
a=[]
# Apply Log Base 1000
print("Lynel HP Values (Log Base 1000 Notation):")
for name, hp in hp_values:
    try:
        num_hp = int(hp)  # Convert VARCHAR to Integer
        log_hp = math.floor (math.log(num_hp, 1000))  # Log base 1000
        b=keep_first_three_digits(num_hp)
        a.append(str(b)+generate_notation(log_hp))
    except ValueError:
        print(f"Skipping invalid HP value: {hp}")
print(a)
# Close Connection
cursor.close()
conn.close()
if register():
    print("Now you can log in!")
    login()