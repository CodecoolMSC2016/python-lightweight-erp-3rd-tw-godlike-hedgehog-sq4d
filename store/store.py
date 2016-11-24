# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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
    table = data_manager.get_table_from_file('store/games.csv')
    title = 'Store manager'
    tool_manager_options = ['Show table', 'Add', 'Remove',
                            'Update', 'Get games by manufacturers', 'Get average stock amounts']
    while True:
        type_list = ["int"]
        ui.print_menu(title, tool_manager_options, 'Back to main menu')
        inputs = ui.get_inputs(["Please enter a number: "], "", type_list)
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            list_labels = ['Add an id you want to remove: ']
            type_list = ["str"]
            inputs = ui.get_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            remove(table, inputs)
        elif option == "4":
            list_labels = ['Add an id you want to update: ']
            type_list = ["str"]
            inputs = ui.get_inputs(list_labels, '', type_list)
            inputs = inputs[0]
            update(table, inputs)
        elif option == "5":
            result = get_counts_by_manufacturers(table)
            ui.print_result(result, '')
        elif option == "6":
            type_list = ["str"]
            inputs = ui.get_inputs(["Add a manufacturer: "], "", type_list)
            inputs = inputs[0]
            result = get_average_by_manufacturer(table, inputs)
            ui.print_result(result, '')
        elif option == "0":
            break

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
    ui.print_table(table, title_list)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    id = common.generate_random(table)
    type_list = ["str", "str", "int", "int"]
    list_labels = ["title", "manufacturer", "price", "in-stock"]
    title = "Enter the details"
    inputs = []
    inputs = ui.get_inputs(list_labels, title, type_list)
    inputs.insert(0, id)
    table.append(inputs)
    data_manager.write_table_to_file('store/games.csv', table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for nested_list in table:
        if id_ == nested_list[0]:
            table.remove(nested_list)
    data_manager.write_table_to_file('store/games.csv', table)
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
            element = ui.get_inputs(
                ['Which elements index you want to modify: '], '', type_list)
            element = int(element[0])
            modification = ui.get_inputs(['Change element: '], '', type_list)
            nested_list[element] = modification[0]
    data_manager.write_table_to_file('store/games.csv', table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacture = {}
    for row in range(len(table)):
        counter = 0
        for manufacturer in range(len(table)):
            if table[manufacturer][2] == table[row][2]:
                counter += 1
        manufacture.update({table[row][2]: counter})

    return manufacture

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    amount = 0
    counter = 0
    result = 0
    for row in range(len(table)):
        if manufacturer == table[row][2]:
            amount += int(table[row][4])
            counter += 1
    result = amount / counter
    return result

    pass
