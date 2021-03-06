# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    table = data_manager.get_table_from_file('hr/persons.csv')
    title = 'Human Resources Manager'
    tool_manager_options = ['Show table', 'Add', 'Remove', 'Update',
                            'Get oldest person', 'Get closest-to-average aged people']
    while True:
        type_list = ["int"]
        ui.print_menu(title, tool_manager_options, 'Back to main menu')
        inputs = ui.get_submenu_inputs(
            ["Please enter a number: "], "", type_list)
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            list_labels = ['Add an id you want to remove: ']
            type_list = ["str"]
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            remove(table, inputs)
        elif option == "4":
            list_labels = ['Add an id you want to update: ']
            type_list = ["str"]
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            update(table, inputs)
        elif option == "5":
            result = get_oldest_person(table)
            ui.print_result(result, "Oldest person/s is/are: ")
        elif option == "6":
            result = get_persons_closest_to_average(table)
            ui.print_result(result, "Closest to average person is: ")
        elif option == "0":
            break

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "birth_date"]
    ui.print_table(table, title_list)
    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    id = common.generate_random(table)
    list_labels = ["name", "birth date"]
    type_list = ["str", "int"]
    title = "Enter the details"
    inputs = []
    inputs = ui.get_submenu_inputs(list_labels, title, type_list)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file('hr/persons.csv', table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            table.remove(nested_list)
    data_manager.write_table_to_file('hr/persons.csv', table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    type_list = ["str"]
    for nested_list in table:
        if id_ == nested_list[0]:
            element = ui.get_submenu_inputs(
                ['Which elements index you want to modify: '], '', type_list)
            element = int(element[0])
            modification = ui.get_submenu_inputs(
                ['Change element: '], '', type_list)
            nested_list[element] = modification[0]
    data_manager.write_table_to_file('hr/persons.csv', table)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with
# the same value)
def get_oldest_person(table):
    oldest_person = []
    birth_date = table[0][2]
    for item in table:
        if item[2] < birth_date:
            birth_date = item[2]
    for item in table:
        if item[2] == birth_date:
            oldest_person.append(item[1])

    return(oldest_person)


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with
# the same value)
def get_persons_closest_to_average(table):
    closest_to_avg_person = []
    avg = 0
    counter = 0
    for item in table:
        avg += int(item[2])
        counter += 1
    avg = avg / counter
    difference = 10000
    for item in table:
        if abs(int(item[2]) - avg) < difference:
            difference = abs(int(item[2]) - avg)
    for item in table:
        if abs(int(item[2]) - avg) == difference:
            closest_to_avg_person.append(item[1])

    return(closest_to_avg_person)
