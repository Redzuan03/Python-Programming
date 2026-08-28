import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "Fried Calamari" : 10,
    "Beach Burger" : 14,
    "Salmon Wonder" : 23,
    "Shrimp Tacos" : 15,
    "Sushi Platter" : 25,
    "Empanadas" : 10,
}

root  = Tk()

root.title("TTC - Binary Restaurant")

# ------------------------------------FUNCTIONS--------------------------------------------- #

#region Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # List of numbers
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']  # List of letters
    order_id = "BIN_"  # Initial order ID string
    random_letters = ""  # Empty string to store random letters
    random_digits = ""  # Empty string to store random digits
    for i in range(0,3):  # Loop three times
        random_letters += random.choice(letters)  # Append a random letter to random_letters
        random_digits += str(random.choice(numbers))  # Append a random digit to random_digits

    order_id += random_letters + random_digits  # Concatenate order_id with random_letters and random_digits
    return order_id  # Return the generated order ID
#endregion

#region Add to Order Button
def add():
    # Updating the transaction label
    current_order = orderTransaction.cget("text")  # Get the current text of the transaction label
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "  # Create the text for the added dish
    updated_order = current_order + added_dish  # Concatenate the current order and the added dish
    orderTransaction.configure(text=updated_order)  # Update the text of the transaction label

    # Updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")  # Get the current order total
    order_total = order_total.replace("$", "")  # Remove the dollar sign from the order total
    updated_total = int(order_total) + prices[displayLabel.cget("text")]  # Calculate the updated order total
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")  # Update the text of the order total label
#endregion

#region Remove Button Function
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])  # Get the text of the dish to remove
    transaction_list = orderTransaction.cget("text").split("$ ")  # Split the transaction label text into a list
    transaction_list.pop(len(transaction_list) - 1)  # Remove the last empty item from the list

    if dish_to_remove in transaction_list:  # Check if the dish to remove is in the transaction list
        # Update transaction label
        transaction_list.remove(dish_to_remove)  # Remove the dish to remove from the transaction list
        updated_order = ""  # Empty string to store the updated order
        for item in transaction_list:  # Iterate over the items in the transaction list
            updated_order += item + "$ "  # Append each item to the updated order with a dollar sign

        orderTransaction.configure(text=updated_order)  # Update the text of the transaction label

        # Update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")  # Get the current order total
        order_total = order_total.replace("$", "")  # Remove the dollar sign from the order total
        updated_total = int(order_total) - prices[displayLabel.cget("text")]  # Calculate the updated order total
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")  # Update the text of the order total label


#endregion

#region Display Button Functions
def displayCalamari():
    # Set the style of the calamari dish frame
    calamariDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    # Set the style of other dish frames to the default style
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")

    # Configure the display label for calamari dish
    displayLabel.configure(
        image=calamariImage,  # Set the image for calamari dish
        text="Fried Calamari",  # Set the text for calamari dish
        font=('Helvetica', 14, "bold"),  # Set the font for the text
        foreground="white",  # Set the text color
        compound="bottom",  # Set the image and text arrangement
        padding=(5, 5, 5, 5),  # Set the padding around the label
    )

def displayBurger():
    # Set the style of the burger dish frame
    burgerDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    # Set the style of other dish frames to the default style
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    # Configure the display label for the burger dish
    displayLabel.configure(
        text="Beach Burger",  # Set the text for the burger dish
        font=('Helvetica', 14, "bold"),  # Set the font for the text
        foreground="white",  # Set the text color
        image=burgerImage,  # Set the image for the burger dish
        compound="bottom",  # Set the image and text arrangement
        padding=(5, 5, 5, 5),  # Set the padding around the label
    )


