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
    table = data_manager.get_table_from_file('tool_manager/tools.csv')
    title = 'Tool manager'
    while True:
        type_list = ["int"]
        tool_manager_options = ['Show table', 'Add', 'Remove', 'Update',
                                'Get available tools', 'Get average durability by manufacturers']
        ui.print_menu(title, tool_manager_options, 'Back to main menu')

        inputs = ui.get_submenu_inputs(
            ["Please enter a number: "], "", type_list)
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            type_list = ["str"]
            list_labels = ['Add an id you want to remove: ']
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            remove(table, inputs)
        elif option == "4":
            type_list = ["str"]
            list_labels = ['Add an id you want to update: ']
            inputs = ui.get_submenu_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            update(table, inputs)
        elif option == "5":
            result = get_available_tools(table)
            ui.print_result(result, '')
        elif option == "6":
            result = get_average_durability_by_manufacturers(table)
            ui.print_result(result, '')
        elif option == "0":
            break
    return
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "manufacturer", "purchase date", "durability"]
    ui.print_table(table, title_list)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    id = common.generate_random(table)
    type_list = ["str", "str", "int", "int"]
    list_labels = ["name", "manufacturer", "purchase date", "durability"]
    title = "Enter the details"
    inputs = []
    inputs = ui.get_submenu_inputs(list_labels, title, type_list)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file('tool_manager/tools.csv', table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string

def remove(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            table.remove(nested_list)
    data_manager.write_table_to_file('tool_manager/tools.csv', table)
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
    data_manager.write_table_to_file('tool_manager/tools.csv', table)
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    year = 2016
    result_list = []
    for nested_list in table:
        nested_list[3] = int(nested_list[3])
        nested_list[4] = int(nested_list[4])
        if nested_list[3] + nested_list[4] >= year:
            result_list.append(nested_list)
    return result_list
    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    durability = {}
    for row in range(len(table)):
        counter = 0
        sum = 0
        result = 0
        for manufacturer in range(len(table)):
            if table[manufacturer][2] == table[row][2]:
                sum += int(table[manufacturer][4])
                counter += 1
        result = sum / counter
        durability.update({table[row][2]: result})

    return durability
    pass
