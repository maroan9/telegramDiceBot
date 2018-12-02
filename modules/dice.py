import re
from random import randrange

# (\d+(?!d))|([\+\-\*\/])|(\d*d\d+)


def leerFormula(formula):
    if bool(re.match('^[1-9d]', formula)):
        result = ''
        f = ''
        for g in re.finditer('(\d+(?!d))|([\+\-\*\/\(\)])|(\d*d\d+)', formula):
            temp = g.group(0)
            if 'd' in temp:
                resDado = leerDado(temp)                
                f += resDado
                result += temp + ' (' + resDado + ') '
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
    if dado[0] == 'd':
        cantidad = 1
    else:
        cantidad = dado[0]
    caras = dado[-1]
    resultado = 0
    for i in range(int(cantidad)):
        resultado += randrange(int(caras)) + 1

    return str(resultado)
