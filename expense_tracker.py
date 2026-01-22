import datetime
import time


all_expenses = []
counter_for_id = 1
def menu_option():
    '''
    This is a function that will print a basic menu for the use to choose from. 
    '''
    user_choices = """
    Welcome to your own personal expense tracker
    Please choose one of the following options

    1. View all the expenses
    2. Add an expense
    3. Remove a expense
    4. Edit an expense

    Enter your choice : 
    """
    return user_choices

#============================ Add Expense==================================
def add_expense(amount , category , note, *args , **kwargs):
    '''
    This is a function used to add an expense to a list of all expenses, the expenses are in the form of a tuple
    '''
    date_of_transaction = datetime.date.today()
    str_date_of_transaction = date_of_transaction.strftime("%d-%B-%Y") #convers datetime to day - month(alphabetic) - year(4 digits)

    #adding an id counter 
    #if the user added no note
    if note is None:
        item_id = counter_for_id
        expense = ( item_id, str_date_of_transaction , amount , category , None)
    item_id = counter_for_id
    expense = (item_id , str_date_of_transaction , amount , category , note) 
    all_expenses.append(expense)
    return expense
#==============================================================

#====================== View all expenses========================================
def view_all_expense():
    for index , item in enumerate(all_expenses):
        print(f"{index +1 } : {item[1:]}")
    return 
#==============================================================


#======== Helper function to check for partial matches ========

def partial_match(list_of_tuple , parial_matching_tuple):
    '''
    this is a helper function that is used to get return all the expenses that the user wants to remove 

    example:
    a = [(date1 , amount1 , category1 , note1) , date1 , amount1 , category2 , note2)  , (date2 , amount2 , category1 , note1)]
    search = (date 1, amount1)

    output : (date1 , amount1 , category1 , note1) , (date1 , amount1 , category2 , note2)
    '''
    res = []
    if len(parial_matching_tuple) == 1:
        for expense in list_of_tuple:
            if expense[1:2] == parial_matching_tuple:
                res.append(expense)
        return res
    elif len(parial_matching_tuple) == 2:
        for expenses in list_of_tuple:
            if expenses[1:3] == parial_matching_tuple:
                res.append(expenses)
        return res
    else:
        for expenses in list_of_tuple:
            if expenses[1:4] == parial_matching_tuple:
                res.append(expenses)
        return res

#==============================================================

#=================== Remove Expense ===========================================
def remove_expense(date , amount , category):
    '''
    This function will remove the a expense from the list of expenses , 
    we need to ask the user what expense at what date does he want to remove
    '''
    #we first assume that the user provided the category and amount for the expense
    if amount is not None and category is not None: 
        partial_matching_tuple = (date , amount , category)
        result = partial_match(list_of_tuple=all_expenses , parial_matching_tuple=partial_matching_tuple)
        for index , items in enumerate(result):
            print(f"{index + 1} : {items[1:]}")

        #if user enters any value which is not a number
        print('')
        try:
            user_choice = int(input("please enter the choice you want to delete : "))
        except ValueError as value_err:
            print("please enter a valid number")
            return 
        #if user tries to enter a value greater than the given value
        if user_choice < 1 or user_choice > len(result):
             print("please enter a valid choice.")
             return
        
        index_to_delete = user_choice - 1
        target_item = result[index_to_delete]
        all_expenses.remove(target_item)
        print("item successfully deleted")
        return 
    #end of base conditon 

    #if category is None and amount is also none
    if amount is None and category is None:
        partial_matching_tuple = (date,) #makes it a tuple
        result = partial_match(list_of_tuple=all_expenses , parial_matching_tuple = partial_matching_tuple)
        for index , item in enumerate(result):
            print(f"{index + 1} , {item[1:]}")
        #if user enters any value which is not a number
        print('')
        try:
            user_choice = int(input("please enter the choice you want to delete : "))
        except ValueError as value_err:
            print("please enter a valid number")
            return 
        #if user tries to enter a value greater than the given value
        if user_choice < 1 or user_choice > len(result):
            print("please enter a valid choice.")
            return
        
        index_to_delete = user_choice - 1
        target_item = result[index_to_delete]
        all_expenses.remove(target_item)
        print("item successfully deleted")
        return 

    #if only the date and amont is provided
    if amount is not None and category is None:
        partial_matching_tuple = (date , amount)
        result = partial_match(list_of_tuple=all_expenses , parial_matching_tuple = partial_matching_tuple)
        for index , item in enumerate(result):
            print(f"{index + 1} , {item[1:]}")
        #if user enters any value which is not a number
        print('')
        try:
            user_choice = int(input("please enter the choice you want to delete : "))
        except ValueError as value_err:
            print("please enter a valid number")
            return 
        #if user tries to enter a value greater than the given value
        if user_choice < 1 or user_choice > len(result):
            print("please enter a valid choice.")
            return
        
        index_to_delete = user_choice - 1
        target_item = result[index_to_delete]
        all_expenses.remove(target_item)
        print("item successfully deleted")
        return 




