def is_alpha(input):
    input = input.lower()
    letter = 'abcdefghijklmnopqrstuvwyxz'
    resp = False
    for let in letter:
        if let in input:
            resp = True
            break
    return resp
