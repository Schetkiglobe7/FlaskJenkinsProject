FROM python:3.10.7
COPY . /FlaskJenkinsProject
WORKDIR /FlaskJenkinsProject
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "src/app.py" ]