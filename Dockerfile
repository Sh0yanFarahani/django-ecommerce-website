FROM python:3.8
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# set work dir
WORKDIR /code
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .