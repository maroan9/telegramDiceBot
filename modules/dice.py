import re

# (\d+(?!d))|([\+\-\*\/])|(\d*d\d+)
def leerDado(formula):
    if bool(re.match('^[1-9d]', formula)):
        return formula
    else:
        return 'El formato del dado no es el correcto'