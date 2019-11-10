# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 01:04:23 2019

Sorts the counties in terms of safety, and then allocates funds for each 
county depending on their safety, and allows the user to see these funds 
per categories such as health insurance

@author: User
"""

import hw5_util

#sorts the counties by safety in terms of deaths per 100,000 people
def sorting(death_list):
    sorted_list = []
    #index is the position in death_list[1]
    index = 0
    total = 0
    #iterates through death_list[1] without going through the last index of death_list[1] which is irrelevant
    while index < (len(death_list[1]) - 1):
        index2 = 1
        #iterates through county's death numbers
        while index2 < len(death_list[1][index]):
            total+=death_list[1][index][index2]
            index2+=1
        #appends tuple with average deaths of all years and county
        sorted_list.append((total/(len(death_list[1][index])-1), death_list[1][index][0]))
        index+=1
        total = 0
    sorted_list.sort()
    names_sorted = []
    #adds the name to the list names_sort
    for x in sorted_list:
        names_sorted.append(x[1])
    return names_sorted

#assigns health insurance per county
def health_insurance(sorted_names):
    total = .2+.4+.6+.8+1
    index = 0
    health_tuples = []
    #all while loops deal with assigning the correct fund to each county in its own 20 percentile
    while index<13:
            fund = 71 * (.2/total) * (1/13)
            health_tuples.append((sorted_names[index], fund))
            index+=1
    index = 13
    while index<26:
            fund = 71 * (.4/total) * (1/13)
            health_tuples.append((sorted_names[index], fund))
            index+=1
    index = 26
    while index<39:
            fund = 71 * (.6/total) * (1/13)
            health_tuples.append((sorted_names[index], fund))
            index+=1
    index = 39
    while index<52:
            fund = 71 * (.8/total) * (1/13)
            health_tuples.append((sorted_names[index], fund))
            index+=1
    index = 52
    while index<65:
            fund = 71 * (1/total) * (1/13)    
            health_tuples.append((sorted_names[index], fund))
            index+=1
    print("\nHealth Insurance Statistics")
    count = 0
    health_tuples.sort()
    #to print every county and the fund assigned to it
    while(count<65):
        print(health_tuples[count][0], ": $" + str(health_tuples[count][1]), "million")
        count+=1

#assigns school aid/special education funds to each county    
def school_aid(sorted_names):
    total = .2+.3+.4+.5+.6
    index = 0
    school_tuples = []
    #all while loops deal with assigning the correct fund to each county in its own 20 percentile
    while index<13:
            fund = 42 * (.2/total) * (1/13)
            school_tuples.append((sorted_names[index], fund))
            index+=1
    index = 13
    while index<26:
            fund = 42 * (.3/total) * (1/13)
            school_tuples.append((sorted_names[index], fund))
            index+=1
    index = 26
    while index<39:
            fund = 42 * (.4/total) * (1/13)
            school_tuples.append((sorted_names[index], fund))
            index+=1
    index = 39
    while index<52:
            fund = 42 * (.5/total) * (1/13)
            school_tuples.append((sorted_names[index], fund))
            index+=1
    index = 52
    while index<65:
            fund = 42 * (.6/total) * (1/13)    
            school_tuples.append((sorted_names[index], fund))
            index+=1
    print("\nSchool Aid/Special Education Statistics")
    count = 0
    school_tuples.sort()
    #to print every county and the fund assigned to it
    while(count<65):
        print(school_tuples[count][0], ": $" + str(school_tuples[count][1]), "million")
        count+=1
        
#assigns social service funds to each county    
def social_service(sorted_names):
    total = .2+.35+.5+.65+.8
    index = 0
    social_tuples = []
    #all while loops deal with assigning the correct fund to each county in its own 20 percentile
    while index<13:
            fund = 33 * (.2/total) * (1/13)
            social_tuples.append((sorted_names[index], fund))
            index+=1
    index = 13
    while index<26:
            fund = 33 * (.35/total) * (1/13)
            social_tuples.append((sorted_names[index], fund))
            index+=1
    index = 26
    while index<39:
            fund = 33 * (.5/total) * (1/13)
            social_tuples.append((sorted_names[index], fund))
            index+=1
    index = 39
    while index<52:
            fund = 33 * (.65/total) * (1/13)
            social_tuples.append((sorted_names[index], fund))   
            index+=1
    index = 52
    while index<65:
            fund = 33 * (.8/total) * (1/13)    
            social_tuples.append((sorted_names[index], fund))
            index+=1
    print("\nSocial Service Statistics")
    count = 0
    social_tuples.sort()
    #to print every county and the fund assigned to it
    while(count<65):
        print(social_tuples[count][0], ": $" + str(social_tuples[count][1]), "million")
        count+=1
    
            

deaths = list(hw5_util.read_deaths_all())
print(sorting(deaths))

print("\nNY State Budgets")

print("You can see the broken up budgets by county for NY State. You can choose from:")
print("\t1. Health Insurance\n\t2. School Aid/Special Education\n\t3. Social Services\n")

#allows user to see which budget they'd like
budget_num = input("\nWhich budget would you like to see? => ").strip()
count = 0
while(count<1):
    if(budget_num == "1" or budget_num == "Health Insurance"):
        health_insurance(sorting(deaths))
        count+=1

    elif(budget_num == "2" or budget_num == "School Aid/Special Education"):
        school_aid(sorting(deaths))
        count+=1
    elif(budget_num == "3" or budget_num == "Social Services"):
        social_service(sorting(deaths))
        count+=1
    else:
        budget_num = input("\nWhich budget would you like to see? => ").strip()
        






    


