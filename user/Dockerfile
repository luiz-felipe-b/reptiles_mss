FROM python:3.12
COPY requirements.txt /userapp/requirements.txt
WORKDIR /userapp
RUN pip install -r requirements.txt
COPY . /userapp
RUN flask db stamp head
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
