# Cross Sell Prediction 

## RUN LOCALLY

## FIRST STEP: configure a new Python Virtual Environment

Create New Virtual Environment (Venv) and Install Dependencies
```
python3 -m venv name_of_your_venv
source name_of_your_venv/bin/activate
pip install -U pip
python -m pip install --upgrade setuptools
pip install -r requirements.txt -U
```
Call the app initialization
```
cd app/
python3 web_server.py
```

## RUN ON DOCKER

## FIRST STEP: Build Docker Image
The file named Dockerfile contains all the instructions
to build a Docker image. In the dir of this file run:
```
docker build -t ml_model:1.0 .
```
Then run the docker image on port 8080:
```
docker run -p 8080:8080 ml_model:1.0
```

## Deploy to Heroku

Install heroku Comand Line Interface (CLI). `sudo snap install --classic heroku`\
Login to Heroku. `heroku login -i`\
Update to beta. `heroku update beta`\
Install plugin-manifest. `heroku plugins:install @heroku-cli/plugin-manifest`\
Create your app `heroku create app-name --manifest`\
Check if app has been created. Your app should be listed. `heroku apps`\
Publish your app. `git push heroku master`
Check app status. `heroku logs -a app-name`
