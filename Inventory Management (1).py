#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime
product_lines = {}


# In[6]:


def get_current_timestamp():
    return datetime.now().isoformat()


# In[3]:


def add_product_line():

    while True:
        # Input to enter new product line
        new_product_line = input("What is your new product line? Or type main menu to return to the main menu.")
        new_product_line_clean = new_product_line.strip().lower() # cleans product line for consistent formatting

        # Returns user to main menu
        if new_product_line_clean == "main menu":
            return

        # If input is already in the product line list, tells user. Lets user input a different product line.
        if new_product_line_clean in product_lines:
            print("That product line already exists.")
            continue # lets user retry

        # Double checks product line was entered correctly
        yes_or_no = input(f"Is '{new_product_line_clean}' the product line you wished to enter? (yes/no)")
        yes_or_no_clean = yes_or_no.strip().lower() # cleans input line for consistency

        # Amends the product line to product line dictionary
        if yes_or_no_clean == "yes":
            product_lines[new_product_line_clean] = {}
            print(f"'{new_product_line_clean}' has been added.")

            # Asks user if they want to input more
            input_more = input("Would you like to input another new product line?")
            input_more_clean = input_more.strip().lower() # Cleans input for consistency
            
            # if user inputs anything but yes, returns user to the main menu
            if input_more_clean != "yes":
                return
                
        # Asks user to correct product line input
        elif yes_or_no_clean == "no": 
            print("Please print correct product line.")

        else:
            print("Please enter yes or no.")
        

def remove_product_line():

    while True:
        # Asks user to enter product line they wish to remove and cleans it
        removed_product_line = input("Which product line would you like to remove? Or type main menu to return to the main menu")
        removed_product_line_clean = removed_product_line.strip().lower()

        # Returns user to main menu
        if removed_product_line_clean == "main menu":
            return

        # If product line is not in product lines dictionary, tells user that product line doesn't exist and to try again
        elif removed_product_line_clean not in product_lines:
            print("Product line doesn't exist. Please try again.")
            continue

        # Double checks user wants to delete product line before deleting
        yes_or_no = input(f"Are you sure you wish to remove '{removed_product_line_clean}'?")
        yes_or_no_clean = yes_or_no.strip().lower()

        # If yes, removes product line from product line dictionary and tells user it has been deleted 
        if yes_or_no_clean == "yes":
            del product_lines[removed_product_line_clean]
            print(f"'{removed_product_line_clean}' has been successfully removed.")

            # Gives user option to delete more
            delete_more = input("Is there another product line you wish to delete?")
            delete_more_clean = delete_more.strip().lower()
            if delete_more_clean != "yes":
                return

        # If user enters no, asks user to enter correct product line
        elif yes_or_no_clean == "no":
            print("Please enter correct product line.")

        else: 
            print("Please enter yes or no.")

def edit_product_line():
    while True:

        # Asks user for input and cleans it for consistency
        change_choice = input("Please enter the product line you wish to edit. Or enter main menu to return to main menu.")
        change_choice_clean = change_choice.strip().lower()

        # Returns user to main menu
        if change_choice_clean == "main menu":
            return

        elif change_choice_clean in product_lines:
            changed_product_line = input(f"What do you wish to change {change_choice_clean} to. Or type back to return.")
            changed_product_line_clean = changed_product_line.strip().lower()
            if changed_product_line_clean == change_choice_clean:
                print("Product line is already that value. Please try again.")
                continue

            # Returns user to edit product line
            if changed_product_line_clean == "back":
                continue
                
            elif changed_product_line_clean != change_choice_clean:
                yes_or_no = input(f"Are you sure you want to change '{change_choice_clean}' to '{changed_product_line_clean}'?")
                yes_or_no_clean = yes_or_no.strip().lower()

                if yes_or_no_clean != "yes":
                    print("No changes were made.")
                    continue
                    
                elif yes_or_no_clean == "yes":
                    product_lines[changed_product_line_clean] = product_lines.pop(change_choice_clean)

        elif change_choice_clean not in product_lines:
            print("Product line is not valid. Please try again.")


# In[4]:


