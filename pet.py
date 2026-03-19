class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

# #### 🧍‍♀️ Creating a Hero

labubu = Hero("Jillian", 150, ["Potion"])
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

# * A **name**
# * A **private variable** for happiness level (e.g., `__happiness`)
# * A method to **play()** that increases happiness
# * A method to **show_status()** that prints how happy the pet is
