# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    table = data_manager.get_table_from_file("crm/customers.csv")
    title = "Customer Relationship Management (CRM)"
    crm_options = ["Show table", "Add", "Remove",
                   "Update", "Get longest name id", "Get subscribed emails"]
    while True:
        ui.print_menu(title, crm_options, 'Back to main menu')
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            list_labels = ['Add an id you want to remove: ']
            inputs = ui.get_inputs(list_labels, '')
            inputs = inputs[0]
            remove(table, inputs)
        elif option == "4":
            list_labels = ['Add an id you want to update: ']
            inputs = ui.get_inputs(list_labels,'')
            inputs = inputs[0]
            update(table, inputs)
        elif option == "5":
            result = get_longest_name_id(table)
            ui.print_result(result, "") 
        elif option == "6":
            result = get_subscribed_emails(table)
            ui.print_result(result, "")
        elif option == "0":
            break

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    id = common.generate_random(table)
    list_labels = ["name", "email", "subscribed"]
    title = "Enter the details"
    inputs = []
    inputs = ui.get_inputs(list_labels, title)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file("teszt.csv", table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            table.remove(nested_list)
    data_manager.write_table_to_file('faszomtudjami.csv', table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            element = ui.get_inputs(
                ['Which elements index you want to modify: '], '')
            element = int(element[0])
            modification = ui.get_inputs(['Change element: '], '')
            nested_list[element] = modification[0]

    return table


# special functions:
# ------------------

# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name,
# return the first of descending alphabetical order
def get_longest_name_id(table):
    name = []
    # leghosszab len(name)
    name_lenght = len(table[0][1])
    for item in table:
        if len(item[1]) == name_lenght:
            name.append(item[1])
    # bubble sort, hogy a listát rendezzük sort() nélkül; descending alphabetical: A-Z
    for num in range(len(name)-1,0,-1):
        for i in range(num):
            if name[i] > name[i+1]:
                temp = name[i]
                name[i] = name[i+1]
                name[i+1] = temp
    # az id meghatározása
    for line in table:
        if name[0] == line[1]:
            return (line[0])
    
    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name,
# separator=";")
def get_subscribed_emails(table):
    result_list = []
    for line in table:
        subscribed = line[3]
        if subscribed == "1":
            email = line[2]
            name = line[1]
            result_item = email + ";" + name
            result_list.append(result_item)
    return result_list
     
    pass
