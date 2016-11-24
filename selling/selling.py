# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    table = data_manager.get_table_from_file('selling/sellings.csv')
    title = 'Tool manager'
    tool_manager_options = ['Show table', 'Add', 'Remove',
                            'Update', 'Get cheapest item', 'Get sellings between dates']
    while True:
        ui.print_menu(title, tool_manager_options, 'Back to main menu')
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            list_labels = ['Add an id you want to remove']
            inputs = ui.get_inputs(list_labels, '')
            remove(table, inputs)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            result = get_lowest_price_item_id(table)
            ui.print_result(result, '')
        elif option == "6":
            list_labels = ['Enter the starting month', 'Enter the starting day', 'Enter the starting year',
                           'Enter the ending month', 'Enter the ending day', 'Enter the ending year']
            inputs = ui.get_inputs(list_labels, '')
            result = get_items_sold_between(table, inputs[0], inputs[1],
                                            inputs[2], inputs[3], inputs[4], inputs[5])
            ui.print_result(result, '')
        elif option == "0":
            break

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "price", "month", "day", "year"]
    ui.print_table(table, title_list)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    id = common.generate_random(table)
    list_labels = ["title", "price", "month", "day", "year"]
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
            element = ui.get_inputs(
                ['Which elements index you want to modify: '], '')
            element = int(element[0])
            modification = ui.get_inputs(['Change element: '], '')
            nested_list[element] = modification[0]

    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of
# descending alphabetical order
def get_lowest_price_item_id(table):
    lowest_price = table[0][2]
    result = ''
    for item in table:
        if item[2] < lowest_price:
            lowest_price = item[2]
    found_lowest = False
    for item in table:
        if item[2] == lowest_price and not found_lowest:
            result = item[0]
            found_lowest = True

    return(result)


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    converted_from = date_converter(month_from, day_from, year_from)
    converted_to = date_converter(month_to, day_to, year_to)

    result = []
    for item in table:
        if date_converter(item[3], item[4], item[5]) >= converted_from and date_converter(item[3], item[4], item[5]) <= converted_to:
            result.append(item)
    return(result)


def date_converter(month, day, year):
    year = str(year)
    month = str(month)
    day = str(day)
    new_day = ''
    new_month = ''
    result = ''
    if len(day) == 1:
        new_day = '0' + day
    else:
        new_day = day
    if len(month) == 1:
        new_month = '0' + month
    else:
        new_month = month
    result += year
    result += new_month
    result += new_day
    result = int(result)

    return(result)
