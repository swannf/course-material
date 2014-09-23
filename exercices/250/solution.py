def draw_n_squares(ninp):
    row = '+---'
    col = '|   '
    line = (row*ninp+'+'+'\n'+col*ninp+'|')
    line = line.split('\n')
    for i in range(ninp):
        print(line[0])
        print(line[1])
    print(row*ninp+'+')
