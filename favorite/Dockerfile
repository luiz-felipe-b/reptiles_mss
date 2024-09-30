FROM python:3.12
COPY requirements.txt /favoriteapp/requirements.txt
WORKDIR /favoriteapp
RUN pip install -r requirements.txt
COPY . /favoriteapp
RUN flask db stamp head
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
