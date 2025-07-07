Simple Inventory Management System

This is a simple command-line based inventory management program written in Python. It enables users to manage an inventory of items by allowing them to add new items, update existing ones, delete items, view details of a specific item, or display the entire inventory. It operates through a text-based menu that continuously prompts the user until they choose to exit the program.

The inventory is stored in memory using a Python dictionary where the item names serve as keys, and each value is a list containing two elements: the quantity of the item and its price. For example, an item `"apple"` with quantity `10` and price `2` would be stored as `inventory["apple"] = [10, 2]`.

When the script is run, it presents the user with a menu that includes five options: adding an item, removing an item, updating an item, viewing a specific item, and exiting the program. Based on the user's selection, the appropriate function is executed. After any add, delete, or update operation, the entire inventory is shown to reflect the current state.

The program uses simple `input()` calls to interact with the user. It assumes that inputs for quantity and price will always be valid integers; if not, it may raise an error.

Please note that this system is non-persistent — all data is lost once the script ends, as it does not currently save data to a file or database. Future improvements could include adding file storage, improving input validation, making item names case-insensitive, or building a graphical interface for easier use.

This program is intended for educational purposes or very basic inventory management tasks. It’s a great starting point for anyone learning Python and looking to practice working with dictionaries, loops, and basic input/output.

---

Let me know if you want this content saved as a `.txt` or `.md` file, or if you'd like help improving or expanding the code.
