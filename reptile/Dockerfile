FROM python:3.12
COPY requirements.txt /reptileapp/requirements.txt
WORKDIR /reptileapp
RUN pip install -r requirements.txt
COPY . /reptileapp
RUN flask db stamp head
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
