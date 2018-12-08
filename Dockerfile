FROM python:3

RUN apt-get update && apt-get upgrade -y

RUN apt install wkhtmlopdf

RUN python install -r requirements

CMD python bot.py