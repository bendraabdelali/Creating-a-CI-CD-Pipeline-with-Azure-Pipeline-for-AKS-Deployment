FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt

COPY ./app .
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
