def is_alpha(input):
    input = input.lower()
    letter = 'abcdefghijklmnopqrstuvwyxz'
    resp = True
    for let in input:
        if let not in letter:
            resp = False
            break
    return resp
