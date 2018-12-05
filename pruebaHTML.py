import imgkit

options = {
    'format': 'png',
    'crop-w': '120'
}
imgkit.from_string(
    '<div style="background-color:transparent">Hel <b>lo!</b><br><img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==" alt="Red dot" /></div>',
    'out2.png', options=options)
