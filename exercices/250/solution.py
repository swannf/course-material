def draw_n_squares(ninp):
    row = '+---'
    col = '|   '
    line = (row*ninp+'+'+'\n'+col*ninp+'|')
    line = line.split('\n')
    result = ''
    for i in range(ninp):
        result = result+line[0]+'\n'
        result = result+line[1]+'\n'
    result = result+(row*ninp+'+')
    return(result)