#==============================================================

#=========================== Menu helper function for edit expense =================================
def menu_edit_expense():
    edit_uder_choice = '''
Please enter what you want to change about the expense

1. date
2. amount 
3. category
4. note

please enter your choice:
    '''
    return edit_uder_choice
#==============================================================


#==================Edit a expense============================================
def edit_expense(date , amount , category):
    #if only date is provided
    if amount is None and category is None:
        date_tuple = (date,)
        result = partial_match(list_of_tuple=all_expenses , parial_matching_tuple=date_tuple)
        for index , item in enumerate(result):
            print(f"{index + 1} : {item[1:]}")
        print('')
    #if only date and amount is given 
    elif amount is not None and category is None:
        date_amount_tuple = (date , amount)
        result = partial_match(list_of_tuple=all_expenses , parial_matching_tuple=date_amount_tuple)
        for index , item in enumerate(result):
            print(f"{index + 1} : {item[1:]}")
        print('')
    #if all 3 are given 
    elif amount is not None and category is not None:
        date_amount_category_tuple = (date , amount , category)
        result = partial_match(list_of_tuple=all_expenses , parial_matching_tuple=date_amount_category_tuple)
        for index , item in enumerate(result):
            print(f"{index + 1} : {item[1:]}")
        print('')
            
    try:
        user_choice = int(input("please enter the expense you want to edit: "))
    except ValueError as value_err:
        print("please enter a valid number")
        return
        
    if user_choice < 1 or user_choice > len(result):
        print("please enter a valid response from the list")
        return 
        
    index_to_edit = user_choice - 1
    expense_to_edit = result[index_to_edit]
    edit_expense_list = list(expense_to_edit)

    try:
        user_choice = int(input(menu_edit_expense()))
    except ValueError as VE:
        print('please enter a number')
        return
        
    if user_choice < 1 or user_choice > 4:
        print("enter a valid choice")
        return

    #if user wants to change the date
    if user_choice == 1:
        try:
            day = int(input('please enter the day'))
            month = int(input('please enter the month'))
            year = int(input('please enter the year'))
 
        except ValueError:
            print("enter date in numbers please")
            return 
        try:
            updated_date = datetime.datetime(year , month , day).strftime("%d-%B-%Y")
        except ValueError:
            print("please enter the correct date")
            return
        edit_expense_list[1] = updated_date
        edited_date_tuple = tuple(edit_expense_list)
        index_to_edit = all_expenses.index(expense_to_edit)
        all_expenses[index_to_edit] = edited_date_tuple
        print('date updated successfully')
        return 
    #if user changed the amount
    if user_choice == 2:
        try:
            amount = int(input("enter the amount you want to change"))
        except ValueError:
            print("please enter a value")
            return 
            
        edit_expense_list[2] = amount
        edited_tuple = tuple(edit_expense_list)
        print(edited_tuple)
        index_to_edit_tuple = all_expenses.index(expense_to_edit)
        all_expenses[index_to_edit_tuple] = edited_tuple
        print("editing successful")
        return 
    #if user changed the category
    if user_choice == 3:
        updated_category = str(input("enter the new category"))
        if len(updated_category) == 0:
            updated_category = None
        if updated_category.isdigit():
            print("please enter a sentence and not a number")
            return 
        edit_expense_list[3] = updated_category
        edited_category_tuple = tuple(edit_expense_list)
        index_edited_category_tuple = all_expenses.index(expense_to_edit)
        all_expenses[index_edited_category_tuple] = edited_category_tuple
        print("editing successful")
        print(edited_category_tuple)
        return
    if user_choice == 4:
        if expense_to_edit[3] == None: #if category of the tuple is None
            print("to add a Note please edit the category first ")
            return
        print("enter your note , press CTRL-D or CTRL-Z to save")
        updated_note_list = []
        while True:
            try:
                line = input()
            except EOFError:
                break 
            updated_note_list.append(line)
        updated_note = ''.join(updated_note_list)

        edit_expense_list[-1] = updated_note
        edited_note_tuple = tuple(edit_expense_list)
        index_to_edit_note = all_expenses.index(expense_to_edit)
        all_expenses[index_to_edit_note] = edited_note_tuple
        return 
