lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer():
    def __init__(self, name, numb):
        self.name = name
        self.numbers = numb

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf",(5, 9, 12, 3, 1, 21))
player_two = LotteryPlayer("James",(5, 9, 12, 3, 1, 21))
#print(player_one.name)
#print(player_two.name)
#print(player_one.numbers == player_two.numbers)


##
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod #does not need to be called by an initialized instance/object of the Student class
    def class_go_to_school(cls):
        print("I'm going to school class.")
        print("I'm a {}".format(cls))

    @staticmethod #does not need to be called by an initialized instance/object of the Student class
    def static_go_to_school():
        print("I'm going to school static.")

    def go_to_school(self):
        print("I'm going to {}.".format(self.school))


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())
anna.go_to_school()
Student.class_go_to_school()
Student.static_go_to_school()