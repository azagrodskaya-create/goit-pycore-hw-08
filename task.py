import pickle
from typing import List, Dict, Optional


class Record:
    def __init__(self, name: str): # Ініціалізація запису з ім'ям та порожнім списком телефонів
        self.name: str = name
        self.phones = []

    def add_phone(self, phone: str): # Додавання телефону до запису
        self.phones.append(phone)

    def __str__(self) -> str: # Створення рядкового представлення запису для виводу
        return f"Contact name: {self.name}, phones: {'; '.join(self.phones)}"


class AddressBook(dict):
    def add_record(self, record) -> None: # Додавання запису до адресної книги
        self.grid_data = self[record.name] = record

# ---  Функції для роботи з файлами (Pickle) ---

def save_data(book, filename="addressbook.pkl") -> AddressBook: # Зберігає адресну книгу у файл
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    return book

def load_data(filename="addressbook.pkl") -> AddressBook: # Завантажує дані. Якщо файлу немає — створює нову книгу.
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        # EOFError додано на випадок, якщо файл порожній
        return AddressBook()

# --- Головна функція  ---

def main(): # Головна функція, яка запускає бота та обробляє команди користувача
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("\nEnter a command: ").strip().lower()
        
        if not user_input:
            continue


        parts = user_input.split() # Розділяємо введений рядок на команду та аргументи
        command = parts[0]
        args = parts[1:]

        if command in ["close", "exit"]: # Команди для виходу з програми
            save_data(book)
            print("Good bye! All data is safely saved.")
            break

        elif command == "add": # Команда для додавання або оновлення контакту
            if len(args) >= 2:
                name, phone = args[0], args[1]
                if name not in book:
                    record = Record(name)
                    book.add_record(record)
                book[name].add_phone(phone)
                print(f"Contact {name} added/updated.")
            else:
                print("Error: Give me name and phone please.")

        elif command == "all": # Команда для виводу всіх контактів у адресній книзі
            if not book:
                print("Address book is empty.")
            for name, record in book.items():
                print(record)

        else: # Якщо команда не розпізнана, виводимо повідомлення про помилку
            print("Invalid command. Try 'add', 'all' or 'exit'.")

if __name__ == "__main__":
    main()