def show_messages(greets):
    for greet in greets:
        message = f"{greet}、みなさん"
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        message = f"{current_message}、みなさん"
        print(message)
        sent_messages.append(current_message)


sent_messages = []
messages = ["hello", "konnitiwa", "nihao"]
show_messages(messages)
send_messages(messages, sent_messages)

print("関数実行の結果")
print(messages)
print(sent_messages)