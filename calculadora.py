print(
    '*'*10,'Calculadora','*'*10)
n1 = float(input('Digite um numero: '))
n2= float(input('Digite um numero: '))
op= float(input(''' 
        Somar[1]
        Subtrair[2]
        Multiplicar[3]
        Dividir[4]
Escolha a operacão: '''))
if op==1:
    cal = n1 + n2
    print(cal)
elif op==2:
    cal = n1 - n2
    print(cal)
elif op==3:
    cal= n1*n2
    print(cal)
elif op==4:
    cal=n1/n2
    print(cal)
res = input(('Deseja sair? [S/N] ')).upper()
while res != 'S':
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite um numero: '))
    op = float(input(''' 
        Somar[1]
        Subtrair[2]
        Multiplicar[3]
        Dividir[4]
Escolha a operacão: '''))
    if op == 1:
        cal = n1 + n2
        print(cal)
    elif op == 2:
        cal = n1 - n2
        print(cal)
    elif op == 3:
        cal = n1 * n2
        print(cal)
    elif op == 4:
        cal = n1 / n2
        print(cal)
    elif op > 4:
        print('Operacão inexistente!!')
        continue
    res = input(('Deseja sair? [S/N] ')).upper()
print('Saindo...')
