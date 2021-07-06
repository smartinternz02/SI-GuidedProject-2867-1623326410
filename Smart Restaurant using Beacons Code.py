#Intelligent Restaurant program
print("\t\t\t**Smart Restaurant**")
print("*Menu\n1.Starters\n2.Side Dishes\n3.Main Course\n4.Dessert")
option=int(input('Enter any option showing above : '))
cost=0
def hotel_menu(option):
    if option == 1:
        print("Starters Menu")
        print("1.Spring Rolls-Rs.50\n2.Tomato Bruschetta-Rs.70\n3.French Onion Soup-Rs.80")
        price=[50,70,80]
        while True:
          option_1=int(input('Entered Starters option do you want to Continue : '))
          print('Your cost of food is : Rs.',cost+price[option_1-1])
          break
    elif option == 2:
        print("Side Dishes Menu")
        print("1.French Fries  Rs.100\n 2.Garlic Bread Rs.110\n 3.Mixed green Salad Rs.100")
        price=[100,110,100]
        while True:
          option_1=int(input('Entered Sidedishes option do you want to Continue : '))
          print('Your cost of food is : Rs.',cost+price[option_1-1])
          break
    elif option == 3:
        print("Main Course Menu")
        print("1.Chicken Biryani Rs.150\n 2.veg thaali Rs.150\n 3.Mutton Biryani Rs.180")
        price=[150,150,180]
        while True:
          option_1=int(input('Entered Main Course option do you want to Continue : '))
          print('Your cost of food is : Rs.',cost+price[option_1-1])
          break
    elif option == 4:
        print("Desserts Menu")
        print("1.Apple Pie Cream Rs.80\n 2.Fruit Salad Rs.50")
        price=[80,50]
        while True:
          option_1=int(input('Entered Desserts option do you want To Continue : '))
          print('Your cost of food is : Rs.',cost+price[option_1-1])
          break
    else:
      print('Invalid option')
    print("Do you want to order again ? (yes/No)")
    order_again=input()
    if order_again=='y':
      print("*Menu\n1.Starters\n2.Side Dishes\n3.Main Course\n4.Desserts")
      option=int(input('Enter any option showing above : ')) 
      hotel_menu(option)
    elif order_again=='n':
      print("Thank You for coming Have a nice day")
    else:
      print("Invalid option")
      print("Thanks for coming")
hotel_menu(option)
