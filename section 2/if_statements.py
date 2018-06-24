should_continue = True
if should_continue:
    print("Hello")
"""
known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know:")

if person in known_people:
    print("You know {}!".format(person)) #format this string, but replacing curly braces with the argument
else:
    print("You don't know {} :(".format(person))
"""
#Exercise

def who_do_you_know():
    #Ask user for a list of people they know
    #return input("Enter a list of people you know as a single line, separated by a space: ").split(' ')
    return [person.strip().lower() for person in input("Enter the names of the people you know: ").split(',')]
    #Split the string into a list
    #Return that list


def ask_user():
    #Ask user for a name
    list = who_do_you_know()
    name = input("Enter a name: ")
    print(list)
    if name.strip().lower() in list:
        print("You know {}!".format(name))
    #See if their name is in a list of people they know
    #Print out that know the person

ask_user()