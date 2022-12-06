import math
def round_up(n, decimals =0):
    multiplier = 10 **decimals
    return math.ceil(n * multiplier/multiplier)
print("*****LONG-DISTANCE CALL*****\n1. AMERICAN REGION\n2. ASIAN REGION\n3. AFRICAN REGION\n4. EUROPEAN REGION")
region = int(input("INPUT DESTINATION CODE: "))
if(region == 1):
    print("\n*****AMERICAN REGION*****")
    dayCode = input("X FOR WEEKDAYS\nY FOR WEEKENDS\nSELECT DAY CODE(X/Y): ")
    if(dayCode == "X" or dayCode == "x"):
        print("\n***WEEKDAYS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P50 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 50 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("\n***NIGHT TIME***")
            call = int(input("(Price P45 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 45 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        else:
            print("\nINVALID!")
    elif(dayCode == "Y" or dayCode == "y"):
        print("\n***WEEKENDS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P40 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 40 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("***\nNIGHT TIME***")
            call = int(input("(Price P38 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 38 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        else:
            print("\nINVALID!")
    else:
        print("\nINVALID!\nPLEASE INPUT DAY CODE")

elif(region == 2):
    print("\n*****ASIAN REGION*****")
    dayCode = input("X FOR WEEKDAYS\nY FOR WEEKENDS\nSELECT DAY CODE(X/Y): ")
    if(dayCode == "X" or dayCode == "x"):
        print("\n***WEEKDAYS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P30 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 30 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("\n***NIGHT TIME***")
            call = int(input("(Price P27 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 27 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        else:
            print("\nINVALID!")
    elif(dayCode == "Y" or dayCode == "y"):
        print("\n***WEEKENDS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P25 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 25 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("***\nNIGHT TIME***")
            call = int(input("(Price P15 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 15 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        else:
            print("\nINVALID!")
    else:
        print("\nINVALID!\nPLEASE INPUT DAY CODE")

elif(region == 3):
    print("\n*****AFRICAN REGION*****")
    dayCode = input("X FOR WEEKDAYS\nY FOR WEEKENDS\nSELECT DAY CODE(X/Y): ")
    if(dayCode == "X" or dayCode == "x"):
        print("\n***WEEKDAYS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P40 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 40 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("\n***NIGHT TIME***")
            call = int(input("(Price P36 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 36 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        else:
            print("\nINVALID!")
    elif(dayCode == "Y" or dayCode == "y"):
        print("\n***WEEKENDS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P35 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 35 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("***\nNIGHT TIME***")
            call = int(input("(Price P22 per 3 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 22 * round_up(call/3)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        else:
            print("\nINVALID!")
    else:
        print("\nINVALID!\nPLEASE INPUT DAY CODE")

elif(region == 4):
    print("\n*****ASIAN REGION*****")
    dayCode = input("X FOR WEEKDAYS\nY FOR WEEKENDS\nSELECT DAY CODE(X/Y): ")
    if(dayCode == "X" or dayCode == "x"):
        print("\n***WEEKDAYS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P35 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 35 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("\n***NIGHT TIME***")
            call = int(input("(Price P30 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 30 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<<")
        else:
            print("\nINVALID!")
    elif(dayCode == "Y" or dayCode == "y"):
        print("\n***WEEKENDS***")
        timeCode = input("A FOR DAY\nB FOR NIGHT\nSELECT TIME CODE(A/B): ")
        if(timeCode == "A" or timeCode == "a"):
            print("\n***DAY TIME***")
            call = int(input("(Price P20 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 20 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        elif(timeCode == "B" or timeCode == "b"):
            print("***\nNIGHT TIME***")
            call = int(input("(Price P19 per 2 mins)\nINPUT DURATION OF CALL(minute/s): "))
            total = 19 * round_up(call/2)
            print("\n>>>>>>>>>TOTAL CHARGES: ",total,"P<<<<<<<<")
        else:
            print("\nINVALID!")
    else:
        print("\nINVALID!\nPLEASE INPUT DAY CODE")
else:
    print("\nINVALID!\nPLEASE INPUT DESTINATION")

