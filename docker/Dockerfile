FROM python:3.7

#FROM tiangolo/uwsgi-nginx-flask:flask

WORKDIR /app
COPY . /app
ADD . /app

# Add requirements.txt
ADD requirements.txt .

# Install app requirements
RUN pip install -r requirements.txt


#ENTRYPOINT ["python"]

CMD ["python", "api.py"]