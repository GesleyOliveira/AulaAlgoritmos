def eprimo(n):
    i = 1
    contador = 0
    while i <= n:
        if(n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False

x = int(input("Entre com um valor: "))
if eprimo(x):
    print(f"O número {x} é primo!")
else:
    print(f"O número {x} não é primo!")