def add_product(): 

    # Asks users to choose a product line to add to
    while True:
        try: 
            print("Please select which product line you would like to add a product to.")
            product_line_list = list(product_lines.keys())

            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")
                
            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index - 1]
            break
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue

    # Asks user to confirm choice
    while True: 
        yes_or_no = input(f"Is {selected_product_line} the correct product line?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            print("Invalid input. Try again")
            # Loops back to try again
            continue

        elif yes_or_no_clean == "yes":
            break

    # Asks user to enter product name 
    while True: 
        product_to_add = input(f"Please input the product you wish to add to {selected_product_line}.")
        product_to_add_clean = product_to_add.strip().lower()
        yes_or_no = input(f"Is {product_to_add_clean} the product you wish to add to {selected_product_line}?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            print("Please try again.")
            continue

        elif yes_or_no_clean == "yes":
            product_lines[selected_product_line][product_to_add_clean] = {}
            print(f"{product_to_add_clean} has been added to {selected_product_line}. \n"
            f"Would you like to edit {product_to_add_clean} details now?")
            yes_or_no = input("Please enter yes or no.")
            yes_or_no_clean = yes_or_no.strip().lower()
            if yes_or_no_clean == "no":
                print("Have a nice day.")
                break
            elif yes_or_no_clean == "yes":
                edit_product_details()
            else: 
                print("Invalid input. Please try again.")

def remove_product():
    # Asks users to choose a product line they would like to remove a product from 
    while True:
        try: 
            print("Please select which product line you would like to add a product to.")
            product_line_list = list(product_lines.keys())

            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")
                
            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index - 1]
            break
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue

    # Asks user to confirm choice
    while True: 
        yes_or_no = input(f"Is {selected_product_line} the correct product line?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            print("Invalid input. Try again")
            # Loops back to try again
            continue

        elif yes_or_no_clean == "yes":
            break

    # Prints products under that product line
    while True: 
        try:
            print(f"Please select which product under {selected_product_line} you would like to delete.")
            product_list = list(product_lines[selected_product_line].keys())
            for i, product in enumerate(product_list, 1):
                print(f" {i}:{product}")
            choice_index = int(input("Please input the number of your selection"))
            selected_product = product_list[choice_index - 1]
            break
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue

    # Asks user to confirm selection
    while True: 
        yes_or_no = input(f"Is {selected_product} the correct product line?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            print("Invalid input. Try again")
            # Loops back to try again
            continue

        elif yes_or_no_clean == "yes":
            # Moves to next bit of code
            break

    # Deletes selected product from the products dictionary
    del product_lines[selected_product_line][selected_product]
                  

def edit_product_name():
    # Asks for product line and confirms with user entered product line is correct
    while True:
        product_line_name = input("Please enter product line name.")
        product_line_name_clean = product_line_name.strip().lower()
        # If product line not in entered product line list, gives error and asks to try again.
        if product_line_name_clean not in product_lines:
            print("That product line doesn't exist. Please try again.")
            continue

        yes_or_no = input(f"Is {product_line_name_clean} correct?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            # Takes user back to beginning of while loop to try again
            print("Please try again.")
            continue
        elif yes_or_no_clean == "yes":
            # Moves to next part of code
            break

    while True:
        try:
            print(f"Please select which product under {product_line_name_clean} you would like to delete.")
            product_list = list(product_lines[product_line_name_clean].keys())
            for i, product in enumerate(product_list, 1):
                print(f" {i}:{product}")
            choice_index = int(input("Please input the number of your selection"))
            selected_product = product_list[choice_index - 1]
            break
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue


            # Asks user to confirm selection
    while True: 
        yes_or_no = input(f"Is {selected_product} the correct product line?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            print("Invalid input. Try again")
            # Loops back to try again
            continue

        elif yes_or_no_clean == "yes":
            # Moves to next bit of code
            break

    # Asks user to input new product name
    new_product_name = input(f"Please enter the new product name to replace {selected_product}.")

    # Asks user to confirm name change
    while True: 
        yes_or_no = input(f"Is {new_product_name} what you want to replace {selected_product} with?")
        yes_or_no_clean = yes_or_no.strip().lower()
        if yes_or_no_clean != "yes":
            print("Invalid input. Try again")
            # Loops back to try again
            continue

        elif yes_or_no_clean == "yes":
            # Moves to next bit of code
            break

    # Changes the product's name
    correct_name = product_lines[product_line_name_clean].pop(selected_product)
    product_lines[product_line_name_clean][new_product_name] = correct_name

    # Confirms that product name was successfully updated 
    print("Product name was successfully updated!")
        


# In[10]:


# Still need to add confirmation checks before saving the product details

def add_product_details():
    # Asks user to choose product line from list
    while True: 
        try:
            print("Please select which product line the product you would like to add details is under.")
            product_line_list = list(product_lines.keys())

            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")

            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index -1]
            break
        except ValueError: 
            print("Please enter a valid input from the list.")

    # Asks user to choose product from chosen product line's product list
    while True: 
        try:
            print(f"Please select which product you would like to add details to under the {selected_product_line}'s products.")
            product_list = list(product_lines[selected_product_line].keys())
    
            for i, product in enumerate(product_list, 1):
                print(f"{i}: {product}")

            choice_index = int(input("Please input the number of your selection: "))
            selected_product = product_list[choice_index - 1]
            break
        except ValueError: 
            print("Please enter a valid input from the list.")

    # Asks user to input product id number or skip. Skip stores id number as none. 
    while True: 
        product_id_input = input("Please enter the product id number or enter 'skip'.")
        if product_id_input.lower().strip() == "skip":
            product_id = None
            break
        try:
            product_id = int(product_id_input)
            break
        except ValueError:
            print("Please enter an integer for the product id or skip.")

    # Asks user to input sku number or skip. Skip stores sku as none
    while True: 
        sku_input = input("Please enter the sku number of this product or enter 'skip'.")
        if sku_input.lower().strip() == "skip":
            sku = None
            break
        try: 
            sku = int(sku_input)
            break 
        except ValueError: 
            print("Please enter an integer for the sku number or skip.")
            

    # Asks user to input price or skip. Skip stores price as none. 
    while True: 
        price_input = input("Please enter the price of this product or enter 'skip'.")
        if price_input.lower().strip() == "skip":
            price = None
            break
        try:
            price = float(price_input) 
            break
        except ValueError: 
            print("Please enter a decimal for the price or skip.")

    # Asks user to input the quantity on hand of the product or skip. Skip stores quantity as none. 
    while True: 
        quantity_input = input("Please enter the quantity on hand of this product or enter 'skip'.")
        if quantity_input.lower().strip() == "skip":
            quantity = None
            break
        try: 
            quantity = int(quantity_input)
            break
        except ValueError:
            print("Please enter an integer for the quantity on hand or skip.")

    # Asks user to input the reorder level (1-10) of the product. Skip stores reorder level as not determined. 
    # 1 is low, 10 is highest
    while True:
        reorder_input = input("Please enter the reorder level of this product or enter 'skip'. 1 is the lowest and 10 is the highest.")
        if reorder_input.lower().strip() == "skip":
            reorder = "Not determined"
            break
        try:
            reorder_value = int(reorder_input)
            if 1 <= reorder_value <= 10:
                reorder = int(reorder_value)
                break
            else: 
                print("Invalid input. Please enter a number 1 to 10. Or enter skip to skip.")
        except ValueError:
            print("Please enter an integer or skip.")

    # Asks user to input supplier name or skip 
    supplier_input = input("Please enter the supplier of this product or enter 'skip'.")
    if supplier_input.lower().strip() == "skip":
        supplier = None
        break
    else:
        supplier = str(supplier_input)
        break

    # Stores the inputs in the designated product dictionary for future reference
    product_lines[selected_product_line][selected_product]["product_id"] = product_id
    product_lines[selected_product_line][selected_product]['sku'] = sku
    product_lines[selected_product_line][selected_product]['price'] = price
    product_lines[selected_product_line][selected_product]['quantity'] = quantity 
    product_lines[selected_product_line][selected_product]['supplier'] = supplier
    product_lines[selected_product_line][selected_product]['reorder_level'] = reorder

    # Stores current time as time last updated
    product_lines[selected_product_line][selected_product]['last_updated'] = get_current_timestamp()

def remove_product_details():
    pass

def edit_product_details():
    pass


# In[ ]:


def update_inventory()


# In[ ]:


def show_best_sellers()


# In[ ]:


# CLI menu 
def main_menu():
    while True:
        print("Inventory Management Menu")
        print("1. Adjust product line")
        print("2. Adjust product")
        print("3. Update inventory")
        print("4. Show best sellers")
        print("5. Exit")

        choice = input("Enter the number of what you would like to do.")

        # Gives options for adjusting product line
        if choice == "1":
            while True:
                product_line_choice = input("Would you like to add, remove or edit a product line? Or type back to return to menu.")
                product_line_choice_clean = product_line_choice.strip().lower()
                if product_line_choice_clean == "add":
                    add_product_line()
                elif product_line_choice_clean == "remove":
                    remove_product_line()
                elif product_line_choice_clean == "edit":
                    edit_product_line_()
                elif product_line_choice_clean == "back":
                    break # Exits sub menu and goes back to main menu
                else: 
                    print("Please enter 'add', 'remove', or 'edit'")

        # Gives options for adjusting product
        elif choice == "2":
            while True:
                product_choice = input("Would you like to add, remove, or edit a product? Or type back to return to the main menu.")
                product_choice_clean = product_choice.strip().lower()
                if product_choice_clean == "add":
                    add_product()
                elif product_choice_clean == "remove":
                    remove_product()
                elif product_choice_clean == "edit":
                    choice = input("Would like to edit product name or details. Please enter 'name' or 'details'")
                    choice_clean = choice.strip().lower()
                    if choice_clean == "name":
                        edit_product_name()
                    elif choice_clean == "details":
                        edit_product_details()
                    else:
                        print("Invalid input. Try again.")
                        continue
                elif product_choice_clean == "back":
                    break # Exits sub menu and goes back to main menu
                else:
                    print("Please enter 'add', 'remove', or 'edit'")

        # Takes user to sub menu to update inventory
        elif choice == "3":
            update_inventory()

        # Shows user best sellers
        elif choice == "4":
            show_best_sellers()

        # Exits the menu
        elif choice == "5":
            print("Have a nice day.")
            break

        # Loops back to the main menu if user enters an invalid input         
        else:
            print("Invalid choice. Please try again.")
            
main_menu() # Runs the main menu


# In[ ]:




