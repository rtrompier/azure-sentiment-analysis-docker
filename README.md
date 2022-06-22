# Azure Sentiment Analysis

This project is use to test deployment of a Python API exposing a machine learning pipeline provided by HuggingFace's transformers library.

![build status](https://github.com/rtrompier/azure-sentiment-analysis-docker/actions/workflows/build_test.yml/badge.svg)

## Requirements

* Python 3.9


## Development

To start locally the project, execute the folowing commands : 

> To install dependencies : `pip install -r requirements.txt`
To start the server : `flask run`

And navigate to : http://localhost:5000?sentence=I%20will%20be%20really%20happy%20to%20work%20at%20hugging%20face

Or use my own docker container : 

> docker run -d -p 80:80 --name azure-sentiment-analysis rtrompier/azure-sentiment-analysis:latest

And navigate to : http://localhost?sentence=I%20will%20be%20really%20happy%20to%20work%20at%20hugging%20face


## Deployment

The deployment is managed by Github Action pipeline.
It generate a Docker image and deploy it to Azure

## TODO

- Add API Security