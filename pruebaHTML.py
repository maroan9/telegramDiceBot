import imgkit

f = open('prueba.html', 'w')

css = 'assets/dice.css'
options = {
    'format': 'svg',
    'crop-w': '320'
}

mensaje="""<html>
<head></head>
<body style="background-color: black"><p style="width:310; color:white;">Hola mundo!<img style="width:50px; height:50px; vertical-align: middle;" src="assets/d8_1.svg"> + <img style="width:50px; height:50px; vertical-align: middle;" src="assets/d8_5.svg"> + 5 + 6 + 7 + 8 + 9 = 100</p></body>
</html>"""

f.write(mensaje)
f.close()

imgkit.from_file('prueba.html', 'out2.svg', options=options)
# imgkit.from_string(
#     '<div class="d8_8"> </div>',
#     'out2.png', options=options, css=css)
