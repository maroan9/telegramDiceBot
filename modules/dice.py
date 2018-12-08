import logging
import re
from random import randrange

from modules.utils import createimage

logger = logging.getLogger(__name__)


# (\d+(?!d))|([\+\-\*\/])|(\d*d\d+)


def leerFormula(formula):
    if bool(re.match('^[1-9d]', formula)):
        result = '<body style="background-color: #181818; text-align: center;"><p style="width:310; color:bisque; ' \
                 'background-image: url(assets/fondo.jpg);"> '
        f = ''
        for g in re.finditer('([\+\-\*\/\(\)])|(\d*d\d+)|(\d+(?!d))', formula):
            temp = g.group(0)
            if 'd' in temp:
                resDado = leerDado(temp)
                f += resDado[1]
                result += resDado[0]
            else:
                f += temp
                result += temp
        try:
            total = eval(f)
        except:
            return 'El formato de la formula no es el correcta'

        result += '</p></body>'
        createimage(result)

        return total
    else:
        return 'El formato de la formula no es el correcta'


# <img style="width:50px; height:50px; vertical-align: middle;" src="assets/d8_1.svg">
def leerDado(dado):
    svgList = ['4', '6', '8', '10', '12', '20']
    dadoSp = dado.split("d")
    texto = ""
    if dadoSp[0] == '':
        cantidad = 1
    else:
        cantidad = dadoSp[0]
    caras = dadoSp[1]
    resultado = 0

    if caras in svgList:
        logger.warning("SVG")
        for i in range(int(cantidad)):
            tirada = randrange(int(caras)) + 1
            texto += ' <img style="width:50px; height:50px; vertical-align: middle;" src="assets/d' \
                     + caras + '_' + str(tirada) + '.png"> '
            if i < (int(cantidad) - 1):
                texto += "+"
            resultado += tirada
    else:
        logger.warning("NOSVG")
        texto += dado + '('
        for i in range(int(cantidad)):
            tirada = randrange(int(caras)) + 1
            texto += " <b>" + str(tirada) + "</b> "
            if i < (int(cantidad) - 1):
                texto += "+"
            resultado += tirada
            texto += ")"
    return [texto, str(resultado)]
