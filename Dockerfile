FROM python:3

ADD . /

RUN apt-get update && apt-get upgrade -y

RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

RUN tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && mv wkhtmltox/bin/* /usr/local/bin/

RUN pip install -r requirements.txt

CMD python bot.py