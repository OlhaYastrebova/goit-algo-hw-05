import sys

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Insufficient arguments."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

contacts = {}

@input_error
def add_contact(args):
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(args):
    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated with new phone number {new_phone}."
    else:
        raise KeyError

@input_error
def show_phone(args):
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError

@input_error
def show_all():
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command. Available commands: hello, add, change, phone, all, close, exit")

if __name__ == "__main__":
    main()

