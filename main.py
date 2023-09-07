from classes import AddressBook, Record, Name, Phone, Birthday
import functools

help = """
Available commands:
hello: print \"How can I help you?\"
add [name] [phone] [birthday]: Add a new record to address book or new phone to contact phone list
add birthday [name] [birthday]: Add a new/change Birthday to the contact of address book
to birthday [name]: Show days to contact`s Birthday
change [name] [old_phone] [new_phone]: Change phone num for contact in address book
phone [name]: Show phone list of contact
show all: Show address book
pages [size]: Show address book in pages, size is number records per page
good bye, close, exit: print \"Good bye!\" and exit
help: Show this help
"""

address_book = AddressBook()


def input_error(func):

    @functools.wraps(func)
    def inner(param_list):

        if func.__name__ == "phone":
            if len(param_list) > 0:
                result = func(param_list)
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 argument: name.\nFor example: {func.__name__} [name]\n\nTRY AGAIN!!!"""
        elif func.__name__ == "add":
            if len(param_list) > 0:
                result = func(param_list)
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 or 2 arguments: name and phone.\nFor example: {func.__name__} [name] - To add a new contact without phones\nFor example: {func.__name__} [name] [phone] - To add a new contact with phones, or add new phone to contact\n\nTRY AGAIN!!!"""
        elif func.__name__ == "add_birthday":
            param_list.pop(0)
            if len(param_list) > 1:
                result = func(param_list)
            else:
                result = f"""Command \"{func.__name__.replace("_", " ")}\" reqired 2 arguments: name and birthday.\nFor example: {func.__name__.replace("_", " ")} [name] [birthday]\n\nTRY AGAIN!!!"""

        elif func.__name__ == "change":
            if len(param_list) > 2:
                result = func(param_list)
            else:
                result = f"""Command \"{func.__name__}\" reqired 3 arguments: name, phone and new_phone.\nFor example: {func.__name__} [name] [phone] [new_phone]\n\nTRY AGAIN!!!"""
        elif func.__name__ == "to_birthday":
            param_list.pop(0)
            if len(param_list) > 0:
                result = func(param_list)
            else:
                result = f"""Command \"{func.__name__.replace("_", " ")}\" reqired 1 argument: name.\nFor example: {func.__name__.replace("_", " ")} [name]\n\nTRY AGAIN!!!"""
        elif func.__name__ == "pages":
            if len(param_list) > 0 and int(param_list[0]) > 0:
                result = func(param_list)
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 argument: size. Size int and must be > 0.\nFor example: {func.__name__} [size]\n\nTRY AGAIN!!!"""

        return result
    return inner
    

@input_error
def add(param_list):

    name = Name(None)
    phone = Phone(None)
    birthday = Birthday(None)

    if len(param_list) == 1:
        try:
            name.value = param_list[0]
        except ValueError as e:
            result = str(e)
            return result
    elif len(param_list) == 2:
        try:
            name.value = param_list[0]
        except ValueError as e:
            result = str(e)
            return result
        try:
            phone.value = param_list[1]
        except ValueError as e:
            result = str(e)
            return result
    elif len(param_list) > 2:
        try:
            name.value = param_list[0]
        except ValueError as e:
            result = str(e)
            return result
        try:
            phone.value = param_list[1]
        except ValueError as e:
            result = str(e)
            return result
        try:
            birthday.value = param_list[2]
        except ValueError as e:
            result = str(e)
            return result

    if phone.value != None:    
        result = address_book.add_record(Record(name, phone=phone, birthday=birthday)) 
    else:
        result = address_book.add_record(Record(name, birthday=birthday))

    return result


@input_error
def add_birthday(param_list):

    name = Name(None)
    birthday = Birthday(None)
    try:
        name.value = param_list[0]
    except ValueError as e:
        result = str(e)
        return result
    try:
        birthday.value = param_list[1]
    except ValueError as e:
        result = str(e)
        return result
    
    result = address_book.add_birthday(Record(name, birthday=birthday))
    

@input_error
def change(param_list):

    record = Record(Name(param_list[0]))
    old_phone_obj = Phone(param_list[1])
    new_phone_obj = Phone(None)
    try:
        new_phone_obj.value = param_list[2]
    except ValueError as e:
        result = str(e)
        return result

    if address_book.is_contact_exist(record):
        result = address_book[param_list[0]].change_phone(old_phone_obj, new_phone_obj)
    else:
        result = f"Contact \"{param_list[0]}\" does not exist in the address book\n"
    
    return result


@input_error
def add_birthday(param_list):

    record = Record(Name(param_list[0]))
    birthday = Birthday(param_list[1])
    if address_book.is_contact_exist(record):
        result = address_book[param_list[0]].add_birthday(birthday)
    else:
        result = f"Contact \"{param_list[0]}\" does not exist in the address book\n"
    
    return result


@input_error
def phone(param_list):

    name = param_list[0]
    record = Record(Name(param_list[0]), None)
    if address_book.is_contact_exist(record):
        phone_list = address_book[name].phones
        value_list = []
        for phone_obj in phone_list:
            value_list.append(phone_obj.value)
        result = f"Phone list of contact \"{name}\" is \"{value_list}\"\n"
    else:
        result = f"Contact \"{name}\" does not exist in the address book\n"

    return result


@input_error
def to_birthday(param_list):

    record = Record(Name(param_list[0]))
    if address_book.is_contact_exist(record):
        result = address_book[param_list[0]].days_to_birthday()
    else:
        result = f"Contact \"{param_list[0]}\" does not exist in the address book\n"
    
    return result


def hello(param_list):

    result = "How can I help you?\n"
    return result


def exit(param_list):

    result = "exit"
    return result


def show_all(param_list):

    result = "All contacts:\n"
    for name, record in address_book.data.items():
        phones = record.phones
        birthday = record.birthday.value
        phone_values = []
        for phone in phones:
            phone_values.append(phone.value)
        result += f"Name: \"{name}\", Phones: {phone_values}, Birthday: [{birthday}]\n"

    return result


@input_error
def pages(param_list):
    size = int(param_list[0])
    result = address_book.get_pages(page_size=size)

    return result


def helper(param_list):
    
    return help


commands = {
        "good bye": exit,
        "close": exit,
        "exit": exit,
        "show all": show_all,
        "show_all": show_all,
        "hello": hello,
        "add birthday": add_birthday,
        "add_birthday": add_birthday,
        "add": add,
        "change": change,
        "phone": phone,
        "to birthday": to_birthday,
        "to_birthday": to_birthday,
        "help": helper,
        "helper": helper,
        "pages": pages
    }


def parser(string: str):

    lower_string = string.lower()
    for keyword, command in commands.items():
        if keyword in lower_string:
            param_list = string.split()
            for param in param_list:
                if param.lower() in keyword:
                    param_list.remove(param)
                    command = command.__name__
            return command, param_list

    return None, ""


def handler(command):

    return commands[command]


def main():

    while True:
        source_command = input("Enter command: ")
        command, param_list = parser(source_command)
        if not command:
            print(f"YOU ENTERED A WRONG COMMAND!!!\n{help}\nTRY AGAIN!!!")
            continue
        result = handler(command)(param_list)
        if result == 'exit':
            print("Good bye!")
            break
        else:
            print(result)


if __name__ == "__main__":
    main()