def displaySalmon():
    # Set the style of the salmon dish frame
    salmonDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    # Set the style of other dish frames to the default style
    calamariDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    # Configure the display label for the salmon dish
    displayLabel.configure(
        text="Salmon Wonder",  # Set the text for the salmon dish
        font=('Helvetica', 14, "bold"),  # Set the font for the text
        foreground="white",  # Set the text color
        image=salmonImage,  # Set the image for the salmon dish
        compound="bottom",  # Set the image and text arrangement
        padding=(5, 5, 5, 5),  # Set the padding around the label
    )

def displayTacos():
    # Set the style of the shrimp dish frame
    shrimpDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    # Set the style of other dish frames to the default style
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    # Configure the display label for the shrimp dish
    displayLabel.configure(
        text="Shrimp Tacos",  # Set the text for the shrimp dish
        font=('Helvetica', 14, "bold"),  # Set the font for the text
        foreground="white",  # Set the text color
        image=shrimpImage,  # Set the image for the shrimp dish
        compound="bottom",  # Set the image and text arrangement
        padding=(5, 5, 5, 5),  # Set the padding around the label
    )

def displayEmpanadas():
    # Set the style of the empanadas dish frame
    empanadasDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    # Set the style of other dish frames to the default style
    salmonDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    # Configure the display label for the empanadas dish
    displayLabel.configure(
        text="Empanadas",  # Set the text for the empanadas dish
        font=('Helvetica', 14, "bold"),  # Set the font for the text
        foreground="white",  # Set the text color
        image=empanadasImage,  # Set the image for the empanadas dish
        compound="bottom",  # Set the image and text arrangement
        padding=(5, 5, 5, 5),  # Set the padding around the label
    )

def displaySushi():
    # Set the style of the sushi dish frame
    sushiDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
    # Set the style of other dish frames to the default style
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    # Configure the display label for the sushi dish
    displayLabel.configure(
        image=sushiImage,  # Set the image for the sushi dish
        text="Sushi Platter",  # Set the text for the sushi dish
        font=('Helvetica', 14, "bold"),  # Set the font for the text
        foreground="white",  # Set the text color
        compound="bottom",  # Set the image and text arrangement
        padding=(5, 5, 5, 5),  # Set the padding around the label
    )
#endregion

#region Generating Receipt from Order Button
def order():
    new_receipt = orderIDLabel.cget("text")  # Get the text of the order ID label
    new_receipt = new_receipt.replace("ORDER ID : ", "")  # Remove the "ORDER ID: " prefix from the order ID
    transaction_list = orderTransaction.cget("text").split("$ ")  # Split the transaction label text into a list
    transaction_list.pop(len(transaction_list) - 1)  # Remove the last empty item from the list

    order_day = date.today()  # Get the current date
    order_time = datetime.now()  # Get the current time

    for item in transaction_list:  # Iterate over the items in the transaction list
        item += "$ "  # Append a dollar sign to each item

    with open(new_receipt, 'w') as file:  # Open the receipt file in write mode
        file.write("The Binary")  # Write the restaurant name
        file.write("\n")
        file.write("________________________________________________________")  # Write a separator
        file.write("\n")
        file.write(order_day.strftime("%x"))  # Write the order date
        file.write("\n")
        file.write(order_time.strftime("%X"))  # Write the order time
        file.write("\n\n")
        for item in transaction_list:  # Iterate over the items in the transaction list
            file.write(item + "\n")  # Write each item to the file
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))  # Write the order total

    orderTotalLabel.configure(text="TOTAL : 0$")  # Reset the order total label
    orderIDLabel.configure(text="ODER ID: " + ORDER_ID())  # Generate a new order ID
    orderTransaction.configure(text="")  # Clear the transaction label

#endregion

# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style() # Set the style for different widgets using ttk.Style()
# Configure the styles for different frames
s.configure('MainFrame.TFrame', background="#2B2B28")  # Styling for the main frame
s.configure('MenuFrame.TFrame', background="#4A4A48")  # Styling for the menu frame
s.configure('DisplayFrame.TFrame', background="#0F1110")  # Styling for the display frame
s.configure('OrderFrame.TFrame', background="#B7C4CF")  # Styling for the order frame
s.configure('DishFrame.TFrame', background="#4A4A48", relief="raised")  # Styling for the dish frame
s.configure('SelectedDish.TFrame', background="#C4DFAA")  # Styling for the selected dish frame
# Configure the styles for different labels
s.configure('MenuLabel.TLabel',
            background="#0F1110",
            font=("Arial", 13, "italic"),
            foreground="white",
            padding=(5, 5, 5, 5),
            width=21
            )  # Styling for the menu label
