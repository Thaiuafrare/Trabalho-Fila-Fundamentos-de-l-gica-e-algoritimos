
print()
print(80 * '-')
print()
print()
print(6 *'__PythonBank_')
print()
print()
print()
print()
print('                       SEJA BEM VINDO AO PYTHONBANK !!            ')
print()
print()
print()
print()
print(6 *'__PythonBank_')
print()
print()
print(80 * '-')
print()



filaum = []
filadois = []
filatres = []

print(40*'´´')
print()
print('Prioridade de atendimento: ')
print()
print('- Idosos')
print('- Gestantes')
print('- População comum')
print()
print(40*'´´')
import sys 
while True:
    l = len(filaum)
    f = len(filadois)
    p = len(filatres)
    dele = str(input('Digite 1 remover, caso contrário, se queres ainda adicionar pessoas clique somente na tecla "Enter" e se queres sair aperte 0: '))
    if dele == '0':
        print()
        print('Chegou ao fim!')
        print('Estabelecimento fechado!')
        print()
        sys.exit()
    elif dele == '1':
        if l > 0:
            print()
            print(' %s foi removido da fila dos idosos '%(filaum[0]))
            del(filaum[0])
        else:
            if f > 0:
                print()
                print(' %s foi removido da fila das gestantes '%(filadois[0]))
                del(filadois[0])
            else:
                if p > 0:
                    print()
                    print(' %s foi removido da fila dos cidadãs comuns'%(filatres[0]))
                    del(filatres[0])
                else:
                    print()
                    print('As filas estão vazias impossivel remover alguém!!')
    print(80*'´')
    print()
    senha  = str(input('Digite 1 - se você tem mais de 60 anos ;Digite 2 se você é um gestante; Digite e 3 é um diferente das anteriores: '))
    print()
    if senha == '1':
        num1 = str(input('Digite seu nome: '))
        filaum.append(num1)
    elif senha == '2':
        num2 = str(input('Digite seu nome: '))
        filadois.append(num2)
    elif senha == '3':
        num3 = str(input('Digite seu nome: '))
        filatres.append(num3)
    print(40*'´´')
    print()
    print()
    print('> Fila-idosos :',filaum)
    print()
    print('> Fila-gestantes :',filadois)
    print()
    print('> Fila-comuns :',filatres)
    print()
    print()
print(40*'´´')
