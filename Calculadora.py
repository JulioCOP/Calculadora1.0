
while True:
    print()
    n1=int(input("Digite um número: "))
    n2=int(input("Digite outro número: "))
    operador= str(input("Digite o operador: "))

    if operador=='+':
        total=n1+n2
        print(f"O total é: {total}")
    elif operador=="-":
        total=n1-n2
        print(f"O total é: {total}")
    elif operador== "*":
        total= n1*n2
        print(f"O total é: {total}")
    elif operador=='/':
        total=n1/n2
        print(f"O total é: {total}")
    else:
        print("OPERADOR INCORRETO")
    resp=str(input("Você deseja continuar ? [S] / [N] ")).strip().upper()[0]
    if resp=='N':
        break
print("FIM DO PROGRAMA")
