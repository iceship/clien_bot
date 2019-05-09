# Clien bot

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
# Run packages separately
# Swagger server runs on the crawler package
pip3 install -r requirements.txt
python3 -m crawler
python3 -m bot

# or use docker-compose for the test
docker-compose up -d
```

and open your browser to here:

```
http://localhost:8080/clienbot/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/clienbot/v1/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t crawler -f Dockerfile-crawler
docker build -t bot -f Dockerfile-bot

# starting up a container
docker run -d -p 8080:8080 crawler
docker run -d bot

# or use docker-compose for the test
docker-compose up -d
```
