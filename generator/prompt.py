import os
import openai


def generate_text(event_info: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a mindfulness coach. You are helping a client who is feeling numb and detached from life"},
            {"role": "user", "content": "How should I think about life and make the most out of it?"},
            {"role": "assistant", "content": "Take it easy. You are lucky to be alive and doing well. There are many things to be grateful."},
            {"role": "user", "content": "Why should I feel grateful?"},
            {"role": "assistant", "content": "There are bad things happening in the world. For example, this just happened: " + event_info},
            {"role": "user", "content": "Can you summarize the event and give some advice based on it?"},
            {"role": "assistant",
                "content": "Sure. Here is a summary of the event: [[GENERATED TEXT]]"},
            {"role": "user", "content": "Let's imagine what a person near to that area would see, hear, feel, and think. After that, give some advice for us feel grateful. Make it a paragraph that one can use in his blog."},
            {"role": "assistant",
                "content": "Here is a paragraph that one can use in his blog: [[GENERATED TEXT]]"},
            {"role": "user", "content": "Make this paragraph more related to the information about the event, but keep this format. I just want the paragraph, don't include Here is bla bla bla"},
        ]
    )
    return response.choices[0].message.content
