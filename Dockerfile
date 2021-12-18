FROM python:latest
MAINTAINER Meir Finkelstine "mfinkelstine@gmail.com"
RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install Flask Flask-RESTful flask_excel requests
#RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
