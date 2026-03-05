import pickle

# --- 1. Опис класів (Тут твоя логіка) ---

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(self.phones)}"

class AddressBook(dict):
    def add_record(self, record):
        self.grid_data = self[record.name] = record

# --- 2. Функції для роботи з файлами (Pickle) ---

def save_data(book, filename="addressbook.pkl"):
    """Зберігає адресну книгу у файл."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Завантажує дані. Якщо файлу немає — створює нову книгу."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        # EOFError додано на випадок, якщо файл порожній
        return AddressBook()

# --- 3. Головна функція (Main Loop) ---

def main():
    # ЗАВАНТАЖЕННЯ: Це відбувається один раз при старті
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("\nEnter a command: ").strip().lower()
        
        if not user_input:
            continue

        # Розбиваємо ввід на команду та аргументи
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        # ЛОГІКА КОМАНД
        if command in ["close", "exit"]:
            # ЗБЕРЕЖЕННЯ: Перед самим виходом
            save_data(book)
            print("Good bye! All data is safely saved.")
            break

        elif command == "add":
            if len(args) >= 2:
                name, phone = args[0], args[1]
                if name not in book:
                    record = Record(name)
                    book.add_record(record)
                book[name].add_phone(phone)
                print(f"Contact {name} added/updated.")
            else:
                print("Error: Give me name and phone please.")

        elif command == "all":
            if not book:
                print("Address book is empty.")
            for name, record in book.items():
                print(record)

        else:
            print("Invalid command. Try 'add', 'all' or 'exit'.")

if __name__ == "__main__":
    main()