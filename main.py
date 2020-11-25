
#importing modules
import time
import random
import re
import _sqlite3

#defining variables
students_information = []
lecture_list = []
admin = "yağızkiremitci"
admin_password = "Kiremitci.yagiz98"
con = _sqlite3.connect("ögrenci_sistemi.db")
cursor = con.cursor()

#defining student class
class Student:

    def create_student(self, name, surname, password):
        self.name = name
        self.surname = surname
        self.identity = str(random.randint(1000000, 9999999))
        self.credit = 40
        self.password = password
        self.lectures = []
        student_information = {"name": self.name, "surname": self.surname, "identity": self.identity,
                               "password": self.password, "lectures": self.lectures, "credit": self.credit}
        students_information.append(student_information)
        student.add_student_to_table(self.name, self.surname, self.identity, self.credit, self.password)
# SQL database codes
    def create_student_table(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(name TEXT, surname TEXT, identity TEXT, password TEXT"
                       ",credit INT, lectures LIST )")

    def add_student_to_table(self, name, surname, identity, credit, password):
        cursor.execute("INSERT INTO ogrenciler(name, surname, identity, password, credit)"
                       "VALUES(?,?,?,?,?)", (name, surname, identity, password, credit))
        con.commit()

    def remove_student_from_table(self, name, surname, identity, credit, password):
        cursor.execute("DELETE FROM ogrenciler VALUES(name, surname, identity, credit, password)"
                       "VALUES(?,?,?,?,?,?)", (name, surname, identity, credit, password))
        con.commit()


    def welcome_screen(self, index):
        str = ("------------------------------------\n"
               "------WELCOME {name}\t{surname}-----\n"
               "   Chose Operation                  \n"
               "****\n"
               "[1] Show student information        \n"
               "[2] Show lecture list               \n"
               "[3] Add/Drop                        \n"
               "[Q] Quit"
               "".format_map(students_information[index]))
        return str


    def add_drop_screen(self):

        print("[1] Add\n"
              "[2] Drop\n"
              "[Q] Quit")

    def add_lecture_control(self):
        if student.is_there_any_lecture_in_lecture_list():
            print(lecture_list)
            print("Welcome to the add lecture part...")
            lecture = input("Type the code of lecture you want to add")
            for i in range(0, len(lecture_list)):
                if lecture.upper() == lecture_list[i]["Lecture"]:
                    return i

    def student_remove_lecture_control(self, index):
        print("Your lectures")
        print(students_information[index]["lectures"])
        print("Please type the code of lecture that you want to remove")
        lecture = input()
        for i in range(0, len(lecture_list)):
            if lecture.upper() == lecture_list[i]["Lecture"]:
                return i

    def add_lecture(self, index, i):
        for lecture in students_information[index]["lectures"]:
            if lecture == lecture_list[i]["Lecture"]:
                return True

    def add_lecture_last(self, index, i):
        students_information[index]["lectures"].append(lecture_list[i]["Lecture"])
        students_information[index]["credit"] -= lecture_list[i]["Credit"]
        print("Operation Completed...")

    def remove_lecture(self, index: int, i):

        students_information[index]["lectures"].remove(lecture_list[i]["Lecture"])
        students_information[index]["credit"] += lecture_list[i]["Credit"]
        print("Operation completed...")

    def is_there_any_lecture_in_lecture_list(self):
        if bool(lecture_list):
            return True
        else:
            print("There are no lecture yet")

    def is_there_any_lecture_in_student_lecture_list(self, index):
        if bool(students_information[index]["lectures"]):
            return True
        else:
            print("Your lectures list is empty")

    def student_credit_info(self, index):
        print("You have {} credit".format(students_information[index]["credit"]))

    def is_there_anyone_students_list(self):
        if not bool(students_information):
            print("There are no one in students list")
        else:
            return True

    def student_entrance(self, name, surname, password):
        for i in range(0, len(students_information)):
            if name == students_information[i]["name"]:
                for j in range(0, len(students_information)):
                    if surname == students_information[j]["surname"]:
                        for k in range(0, len(students_information)):
                            if password == students_information[k]["password"]:
                                if i == j and i == k and k == j:
                                    return i

    def student_choose_lecture(self):
        print(lecture_list)
        print("Welcome to the add lecture part...")

    def student_remove_lecture(self):

        print(lecture_list)
        print("Welcome to the remove lecture part...")

# defining manager class


class Manager:
    def int(self):
        self.admin = "yağız kiremitci"
        self.admin_password = "Kiremitci.yagiz98"

    def management_screen(self):
        print("Welcome {}\t*\n"
              "choose your operation\n"
              "[1] Show Lists\n"
              "[2] Add/Remove Operations\n"
              "[3] Add/Remove Lectures\n"
              "[Q] Quit".format(admin))

    def management_lists_screen(self):
        print("[1] Show Student List\n"
              "[2] Show lecture List\n"
              "[Q] Quit")


    def student_add_remove(self):
        print("[1] Add Student\n"
              "[2] Remove Student\n"
              "[Q] Quit")


    def management_add_and_remove_operations_lecture_screen(self):
        print("[1] Add Lecture\n"
              "[2] Remove Lecture\n"
              "[3] Delete Lecture List\n"
              "[4] Delete Student List\n"
              "[Q] Quit")

    def management_show_students(self):
        if bool(students_information):
            print(students_information)
        else:
            print("There are no students")


    def management_show_lectures(self):
        if bool(lecture_list):
            print(lecture_list)
        else:
            print("There are no lectures")

    def management_add_lecture(self):
        lecture_name = input("Lecture Name:")
        if lecture_name != "":
            credit = int(input("Credit:"))
            if credit != "":
                if credit > 8:
                    print("Lectures' credit can be 8 maximum")
                else:
                    lecture_department = input("Department:")
                    if lecture_department != "":
                        lecture = {"Id": random.randint(0, 1000), "Lecture": lecture_name.upper(), "Credit": credit,
                                   "Department": lecture_department.upper()}
                        lecture_list.append(lecture)
                        time.sleep(0.2)
                    else:
                        fill_all_info()
            else:
                fill_all_info()
        else:
            fill_all_info()

    def management_remove_lecture(self):
        if bool(lecture_list):
            remove_lecture = input("Code of Lecture You Want To Remove:")
            if remove_lecture != "":
                for i in range(0, len(lecture_list)):
                    if lecture_list[i]["Lecture"] == remove_lecture.title():
                        lecture_list.pop(i)
                        time.sleep(0.2)
                        return True
            else:
                fill_all_info()
        else:
            print("There are no lectures")

    def management_delete_student_list(self):
        del students_information
        time.sleep(0.2)


    def management_delete_lecture_list(self):
        del lecture_list
        time.sleep(0.2)

    def add_student(self):
        name = input("Name:")
        if name != "":
            surname = input("Surname:")
            if surname != "":
                password = input("Password:")
                if password != "":
                    for i in range(0, len(students_information)):
                        if name == students_information[i]["name"]:
                            for j in range(0, len(students_information)):
                                if surname == students_information[j]["surname"]:
                                    for k in range(0, len(students_information)):
                                        if password == students_information[k]["password"]:
                                            if i == k and i == j and k == j:
                                                student.create_student(name, surname, password)

                else:
                    fill_all_info()
            else:
                fill_all_info()
        else:
            fill_all_info()

    def remove_student(self):
        identity = input("Please write identity of student")
        if identity != "":
            for i in range(0, len(students_information)):
                if students_information[i]["identity"] == identity:
                    selection = input("Are you sure that you want to {name}\t{surname} from student list ? [Y/N]"
                                      .format_map(students_information[i]))
                    if selection == "y" or selection == "Y":
                        students_information.pop(i)
                    elif selection == "n" or selection == "N":
                        break
                    else:
                        press_valid()
        else:
            fill_all_info()


    def management_entrance(self):
        username = input("Username:")
        password = input("Password:")
        if username == admin and password == admin_password:
            return True

def fill_all_info():
    print("Please fill all information")


def operation_completed():
    print("Operation Completed Successfully...")


def choosing_password(entrance_password: str):
    while True:
        if len(entrance_password) < 6 or len(entrance_password) > 20:
            flag = -1
            break
        elif not re.search("[a-z]", entrance_password):
            flag = -1
            break
        elif not re.search("[A-Z]", entrance_password):
            flag = -1
            break
        elif not re.search("[0-9]", entrance_password):
            flag = -1
            break
        elif not re.search("[-_!@]", entrance_password):
            flag = -1
            break
        elif re.search("\s", entrance_password):
            flag = -1
            break
        else:
            print("Valid password")
            return entrance_password
    if flag == -1:
        print("Invalid password")
        time.sleep(0.75)


def password_screen():
    str = ("Primary conditions for password validation:          \n"
           "1.Minimum 8 characters.                              \n"
           "2.The alphabets must be between [a-z]                \n"
           "3.At least one alphabet should be of Upper Case [A-Z]\n"
           "4.At least 1 number or digit between [0-9].          \n"
           "5.At least 1 character from [ _ or - or ! or @ ].")
    return str


def is_name_valid(name):
    if name.isalpha():
        if 1 < len(name) < 25:
            return True


def is_surname_valid(surname):
    if surname.isalpha():
        if 1 < len(surname) < 25:
            return True


def main_screen():
    str = ("--------------------\n"
           "-------WELCOME------\n"
           "   Chose Operation  \n"
           "********************\n"
           "[1] Student sign up \n"
           "[2] Student sign in \n"
           "[3] Management      ")
    return str



def press_valid():
    print("Please press valid button")


def press_continue():
    while True:
        selection = input("To Continue Press ENTER")
        if selection == "":
            return True
        else:
            press_valid()


def choose_operation():
    operation = input("Please choose your operation")
    return operation


def wrong_username_password():
    print("Username or Password is Wrong")


def invalid_lecture_name():
    print("Invalid Lecture Name Please Make a Valid choose")


def main_selection():
    while True:
        while True:
            print(main_screen())
            selection = choose_operation()
            if selection == "1":
                name = input("Name")
                if is_name_valid(name):
                    surname = input("Surname")
                    if is_surname_valid(surname):
                        password = input("Define a Password\n" + password_screen())
                        if choosing_password(password):
                            print("Your account is creating")
                            student.create_student_table()
                            student.create_student(name, surname, password)
                            time.sleep(0.75)
                            print("Account is created")
                            if press_continue():
                                break
                        else:
                            break
                    else:
                        print("Please enter valid surname")
                        break
                else:
                    print("Please enter valid name")
                    break

            elif selection == "2":
                if student.is_there_anyone_students_list():
                    try:
                        index = student.student_entrance(input("Name:"), input("Surname:"), input("Password"))
                        while True:
                            print(student.welcome_screen(index))
                            selection = choose_operation()
                            if selection == "1":
                                print(students_information[index])
                                while True:
                                    if press_continue():
                                        break
                            elif selection == "2":
                                while True:
                                    print(lecture_list)
                                    if press_continue():
                                        break
                            elif selection == "3":
                                while True:
                                    student.add_drop_screen()
                                    selection = choose_operation()
                                    if selection == "1":
                                        if student.is_there_any_lecture_in_lecture_list():
                                            try:
                                                student.student_credit_info(index)
                                                i = student.add_lecture_control()
                                                if student.add_lecture(index, i):
                                                    print("You choose this lecture already..")

                                                else:
                                                    student.add_lecture_last(index, i)
                                                    student.student_credit_info(index)
                                                    operation_completed()
                                                    while True:
                                                        if press_continue():
                                                            break
                                            except TypeError:
                                                print("Invalid lecture name")
                                                if press_continue():
                                                    break
                                    elif selection == "2":
                                        if student.is_there_any_lecture_in_student_lecture_list(index):
                                                i = student.student_remove_lecture_control(index)
                                                student.remove_lecture(index, i)
                                                student.student_credit_info(index)
                                                operation_completed()
                                                while True:
                                                    if press_continue():
                                                        break
                                        else:
                                            while True:
                                                if press_continue():
                                                    break
                                    elif selection == "q" or selection == "Q":
                                        break
                                    else:
                                        while True:
                                            press_valid()
                                            break
                            elif selection == "Q" or selection == "q":
                                break
                            else:
                                while True:
                                    press_valid()
                                    break
                    except TypeError:
                        print("Wrong username or password")
            elif selection == "3":
                if bool(manager.management_entrance()):
                    while True:
                        manager.management_screen()
                        selection = choose_operation()
                        if selection == "1":
                            while True:
                                manager.management_lists_screen()
                                selection = choose_operation()
                                if selection == "1":
                                    manager.management_show_students()
                                    while True:
                                        if press_continue():
                                            break
                                elif selection == "2":
                                    manager.management_show_lectures()
                                    while True:
                                        if press_continue():
                                            break
                                elif selection == "Q" or selection == "q":
                                    break
                                else:
                                    while True:
                                        press_valid()
                                        break
                        elif selection == "2":
                            while True:
                                manager.student_add_remove()
                                selection = choose_operation()
                                if selection == "1":
                                    while True:
                                        manager.add_student()
                                        operation_completed()
                                        if press_continue():
                                            break
                                elif selection == "2":
                                    while True:
                                        manager.remove_student()
                                        operation_completed()
                                        if press_continue():
                                            break
                                elif selection == "q" or selection == "Q":
                                    break
                                else:
                                    while True:
                                        press_valid()
                                        break

                        elif selection == "3":
                            while True:
                                manager.management_add_and_remove_operations_lecture_screen()
                                selection = choose_operation()
                                if selection == "1":
                                    try:
                                        manager.management_add_lecture()
                                        operation_completed()
                                        if press_continue():
                                            break
                                    except ValueError:
                                        print("Please enter all information")
                                elif selection == "2":
                                    if manager.management_remove_lecture():
                                        operation_completed()
                                        if press_continue():
                                            break
                                    else:
                                        invalid_lecture_name()
                                        break
                                elif selection == "3":
                                    manager.management_delete_lecture_list()
                                    operation_completed()
                                    if press_continue():
                                        break
                                elif selection == "4":
                                    manager.management_delete_student_list()
                                    operation_completed()
                                    if press_continue():
                                        break
                                elif selection == "q" or selection == "Q":
                                    break
                                else:
                                    while True:
                                        press_valid()
                                        break
                        elif selection == "Q" or selection == "q":
                            break
                        else:
                            while True:
                                press_valid()
                                break
                else:
                    while True:
                        wrong_username_password()
                        break
            else:
                while True:
                    press_valid()
                    break


student = Student()
manager = Manager()
main_selection()
