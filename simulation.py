# Name - Aman Kumar
# Roll No - 2020279
from a2 import *

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''

s = "samesh"
b = "IsaBelLa RaMiRez"
a = read_data_from_file()
dict = {
    0: filter_by_first_name(a),
    1: filter_by_last_name(a),
    3: filter_by_full_name,
    4: filter_by_age_range(a),
    5: count_by_gender(a),
    6: filter_by_address(a),
    7: find_alumni(a)}
'''   
    8:,
    9:,
    10:,
    11:,
    12:,
    13:,
    14:,
    15:,
    16:
'''
while True:
    print("Welcome !!!")
    print("which operation do you wish to perform with data")
    print("1. Filter person id with first name")
    print("2. Filter person id with last name")
    print("3. Filter person id with age range")
    print("3. Filter person with with full name")
    print("3. Filter person with with full name")
    print("3. Filter person with with full name")
    print("3. Filter person with with full name")
    print("enter you choice (1 to 14) ; enter blank to exit")
    x = input()
    if x == "":
        break
    elif int(x) >= 0 and int(x) <= 16:
        x = int(x)
        if x == 1:
            a1 = int(input("enter the first name (case insensitive) for filtering person id"))
            z = filter_by_first_name(a, a1)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)
        elif x == 2:
            a1 = int(input("enter the last name (case insensitive) for filtering person id"))
            z = filter_by_last_name(a, a1)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)
        elif x == 3:
            a1 = int(input("enter the full name (case insensitive) for filtering person id"))
            z = filter_by_full_name(a, a1)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)
        elif x == 4:

            while True:
                a1 = int(input("lower limit of age range"))
                if a1 >= 0:
                    break
                else:
                    print("age must be greater than 0")
            while True:
                a2 = int(input("lower upper of age range"))
                if a2 >= a1:
                    break
                else:
                    print("upper age limit must be greater than or equal to lower age limit")
            z = filter_by_age_range(a, a1, a2)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)

        elif x == 5:
            print("the count of male and females are :")
            print(count_by_gender(a))

        elif x == 6:
            dict = {}
            print("enter the address you wish to search for (enter blank if you don't want to add a field)")
            s1 = input("house_no :")
            if s1 != '':
                dict["house_no"] = s1
            s2 = input("block :")
            if s2 != '':
                dict["block"] = s2
            s3 = input("town :")
            if s3 != '':
                dict["town"] = s3
            s4 = input("city :")
            if s4 != '':
                dict["city"] = s4
            s5 = input("state :")
            if s5 != '':
                dict["state"] = s5
            s6 = input("pincode :")
            if s5 != '':
                dict["pincode"] = s5

            z = filter_by_address(a, dict)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)

        elif x == 7:
            a1 = input("enter the name of uniiversity from which you want records of alumni")
            z = find_alumni(a, a1)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)

        elif x == 8:
            z = find_topper_of_each_institute(a)
            if z == []:
                print("No results found")
            else:
                print("we found the following results")
                print(z)

        elif x == 9:
            a1 = int(input("enter the ID of person who wants to receive blood"))
            z = find_blood_donors(a, a1)
            if z == []:
                print("The receiver doesnot exist")
            else:
                print("the following people are eligible to donate blood")
                print(z)

        elif x == 10:
            print("enter the ids if people for which you want to find common friends (enter blank to exit)")
            while True:
                ids = []
                a1 = input()
                if a1 == "":
                    break
                else:
                    ids.append(int(a1))

            z = get_common_friends(a, ids)
            if z == []:
                print("No common friends found")
            else:
                print("the following are the ids of common friends")
                print(z)

        elif x == 11:
            a1 = int(input("enter the ID of first person"))
            a2 = int(input("enter the ID of second person"))
            z = is_related(a, a1, a2)
            if z == True:
                print("both people are related and are friends directly or indirectly")
            else:
                print("both persons are not related")

        elif x == 12:
            a1 = int(input("enter the id of person you want to delete"))
            z = delete_by_id(a, a1)
            a = z
            print("records updated successfully")

        elif x == 13:
            a1 = int(input("Add the id of first person"))
            a2 = int(input("Add the id of second person you want to add as a friend"))

            z = add_friend(a, a1, a2)
            a = z
            print("Records updated successfully")

        elif x == 14:
            a1 = int(input("Add the id of first person"))
            a2 = int(input("Add the id of second person you want to remove from friend"))

            z = remove_friend(a, a1, a2)
            a = z
            print("Records updated successfully")

        elif x == 15


    else:
        print("please enter correctly")

