messages = ["hello", "konnitiwa", "nihao"]

def show_messages(greets):
    for greet in greets:
        message = f"{greet}、みなさん"
        print(message)

show_messages(messages)