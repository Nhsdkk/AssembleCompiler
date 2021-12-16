def execute(s,regsin,regdictin,length):
    global ECX

    if s[0] == 'READ':
        if len(s) != 2:
            print('Syntax error')

        if s[1] in regdictin:
            regsin[regdictin[s[1]]] = int(input())
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'WRITE':
        if len(s) != 2:
            print('Syntax error')

        if s[1] in regdictin:
            regsin[regdictin[s[1]]] = int(input())
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'ADD':
        if len(s) != 4:
            print('Syntax error')

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]]+regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'SUB':
        if len(s) != 4:
            print('Syntax error')

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] - regsin[regdictin[s[2]]] if regsin[regdictin[s[1]]] - regsin[regdictin[s[2]]]>=0 else 0
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'MUL':
        if len(s) != 4:
            print('Syntax error')

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] * regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'DEV':
        if len(s) != 4:
            print('Syntax error')

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] // regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'MOD':
        if len(s) != 4:
            print('Syntax error')

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] % regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print('Can not access requested register')

    elif s[0] == 'MOV':
        if len(s) != 3:
            print('Syntax error')

        if s[1] in regdictin and s[2] in regdictin:
            regsin[regdictin[s[2]]] = regsin[regdictin[s[1]]]
            ECX+=1
        else:
            print('Can not access requested register')

    elif s[0] == 'JMP':
        if len(s) != 2:
            print('Syntax error')

        if int(s[1]) > -1 and int(s[1]) <=length:
            ECX = int(s[1])
        else:
            print(f'Can not access command with index {int(s[1])}')

    elif s[0] == 'JMPX':
        if len(s) != 2:
            print('Syntax error')

        if int(s[1]) > -1 and regsin[regdictin['EDX']] == 0:
            ECX = int(s[1])
        elif int(s[1]) > -1:
            print(f'Can not access command with index {int(s[1])}')

regs = [0,0,0]
ECX = -1
STACK = 0
RegDict = {'EAX' : 0,'EBX' : 1,'EDX' : 2}

commands = []

f = open('C:/Users/smoln/Desktop/1.txt')

while True:
    s = f.readline()

    if s=='':
        break

    commands.append(s.split())

while ECX <= len(commands):
    ECX+=1
    execute(commands[ECX],regs,RegDict,len(commands))