s.configure('orderTotalLabel.TLabel',
            background="#0F1110",
            font=("Arial", 10, "bold"),
            foreground="white",
            padding=(2, 2, 2, 2),
            anchor="w"
            )  # Styling for the order total label
s.configure('orderTransaction.TLabel',
            background="#4A4A48",
            font=('Helvetica', 12),
            foreground="white",
            wraplength=170,
            anchor="nw",
            padding=(3, 3, 3, 3)
            )  # Styling for the order transaction label


# endregion

# region Images
# Top Banner images
LogoImageObject = Image.open("Images/Binary Logo.png").resize((130, 130))  # Load and resize the logo image
LogoImage = ImageTk.PhotoImage(LogoImageObject)  # Create a PhotoImage object from the logo image

TopBannerImageObject = Image.open("Images/restaurant top banner.jpg").resize((800, 130))  # Load and resize the top banner image
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)  # Create a PhotoImage object from the top banner image

displayDefaultImageObject = Image.open("Images/display - Default.png").resize((350, 360))  # Load and resize the default display image
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)  # Create a PhotoImage object from the default display image

calamariImageObject = Image.open("Images/menu/fried calamari.png").resize((350, 334))  # Load and resize the calamari dish image
calamariImage = ImageTk.PhotoImage(calamariImageObject)  # Create a PhotoImage object from the calamari dish image

burgerImageObject = Image.open("Images/menu/beach burger.png").resize((350, 334))  # Load and resize the burger dish image
burgerImage = ImageTk.PhotoImage(burgerImageObject)  # Create a PhotoImage object from the burger dish image

salmonImageObject = Image.open("Images/menu/salmon wild rice.png").resize((350, 334))  # Load and resize the salmon dish image
salmonImage = ImageTk.PhotoImage(salmonImageObject)  # Create a PhotoImage object from the salmon dish image

shrimpImageObject = Image.open("Images/menu/shrimp tacos.png").resize((350,334))
shrimpImage = ImageTk.PhotoImage(shrimpImageObject)

sushiImageObject = Image.open("Images/menu/sushi platter.png").resize((350, 334))  # Load and resize the sushi dish image
sushiImage = ImageTk.PhotoImage(sushiImageObject)  # Create a PhotoImage object from the sushi dish image

empanadasImageObject = Image.open("Images/menu/empanadas.png").resize((350, 334))  # Load and resize the empanadas dish image
empanadasImage = ImageTk.PhotoImage(empanadasImageObject)  # Create a PhotoImage object from the empanadas dish image


#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')  # Main frame of the application
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)  # Frame for the top banner
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')  # Frame for the menu section
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")  # Frame for the display section
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")  # Frame for the order section
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
calamariDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")  # Frame for the calamari dish
calamariDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

burgerDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")  # Frame for the burger dish
burgerDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

salmonDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")  # Frame for the salmon dish
salmonDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

shrimpDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")  # Frame for the shrimp dish
shrimpDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

sushiDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")  # Frame for the sushi dish
sushiDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

empanadasDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")  # Frame for the empanadas dish
empanadasDishFrame.grid(row = 6, column = 0, sticky ="NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")  # Label for the logo image
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")  # Label for the restaurant banner image
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

# region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")  # Label for the menu title
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

CalamariDishLabel = ttk.Label(calamariDishFrame, text ="Fried Calamari ..... 10$", style ="MenuLabel.TLabel")  # Label for the calamari dish
CalamariDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

