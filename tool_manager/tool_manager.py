# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    table = data_manager.get_table_from_file('tool_manager/tools.csv')
    title = 'Tool manager'
    while True:
        tool_manager_options = ['Show table','Add','Remove','Update','Get available tools','Get average durability by manufacturers']
        ui.print_menu(title, tool_manager_options, 'Back to main menu')
    
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            list_labels = ['Add an id you want to remove: ']
            inputs = ui.get_inputs(list_labels,'')
            inputs = inputs[0]
            remove(table, inputs)
        elif option == "4":
            list_labels = ['Add an id you want to update: ']
            inputs = ui.get_inputs(list_labels,'')
            inputs = inputs[0]
            update(table, inputs)
        elif option == "5":
            get_available_tools(table)
        elif option == "6":
            get_average_durability_by_manufacturers(table)
        elif option == "0":
            break
    return
    


    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    print('Fika')
    print(table)

    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    id = common.generate_random(table)
    list_labels = ["name", "manufacturer", "purchase date", "durability"]
    title = "Enter the details"
    inputs = []
    inputs = ui.get_inputs(list_labels, title)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file('faszomtudjami.csv', table)

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
            element = ui.get_inputs(['Which elements index you want to modify: '] ,'')
            element = int(element[0])
            modification = ui.get_inputs(['Change element: '] ,'')
            nested_list[element] = modification[0]
  
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    year = 2016
    result_list =[]
    for nested_list in table:
        if (int(nested_list[3])+int(nested_list[4]))>=year:
            result_list.append(nested_list)
    print(result_list)

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass

#start_module()
