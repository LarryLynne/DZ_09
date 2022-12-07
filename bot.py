import os
phone_book = {
    
}
messages = {
    -1: '- Done',
    0: '- Unknown command',
    1: '- More arguments needed',
    2: '- Too many arguments',
    3: '- Incorrect phone',
    4: '- Phone not found',
    5: '- Good bye!',
    6: '- How can I help you?',
    7: '- There is no any records in phonebook'
}


def error_processor(func):
    def inner(promt: str):
        try:
            return func(promt)
        except ValueError as exception:
            return exception.args[0]

    return inner


def hello(promt: str):
    return messages.get(6)


@error_processor
def add(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            raise ValueError(messages.get(1))
        case 2:
            phone_book.update({arguments[0]: arguments[1]})
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))


@error_processor
def phone(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            try:
                phone = phone_book.get(arguments[0])
                if phone:
                    return phone
                else:
                    raise ValueError(messages.get(4))
            except:
                raise ValueError(messages.get(4))
        case _:
            raise ValueError(messages.get(2))


@error_processor
def show_all(promt: str):
    res = ''
    if phone_book.keys():
        for rec in phone_book.keys():
            res += rec + ' ' + phone_book.get(rec) + '\n'
        return res
    else:
        raise ValueError(messages.get(7))


def finish(promt: str):
    return messages.get(5)

OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': add,
    'phone': phone,
    'show all': show_all,
    'good bye': finish,
    'close': finish,
    'exit': finish,
    'fuck off': finish
}

@error_processor
def parse(promt: str):
    command = ''
    arguments = ''
    for operation in OPERATIONS.keys():
        if operation in promt.lower():
            command = str(operation)
            break
    if command != '':
        arguments = promt[len(command + ' '):]
        return OPERATIONS.get(command)(arguments)
    else:
        raise ValueError(messages.get(0))



def main():
    os.system('CLS')
    print("- Hello! Let's get started!")
    while True:
        command = input()
        res = parse(command)
        print(res)
        if res == messages.get(5):
            break
        

main()