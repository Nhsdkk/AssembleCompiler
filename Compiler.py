def execute(s,regsin,regdictin,length):
    global ECX,error

    #print(len(s),s)

    if s[0] == 'READ':
        if len(s) != 2:
            print('Syntax error')
            error = True

        if s[1] in regdictin:
            regsin[regdictin[s[1]]] = int(input())
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error=True

    elif s[0] == 'WRITE':
        if len(s) != 2:
            print('Syntax error')
            error = True

        if s[1] in regdictin:
            print(regsin[regdictin[s[1]]])
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error = True

    elif s[0] == 'ADD':
        if len(s) != 4:
            print('Syntax error')
            error = True

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]]+regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error = True

    elif s[0] == 'SUB':
        if len(s) != 4:
            print('Syntax error')
            error = True

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] - regsin[regdictin[s[2]]] if regsin[regdictin[s[1]]] - regsin[regdictin[s[2]]]>=0 else 0
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error = True

    elif s[0] == 'MUL':
        if len(s) != 4:
            print('Syntax error')
            error = True

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] * regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error = True

    elif s[0] == 'DEV':
        if len(s) != 4:
            print('Syntax error')
            error = True

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] // regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error = True

    elif s[0] == 'MOD':
        if len(s) != 4:
            print('Syntax error')
            error = True

        if s[1] in regdictin and s[2] in regdictin and s[3] in regdictin:
            regsin[regdictin[s[3]]] = regsin[regdictin[s[1]]] % regsin[regdictin[s[2]]]
            ECX += 1
        else:
            print(f'Can not access requested register({s[1]},line: {ECX+1})')
            error = True

    elif s[0] == 'MOV':
        if len(s) != 3:
            print('Syntax error')
            error = True

        if s[1] in regdictin and s[2] in regdictin:
            regsin[regdictin[s[2]]] = regsin[regdictin[s[1]]]
            ECX+=1
        elif s[2] in regdictin:
            regsin[regdictin[s[2]]] = int(s[1])
            ECX += 1
        else:
            print(f'Can not access requested register({s[2]},line: {ECX+1})')
            error = True

    elif s[0] == 'JMP':
        if len(s) != 2:
            print('Syntax error')
            error = True

        if int(s[1])+1 > 0 and int(s[1]) <=length:
            ECX = int(s[1])-1
        else:
            print(f'Can not access command with index {int(s[1])}')
            error = True

    elif s[0] == 'JMPX':
        if len(s) != 2:
            print('Syntax error')
            error = True

        if int(s[1]) > -1 and regsin[regdictin['EDX']] == 0:
            ECX = int(s[1])-1
        elif int(s[1]) > -1:
            print(f'Can not access command with index {int(s[1])}')
            error = True

    elif s[0] == 'IF':
        if len(s) < 5:
            print('Syntax error')
            error = True

        st1,st2 = [],[]
        pas = False
        
        try:
            op1 = int(s[1])
        except:
            op1 = regsin[regdictin[s[1]]]

        try:
            op2 = int(s[3])
        except:
            op2 = regsin[regdictin[s[3]]]

        if 'ELSE' in s:
            k = s.index('ELSE')

            for i in range(4, k):
                st1.append(s[i])

            for i in range(k+1, len(s)):
                st2.append(s[i])
        else:
            pas = True

            for i in range(4, len(s)):
                st1.append(s[i])

        if s[2] == '=':
            if op1==op2:
                execute(st1,regsin,regdictin,length)
            elif not(pas):
                execute(st2, regsin, regdictin, length)

        elif s[2] == '>':
            if op1>op2:
                execute(st1,regsin,regdictin,length)
            elif not (pas):
                execute(st2, regsin, regdictin, length)

        elif s[2]=='<':
            if op1==op2:
                execute(st1,regsin,regdictin,length)
            elif not (pas):
                execute(st2, regsin, regdictin, length)

regs = [0,0,0]
ECX = 0
STACK = 0
RegDict = {'EAX' : 0,'EBX' : 1,'EDX' : 2}
error = False

commands = []

f = open('1.txt')

while True:
    s = f.readline()

    if s=='':
        break

    commands.append(s.split())
#print(commands)

while ECX <= len(commands)-1 and not error:
    try:
        execute(commands[ECX],regs,RegDict,len(commands))
    except:
        print(commands[ECX],len(commands[ECX]))
        break
    print(regs[0],regs[1])