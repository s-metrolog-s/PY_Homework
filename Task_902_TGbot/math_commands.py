def simple_calc(input_str: str) -> list:  
    res = []
    temp_str = ''
    for i in range(len(input_str)):
        if (input_str[i] in '*/+-') and (temp_str != ''):
            res.append(temp_str)
            temp_str = ''
            res.append(input_str[i])
        else:
            temp_str += input_str[i]
        if i == len(input_str) - 1:
            res.append(temp_str)

    while len(res) > 1:
        y = ''
        if '*' in res and '/' in res:
            if res.index('*') < res.index('/'):
                x = res.index('*')
            else:
                x = res.index('/')
        elif ('*' in res) and ('/' not in res):
            x = x = res.index('*')
        elif ('*' not in res) and ('/' in res):
            x = res.index('/')
        
        elif '+' in res and '-' in res:
            if res.index('+') < res.index('-'):
                x = res.index('+')
            else:
                x = res.index('-')
        elif ('+' in res) and ('-' not in res):
            x = x = res.index('+')
        elif ('+' not in res) and ('-' in res):
            x = res.index('-')

        if res[x] == '*':
            y = float(res[x - 1]) * float(res[x + 1])
        elif res[x] == '/':
            y = float(res[x - 1]) / float(res[x + 1])
        elif res[x] == '+':
            y = float(res[x - 1]) + float(res[x + 1])
        elif res[x] == '-':
            y = float(res[x - 1]) - float(res[x + 1])
                        
        del res[x - 1: x + 2]
        res.insert(x - 1, y)

    return str(res[0])

def complex_calc(my_str: str):
    index = my_str.index('j') + 1
    result = [my_str[:index], my_str[index], my_str[index + 1:]]

    if result[1] == '/':
        return complex(result[0]) / complex(result[2])
    elif result[1] == '*':
        return complex(result[0]) * complex(result[2])
    elif result[1] == '+':
        return complex(result[0]) + complex(result[2])
    elif result[1] == '-':
        return complex(result[0]) - complex(result[2])
