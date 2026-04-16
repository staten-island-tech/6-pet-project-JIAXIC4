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
# > Only the Hero knows how to open it properly (using their methods).
# > You don’t just reach in and mess with it directly!

# In Python, we can use **naming conventions** to mark variables as “private” (for internal use only).

# Example:

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
# 🧍‍♀️ Hero Class
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(f"{self.name}'s inventory: {self.inventory}")


# #### 🧍‍♀️ Creating a Hero
labubu = Hero("fluffy", 150, ["Potion"])

# #### 💰 Buying an Item
labubu.buy({"title": "Sword", "atk": 34})
print(labubu.__dict__)


# ---


# 🔒 Encapsulation Example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")


account = BankAccount("fluffy", 500)
account.deposit(200)
account.show_balance()


# ---

# 🐾 Pet Class (Encapsulation Practice)
class Pet:
    def __init__(self, name, happiness=50):
        self.name = name
        self.__happiness = happiness

    def play(self, minutes=5):
        """Play with the pet to increase happiness."""
        gained = minutes * 2
        self.__happiness += gained
        print(f"{self.name} played for {minutes} minutes and gained {gained} happiness.")

    def show_status(self):
        """Print the pet's current happiness."""
        print(f"{self.name}'s happiness: {self.__happiness}")


# 🧠 Testing Pet
fluffy = Pet("Fluffy")
fluffy.show_status()
fluffy.play(10)
fluffy.show_status()
