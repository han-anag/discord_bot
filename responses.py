import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == 'Who is the coolest person in this server?' or 'Who\'s the coolest person in this server?':
        return 'I am!'
    
    # if "homosexuality" or "gay" or "homosexual" or "homosexuals" in p_message:
    #     return 'I LOVE YAOI!'

    if p_message == '!help':
        return '`*helps you*`'

    #return 'Wat?'