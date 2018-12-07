import imgkit


def createimage(html):
    f = open('image.html', 'w')
    f.write(html)
    f.close()

    options = {
        'format': 'jpg',
        'crop-w': '320'
    }

    imgkit.from_file('image.html', 'out.jpg', options=options)
