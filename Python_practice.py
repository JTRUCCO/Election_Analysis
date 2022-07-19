from multiprocessing.sharedctypes import Value
from tkinter import scrolledtext

#counties=["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Passo is in the list of counties.")
#else:
   # print("El Paso is not the list of counties.")
#if "Arapahoe" in counties and "El Paso" in counties:
    #print("Arapahoe and El Paso are in the list of counties.")
#else:
    #print("Arapahoe or El Paso is not in the list of counties.")



#counties=["Arapahoe","Denver","Jefferson"]   
#if "Arapahoe" in counties or "El Paso" in counties:
    #print("Arapahoe or El Paso is in the list of counties.")
#else:
    #print("Arapahoe and El Paso are not in the list of counties.")
#if "Arapahoe" in counties and "El Paso" not in counties:
   #print("Only Arapahoe is in the list of counties.")
#else:
    #print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")   


#x=0
#while x<=5:
    #print(x)
    #x=x+1

#counties=["Arapahoe","Denver","Jefferson"]   
#for county in counties:
 #   print(county)

#Output
#Arapahoe
#Denver
#Jefferson

#numbers=[0,1,2,3,4]
#for num in numbers:
 #   print(num)

 #output
#0
#1
#2
#3
#4
#same output 

#for num in range(5):
    #print(num)
#0
#1
#2
#3
#4


#counties=["Arapahoe","Denver","Jefferson"]   
#for i in range(len(counties)):
    #print(counties[i])

#Output
#Arapahoe
#Denver
#Jefferson

#counties_tuple = ("Arapahoe","Denver","Jefferson")

#for i in range(len(counties_tuple)):

    #print(counties_tuple[i])

#Output
#Arapahoe
#Denver
#Jefferson

#counties_tuple = ("Arapahoe","Denver","Jefferson")
#for county in counties_tuple:
    #print(county)
#Output
#Arapahoe
#Denver
#Jefferson


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict:
    #print(county)
#Output
#Arapahoe
#Denver
#Jefferson    

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.keys():
    #print(county)

#Output
#Arapahoe
#Denver
#Jefferson   

#Print each county from the counties dictionary using the keys() method.
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#???

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for voters in counties_dict.values():
    #print(voters)

#output
#422829
#463353
#432438

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict:
    #print(counties_dict[county])

#output
#422829
#463353
#432438

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict:
    #print(counties_dict.get(county))

#output
#422829
#463353
#432438

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county, voters in counties_dict.items():
    #print(county,voters)

#Arapahoe 422829
#Denver 463353
#Jefferson 432438



#??????????????????????????????????????

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                #{"county":"Denver", "registered_voters": 463353},
               #{"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):

      #print(voting_data[i]['county'])


      #???????????????????????????????????????????????????????

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                #{"county":"Denver", "registered_voters": 463353},
                #{"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #for values in county_dict.values():
        #print(values)

#Arapahoe
#422829
#Denver
#463353
#Jefferson
#432438

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                #{"county":"Denver", "registered_voters": 463353},
                #{"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
   #print(county_dict['county'])

#Arapahoe
#Denver
#Jefferson

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#or

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#How many votes did you get in the election? 100
#What is the total votes in the election? 150
#I received 66.66666666666666% of the total votes.

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
 #   print(county + " county has " + str(voters) + " registered voters.")

#or
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters} registered voters.")

#Arapahoe county has 369237 registered voters.
#Denver county has 413229 registered voters.
#Jefferson county has 390222 registered voters.



#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes. "
 #   f"The total number of votes in the election was {total_votes}. "
 #   f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

#How many votes did the candidate get in the election? 5
#What is the total number of votes in the election? 6
#You received 5 number of votes. The total number of votes in the election was 6. You received 83.33333333333334% of the total votes.


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)




























































