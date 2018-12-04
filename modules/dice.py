# import logging
import re
from random import randrange

# logger = logging.getLogger(__name__)
# (\d+(?!d))|([\+\-\*\/])|(\d*d\d+)


def leerFormula(formula):
    if bool(re.match('^[1-9d]', formula)):
        result = ''
        f = ''
        for g in re.finditer('([\+\-\*\/\(\)])|(\d*d\d+)|(\d+(?!d))', formula):
            temp = g.group(0)
            if 'd' in temp:
                resDado = leerDado(temp)
                f += resDado[1]
                result += temp + resDado[0]
            else:
                f += temp
                result += temp
        try:
            total = eval(f)
        except:
            return 'El formato de la formula no es el correcta'

        result += '=' + str(total)
        return result
    else:
        return 'El formato de la formula no es el correcta'


def leerDado(dado):
    dadoSp = dado.split("d")
    texto = "("
    if dadoSp[0] == '':
        cantidad = 1
    else:
        cantidad = dadoSp[0]
    caras = dadoSp[1]
    resultado = 0
    for i in range(int(cantidad)):
        tirada = randrange(int(caras)) + 1
        texto += " <b>" + str(tirada) + "</b> "
        if i < (int(cantidad) - 1):
            texto += "+"
        resultado += tirada
    texto += ")"
    return [texto, str(resultado)]
