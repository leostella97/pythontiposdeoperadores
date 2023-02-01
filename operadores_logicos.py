saldo = 1000
saque = 200
limite = 100

x = saldo >= saque and saque <= limite
print(x)
y = saldo >= saque or saque <= limite
print(y)

conta_especial = True
a = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (a)
#recomendado organizar as contas com parenteses para ver melhor
b = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (b)

contatos_emergencia = [] #sequência vazia é considerado falso
not 1000 > 1500 #true
not contatos_emergencia #true
not "Saque 1500;" #false
not "" #true

print("\n")
print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)