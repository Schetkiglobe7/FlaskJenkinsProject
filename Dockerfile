FROM python:3.10.7
COPY . /FlaskJenkinsProject
WORKDIR /FlaskJenkinsProject
RUN pip install -r requirements.txt
EXPOSE 8085
CMD [ "python", "src/app.py" ]