BurgerDishLabel = ttk.Label(burgerDishFrame, text ="Beach Burger ..... 14$", style ="MenuLabel.TLabel")  # Label for the burger dish
BurgerDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SalmonDishLabel = ttk.Label(salmonDishFrame, text ="Salmon Wonder ..... 23$", style ="MenuLabel.TLabel")  # Label for the salmon dish
SalmonDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

ShrimpDishLabel = ttk.Label(shrimpDishFrame, text ="Shrimp Tacos ..... 15$", style ="MenuLabel.TLabel")  # Label for the shrimp dish
ShrimpDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

SushiDishLabel = ttk.Label(sushiDishFrame, text ="Sushi Platter ..... 25$", style ="MenuLabel.TLabel")  # Label for the sushi dish
SushiDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

EmpanadasDishLabel = ttk.Label(empanadasDishFrame, text ="Empanadas .... 10$", style ="MenuLabel.TLabel")  # Label for the empanadas dish
EmpanadasDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

# Buttons
CalamariDisplayButton = ttk.Button(calamariDishFrame, text ="Display", command = displayCalamari)  # Button to display calamari dish
CalamariDisplayButton.grid(row = 0, column = 1, padx = 10)

BurgerDisplayButton = ttk.Button(burgerDishFrame, text ="Display", command = displayBurger)  # Button to display burger dish
BurgerDisplayButton.grid(row = 0, column = 1, padx = 10)

SalmonDisplayButton = ttk.Button(salmonDishFrame, text ="Display", command = displaySalmon)  # Button to display salmon dish
SalmonDisplayButton.grid(row = 0, column = 1, padx = 10)

ShrimpDisplayButton = ttk.Button(shrimpDishFrame, text ="Display", command = displayTacos)  # Button to display shrimp dish
ShrimpDisplayButton.grid(row = 0, column = 1, padx = 10)

SushiDisplayButton = ttk.Button(sushiDishFrame, text ="Display", command = displaySushi)  # Button to display sushi dish
SushiDisplayButton.grid(row = 0, column = 1, padx = 10)

EmpanadasDisplayButton = ttk.Button(empanadasDishFrame, text ="Display", command = displayEmpanadas)  # Button to display empanadas dish
EmpanadasDisplayButton.grid(row = 0, column = 1, padx = 10)

# endregion

# region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")  # Label for the order title
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())  # Label for the order ID
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')  # Label for the order transaction
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")  # Label for the order total
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)  # Button to place the order
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)  # Label for the display image
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)  # Button to add item to the order
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)  # Button to remove item from the order
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

# endregion

#----------------------------- GRID CONFIGURATIONS -------------------------------------------#

# Configuring the grid layout for the mainFrame
mainFrame.columnconfigure(2, weight = 1)  # The 3rd column expands horizontally when the window is resized
mainFrame.rowconfigure(1, weight = 1)     # The 2nd row expands vertically when the window is resized

# Configuring the grid layout for the menuFrame
menuFrame.columnconfigure(0, weight = 1)  # The 1st column expands horizontally when the window is resized
menuFrame.rowconfigure(1, weight = 1)     # The 2nd row expands vertically when the window is resized
menuFrame.rowconfigure(2, weight = 1)     # The 3rd row expands vertically when the window is resized
menuFrame.rowconfigure(3, weight = 1)     # The 4th row expands vertically when the window is resized
menuFrame.rowconfigure(4, weight = 1)     # The 5th row expands vertically when the window is resized
menuFrame.rowconfigure(5, weight = 1)     # The 6th row expands vertically when the window is resized
menuFrame.rowconfigure(6, weight = 1)     # The 7th row expands vertically when the window is resized

# Configuring the grid layout for the orderFrame
orderFrame.columnconfigure(0, weight = 1)  # The 1st column expands horizontally when the window is resized
orderFrame.rowconfigure(2, weight = 1)     # The 3rd row expands vertically when the window is resized




root.mainloop()# The `mainloop` function is called to start the main event loop of the Tkinter application.
