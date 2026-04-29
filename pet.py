# class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)


# # #### 🧍‍♀️ Creating a Hero

# labubu = Hero("Jillian", 150, ["Potion"])
# ```

# * We just made a new **Hero object** named Jillian!
# * Jillian starts with **$150** and one **Potion**.

# #### 💰 Buying an Item

# ```python
# Jillian.buy({"title": "Sword", "atk": 34})
# print(Jillian.__dict__)
# ```

# When Jillian buys something:

# * The item is added to her inventory list.
# * The inventory is printed.
# * `__dict__` shows all her data stored in a dictionary format.

# ---

# ## 🔒 4. Encapsulation: Protecting Data

# Encapsulation means **keeping related data and methods inside a single unit (the class)** — and **controlling how outside code interacts** with that data.

# ### Analogy:

# > Imagine the Hero’s backpack is zipped shut 🎒.
# > Only the Hero knos how to open it properly (using their methods).
# > You don’t just reach in and mess with it directly!

# In Python, we can use **naming conventions** to mark variables as “private” (for internal use only).


# ```python
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")
# ```

# This way, no one outside the class should directly do `my_account.__balance = 0`.
# They should use the **methods** (`deposit`, `show_balance`) instead.

# ---

# ## 🧠 5. Practice Time

# ### ✏️ Activity 1 – Create Your Own Hero

# Make your own hero object with a name, starting money, and one item.

# Then, use `.buy()` to add another item to your inventory.

# ### ✏️ Activity 2 – Add Encapsulation

# Create a class `Pet` that has:


# * A **private variable** for happiness level (e.g., `__happiness`)
# * A method to **play()** that increases happiness
# * A method to **show_status()** that prints how happy the pet is

import random

print("Welcome to the pet store! Please customize your pet")

name = input("What's your pet's name? ")
pet_type = input("What type of pet would you like? (active, calm, lazy, fun): ")
money = int(input("How much money does your pet have? "))


class Pet:
    def __init__(self, name, happiness=50, hunger=50, energy = 0, water=50):
        self.name = name
        self.__happiness = happiness  
        self.hunger = hunger
        self.water = water
        self.energy = energy
        self.inventory = []

    def play(self, minutes=5):
        if self.__happiness < 100:
            gained = minutes * 2
            self.__happiness += gained
            print(f"{self.name} played and gained {gained} happiness! Here is the new status:{self.__happiness}")
        
        if self.__happiness >= 100:
            print(f"{self.name} is too happy, no more playing.")

    def feed(self):
        if self.hunger < 100:
            self.hunger += 10
            print(f"{self.name} has been fed. Here is the new status:{self.hunger}")
        if self.hunger >= 100: 
            print(f"{self.name} is full.")

    def sleep(self):
        if self.energy < 100:
            self.energy += 50
            print(f"{self.name} slept for 5 hours. Here is the new status:{self.energy}" )
        if self.energy >= 100: 
            print(f"{self.name} is not tired.")

    def give_water(self):
        if self.water < 100:
            self.water += 10
            print(f"{self.name} drank some water. Here is the new status:{self.water}")
        if self.water >= 100: 
            print(f"{self.name} is not thursty.")


    def show_status(self):
        print("\n--- PET STATUS ---")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Water: {self.water}")
        print(f"Happiness: {self.__happiness}")
        print(f"Energy: {self.energy}")
        print(f"Inventory: {self.inventory}")



class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(f"{self.name}'s inventory: {self.inventory}")



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")



pet = Pet(name)
player = Hero(name, money, ["Starter Toy"])

print("\nThank you for purchasing a pet!")
pet.show_status()



while True:
    print("\nWhat would you like to do?")
    print("1. Play")
    print("2. Feed")
    print("3. Give Water")
    print("4. Buy Item")
    print("5. Sleep")
    print("6. Show Stats")
    print("7. Quit")

    choice = input("> ")

    if choice == "1":
        pet.play()

    elif choice == "2":
        pet.feed()

    elif choice == "3":
        pet.give_water()

    elif choice == "4":
        item = input("Enter item name: ")
        player.buy(item)
        pet.inventory.append(item)

    elif choice == "5":
        pet.sleep()

    elif choice == "6":
        pet.show_status()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")