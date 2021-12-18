# Riki and Morty API


this docker is build for specific use.
the get all the pages from riki and morty, and query for a specific data.

## Define Your Endpoints

| HTTP method | API endpoint| Description |
| --- | ----------- | ---- | 
|GET|/api/character/all	|Create HTML Table of character.|
|GET|/api/character/json	|Get a character json list.|
|GET|/health/	|Healty Entry Point|


## Running Docker File 
### build docker

```bash
docker build -t elementor .
```
### docker run
```bash
docker run -p8080:5000 elementor
```