#==============================================================


#========================== MAIN FUNCTION ====================================
def main():
    try:
        user_choice = int(input(menu_option()))
    except ValueError:
        print("Please make sure that the option is a number")
        return 

    #is the user choice is outside of the 
    if user_choice <= 0 or user_choice > 4:
        print("please choose the correct option and try again")
        return 

    if user_choice == 1:
        view_all_expense()

    if user_choice == 2:
        try:
            amount = int(input("enter the amount you want to add"))
        except ValueError as VE:
            print("please enter digits and not a sentence")
            return
        category = input('enter your category')

        if category.isdigit():
            print("Please enter the correct category")
            return 
        user_note_choice = input("Do you want to enter a note : (y/n)").lower()
        if user_note_choice == 'y':
            while True:
                print("enter the note you want to save! CTRL-D or CTRL-Z to save : \n")
                note_list = []
                try:
                    line = input()
                except EOFError as EOF:
                    break
                note_list.append(line)
            note = ''.join(note_list)
        elif user_note_choice == 'n':
            note = ""
        else:
            note = ""
        if note == "":
            add_expense(amount , category)
            counter_for_id += 1
            print("expense added successfully")
            return 
        else:
            add_expense(amount , category , note)
            counter_for_id += 1 
            print("expense added successfully")
            return 
    
    if user_choice == 3:
        specific_date = input("do you want to remove the expense from a specific date? (y/n)").lower()
        if specific_date == 'y':
            try:
                day = int(input('please enter the day'))
                month = int(input('please enter the month'))
                year = int(input('pelase enter the year'))
 
            except ValueError:
                print("enter date in numbers please")
                return 
            date = datetime.datetime(year , month , day).strftime('%d-%B-%Y')
        elif specific_date == 'n':
            date = datetime.datetime.today().strftime('%d-%B-%Y')
        else:
            print("please enter a valid value")
            return 
    
        amount_flag = input("do you remember the amount (y/n)").lower()
        if amount_flag == 'y':
            try:
                amount = int(input("enter the amount:"))
            except ValueError:
                print("please enter the valid value")
                return 
        elif amount_flag == 'n':
            amount = None
        else:
            print("please enter a valid value")
            return 

        if amount is not None:
            category_flag = input("do you remember the category(y/n)").lower()
            if category_flag == 'y':
                category = input("enter your category")
            elif category_flag =='n':
                category = None
            else:
                print("please enter the valid value")
                return 
        elif amount is None:
            category = None
        remove_expense(date , amount , category)
    
    #edit an expense
    if user_choice == 4:
        specific_date = input("do you want to edit the expense from a specific date? (y/n)").lower()
        if specific_date == 'y':
            try:
                day = int(input('please enter the day'))
                month = int(input('please enter the month'))
                year = int(input('pelase enter the year'))

            except ValueError:
                print("enter date in numbers please")
                return 
            date = datetime.datetime(year , month , day).strftime('%d-%B-%Y')
        elif specific_date == 'n':
            date = datetime.datetime.today().strftime('%d-%B-%Y')
        else:
            print("please enter a valid value")
            return 
        amount_flag = input("do you remember the amount (y/n)").lower()
        if amount_flag == 'y':
            try:
                amount = int(input("enter the amount:"))
            except ValueError:
                print("please enter the valid value")
                return 
        elif amount_flag == 'n':
            amount = None
        else:
            print("please enter a valid value")

        if amount is not None:
            category_flag = input("do you remember the category(y/n)").lower()
            if category_flag == 'y':
                category = input("enter your category")
            elif category_flag =='n':
                category = None
            else:
                print("please enter the valid value")
                return 
        elif amount is None:
            category = None
        edit_expense(date , amount , category)
#==============================================================

            
if __name__ == '__main__':
    main()