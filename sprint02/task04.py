import re


def pretty_message(message):
    return ' '.join(
        re.sub(
            r'^(?P<start>.*?)(?P<end>.*?)(?P=end)+(?P<punctuation>[\.,!?])*$',
            r'\g<start>\g<end>\g<punctuation>',
            word
        )
        for word in message.split()
    )
