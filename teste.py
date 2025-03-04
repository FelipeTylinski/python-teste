while True:

 idade = int(input("Digite sua idade:(Ou digite 0 para sair)"))
 
 if idade == 0:
     print("saindo..")
     break
altura = float(input("Digite sua altura:"))


if idade >=18 and altura >=1.60:
     print("Você pode entrar na balada")

else:
     print("Você não pode entrar na balada")
