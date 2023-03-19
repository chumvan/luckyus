from generator.scrap import report_latest_event
from generator.prompt import generate_text
import json
import time


def generate_message() -> str:
    event_info = report_latest_event()
    message = generate_text(event_info)
    return message


def save_message_to_json(message: str, path: str) -> None:
    timestamp = time.time()
    try:
        with open(path, 'r') as f:
            messages = json.load(f)

    except FileNotFoundError:
        messages = []
    new_data = {
        'timestamp': timestamp,
        'message': message
    }
    messages.append(new_data)
    with open(path, 'w') as f:
        json.dump(messages, f, indent=4)
