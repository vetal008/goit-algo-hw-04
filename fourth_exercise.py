from colorama import Fore, Style

def user_input(mes_to_user: str):
    first_param, *args = input(mes_to_user).split()
    first_param = first_param.lower()
    # print(first_param)
    return first_param, *args

def add_contact(phone_numbers, *args):
    try:
        if not args[0].isalpha():
            # print(args)
            return Fore.RED + 'Only alpha characters are allowed in [name].' + Style.RESET_ALL
        elif not args[1].isdigit():
            return Fore.RED + 'Only digit numbers are allowed in [phone].' + Style.RESET_ALL
        elif (len(args)) > 2:
            return Fore.RED + "Waiting for 2 params. Instead got more." + Style.RESET_ALL
        else:
            phone_numbers[args[0]] = int(args[1])
            return Fore.YELLOW + 'Contact added.' + Style.RESET_ALL
    except IndexError:
        return Fore.RED +  'Waiting for 2 params([name] [phone])' + Style.RESET_ALL



def change_phone(phone_numbers, *args):
    try:
        if not args[0].isalpha():
            return Fore.RED + 'Only alpha characters are allowed in [name].' + Style.RESET_ALL
        elif not args[1].isdigit():
            return Fore.RED + 'Only digit numbers are allowed in [phone].' + Style.RESET_ALL
        elif (len(args)) > 2:
            return Fore.RED + "Waiting for 2 params. Instead got more." + Style.RESET_ALL
        elif args[0] not in phone_numbers:
            return Fore.RED + 'No contacts with that name.' + Style.RESET_ALL
        else:
            phone_numbers[args[0]] = int(args[1])
            return Fore.YELLOW + 'Contact changed.' + Style.RESET_ALL

    except IndexError:
        return Fore.RED + 'Waiting for 2 params([name] [new phone])' + Style.RESET_ALL

# def show_phone(phone_numbers, *args):




def remove_number(phone_numbers, *args):
    try:
        del phone_numbers[args[0]]
        return Fore.YELLOW + 'Contact removed.' + Style.RESET_ALL
    except IndexError:
        return Fore.RED + 'Waiting for 1 param([name]).' + Style.RESET_ALL
    except KeyError:
        return Fore.RED + 'No contacts with that name.' + Style.RESET_ALL

def help_command():
    help_message = Fore.YELLOW + "Use next commands:\n"  + Style.RESET_ALL + \
    "\t'add' to add a number.(add [name] [number])\n\
    'change' to change number.(change [name] [new number])\n\
    'phone' to get a phone number.(phone [name])\n\
    'all' to get all numbers.\n\
    'remove' to remove a number(remove [name]).\n\
    'close' or 'exit' or 'quit' to exit the bot."
    return help_message


def main():
    phone_numbers = dict()
    print(Fore.BLUE + 'Welcome to my first bot!' + Style.RESET_ALL)
    while True:
        first_param, *args = user_input(Fore.BLUE + 'Enter a command: ' + Style.RESET_ALL)
        # print(first_param, args)
        match first_param:
            case 'greeting':
                print_mes = "Hi! I`m a simple bot which works with phone numbers.\nYou can have some help: write 'help'"
                print(print_mes)
            case 'help':
                print(help_command())
                    # help_message = "Use next commands:\n\
                    #     'add' to add a number.(add [name] [number])\n\
                    #     'change' to change number.(change [name] [new number])\n\
                    #     'phone' to get a phone number.(phone [name])\n\
                    #     'all' to get all numbers.\n\
                    #     'remove' to remove a number(remove [name]).\n\
                    #     'close' or 'exit' or 'quit' to exit the bot."
                    # print(help_message)
            case 'add':
                print(add_contact(phone_numbers, *args))
            case 'change':
                print(change_phone(phone_numbers, *args))
            case 'phone':
                try:
                    print(f"{args[0]} number: {phone_numbers[args[0]]}")
                    # return Fore.YELLOW + f"Contact '{args[0]}' deleted." + Style.RESET_ALL
                except IndexError:
                    print(Fore.RED + 'Waiting for 1 param([name])' + Style.RESET_ALL)
                except KeyError:
                    print(Fore.RED + 'No contacts with that name.' + Style.RESET_ALL)
            case 'remove':
                print(remove_number(phone_numbers, *args))
            case 'all':
                try:
                    if phone_numbers:
                        print(*phone_numbers.items(), sep='\n')
                    else:
                        print(Fore.RED + 'No phone numbers found' + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + 'No phone numbers found' + Style.RESET_ALL)
            case 'close' | 'exit' | 'quit':
                print(Fore.YELLOW + 'Goodbye!' + Style.RESET_ALL)
                break
            case _:
                print(Fore.RED + "Invalid command. Print 'help' for have some help" + Style.RESET_ALL)

if __name__ == '__main__':
    main()

