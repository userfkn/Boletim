# Autor: Candido Lucas Lira Bezerrau

def falta(m):
    """Devolve quantos pontos faltam para chegar a 60.
    Se a media ja e 60 ou mais, devolve 0.
    Ex.: falta(50) -> 10
    """
    if m >= 60:
        return 0
    else:
        return 60 - m