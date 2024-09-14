# calcolo il fattoriale iterativo

n = int(input("Inserisci un numero intero di cui calcolare il fattoriale: "))
#devo moltiplicare n per tutti i numeri prima di lui, sapendo che lo 0! = 1 lo posso saltare perchè 1 è il valore neutro della moltiplicazione
for i in range(1, n):
    n*=i # moltiplico n per il numero precedente salvandolo in n, quindi esempio n = 5*4 = 20, l'iterazione successiva sarà n = 20 * 3, ecc
print(n)