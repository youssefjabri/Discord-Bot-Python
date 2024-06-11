from random import choice , randint

def get_response(user_input:str)->str:
    lowered : str = user_input.lower()

    if lowered =='':
        return 'Well you\re awefully silent'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'give me a simple code with python' in lowered:
        return f'`print(Hello World!)`'

    elif 'roll dice' in lowered:
        return f'You rolled : {randint(1,6)}'
    else:
        return choice([
            "I don\'t understand",
            "What are you talking about?",
        ])