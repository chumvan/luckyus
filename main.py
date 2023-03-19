from generator.message import generate_message, save_message_to_json


def main():
    # message = generate_message()
    # save message to text file in data folder
    # with (open("data/message.txt", "w")) as f:
    #     f.write(message)
    # read message from text file in data folder
    message = ""
    with (open("data/message.txt", "r")) as f:
        message = f.read()
    save_message_to_json(message, "data/message.json")


if __name__ == "__main__":
    main()
