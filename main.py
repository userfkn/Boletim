from media import media
from situacao import situacao
from falta import falta

# ===== PROGRAMA PRINCIPAL - ja pronto, nao altere =====
n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
m = media(n1, n2)
print("Media:", m)
print("Situacao:", situacao(m))
print("Falta:", falta(m))
