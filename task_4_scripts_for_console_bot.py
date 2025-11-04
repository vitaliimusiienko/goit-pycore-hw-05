def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено"
        except ValueError:
            return "Для команди потрібно два аргументи ім'я та номер телефону"
        except IndexError:
            return "Введіть ім'я будь-ласка"

    return inner


@input_error
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано"


@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Контакт оновлено"


@input_error
def show_phone(args, contacts: dict):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts: dict):
    return contacts
