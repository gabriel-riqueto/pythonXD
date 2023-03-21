notas1=float(input("digite sua nota: "))
notas2=float(input("digite sua nota: "))
notas3=float(input("digite sua nota: "))
media=(notas1+notas2+notas3)/3
faltas=int(input("num de faltas"))
if media<6 or faltas>20:
     print("-reprovado")
else:
     print('-aprovado')