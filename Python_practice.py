from ast import If
import os
from tkinter.messagebox import YES
counties = [ "Arapahoe", "Denver", "Jefferson"]
print (counties)
print (counties [0])
print (counties [2])
print (counties [-2])
print (counties [-1])
print (len(counties))
print (counties[0:2])
print (counties [:2])
counties.append("El Paso")
print(counties)
counties.insert (2, "El Paso")
print (counties)
counties.remove("El Paso")
print (counties)
counties.pop(3)
'El Paso'
counties[2] = "El Paso"
print (counties)
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print (counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print (counties_dict)
len(counties_dict)
print (counties_dict.items)
print (counties_dict.values)
print (counties_dict.get("Denver"))
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print (voting_data)

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
dir(csv)
