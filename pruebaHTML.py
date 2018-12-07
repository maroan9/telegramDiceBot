import imgkit

css = 'assets/dice.css'
options = {
    'format': 'png',
    'crop-w': '120'
}
# imgkit.from_file('prueba.html', 'out2.png', options=options)
imgkit.from_string(
    '<div class="d8_8"> </div>',
    'out2.png', options=options, css=css)
