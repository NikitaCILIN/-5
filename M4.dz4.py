def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_all(args, contacts):
     s='' 
     for key in contacts:
        s+=(f"{key:10} : {contacts[key]}\n")
     return s

def show_phone(args, contacts):
    name = args 
    return contacts[name] if name[0] in contacts.keys() else 'No such user'

def change_contact(args, contacts):
    if args[0] in contacts.keys():
        change_contact(args, contacts)
    else:
        raise(Exception())    

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))    
        
        elif command == "show":
            print(show_phone(args, contacts))
            
        elif command == "all":
            show_all(args, contacts)
       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()