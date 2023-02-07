def get_answer(answer):
    if type(answer) is bool:
        return 'yes' if answer else 'no'
    else:
        return str(answer)
