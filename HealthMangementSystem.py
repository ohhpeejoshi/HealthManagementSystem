###QUESTION###
# Health Management System
# 3 clients - Harry, Rohan and Hammad

# Use this function
# def getdate():
#     import datetime
#     return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def getdate():
    import datetime
    return datetime.datetime.now()


ret_or_log = int(input("1 for Log, 2 for Retrieve"))
name_id = int(input('1 for Rohan, 2 for Harry, 3 for Hammad'))
ex_or_food = int(input("1 for Exercise, 2 for Food"))
date = getdate()


def locker(id, activity):
    if ex_or_food == 1:
        inp = input("Which exercise ?")
        if name_id == 1:
            file = open('RohanExercise.txt', 'a')
            file.write(str(date) + " " + inp + '\n')
            file.close()

        elif name_id == 2:
            file = open('HarryExercise.txt', 'a')
            file.write(str(date) + " " + inp + '\n')
            file.close()

        elif name_id == 3:
            file = open('HammadExercise.txt', 'a')
            file.write(str(date) + " " + inp + '\n')
            file.close()

        else:
            print("Invalid Input!")

    elif ex_or_food == 2:
        inp = input("What did you eat?")
        if name_id == 1:
            file = open('RohanFood.txt', 'a')
            file.write(str(date) + " " + inp + '\n')
            file.close()

        elif name_id == 2:
            file = open('HarryFood.txt', 'a')
            file.write(str(date) + " " + inp + '\n')
            file.close()

        elif name_id == 3:
            file = open('HammadFood.txt', 'a')
            file.write(str(date) + " " + inp + '\n')
            file.close()
        else:
            print("Invalid Input!")


def retriever(id, activity):
    if ex_or_food == 1:
        if name_id == 1:
            file = open('RohanExercise.txt', 'rt')
            print(file.read())
            file.close()

        elif name_id == 2:
            file = open('HarryExercise.txt', 'rt')
            print(file.read())
            file.close()

        elif name_id == 3:
            file = open('HammadExercise.txt', 'rt')
            print(file.read())
            file.close()

        else:
            print("Invalid Input!")


    elif ex_or_food == 2:
        if name_id == 1:
            file = open('RohanFood.txt', 'rt')
            print(file.read())
            file.close()

        elif name_id == 2:
            file = open('HarryFood.txt', 'rt')
            print(file.read())
            file.close()

        elif name_id == 3:
            file = open('HammadFood.txt', 'rt')
            print(file.read())
            file.close()

        else:
            print("Invalid Input!")


if ret_or_log == 1:
    locker(name_id, ex_or_food)

elif ret_or_log == 2:
    retriever(name_id, ex_or_food)