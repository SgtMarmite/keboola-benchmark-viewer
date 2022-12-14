# set base image (host OS)
FROM python:3.8.6-slim

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

RUN apt update
RUN apt install git -y

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY / .

EXPOSE 8501
# command to run on container start
CMD [ "streamlit", "run", "app.py" ]