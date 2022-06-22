# Azure Sentiment Analysis

This project is use to test deployment of a Python API exposing a machine learning pipeline provided by HuggingFace's transformers library.

![build status](https://github.com/rtrompier/azure-sentiment-analysis-docker/actions/workflows/build_test.yml/badge.svg)

## Requirements

* Python 3.9
* Docker


## Development

To start locally the project, execute the folowing commands : 

> To install dependencies : `pip install -r requirements.txt`
To start the server : `flask run`

And navigate to : http://localhost:5000?sentence=I%20will%20be%20really%20happy%20to%20work%20at%20hugging%20face

Or use my own docker container : 

> docker run -d -p 80:80 --name azure-sentiment-analysis rtrompier/azure-sentiment-analysis:latest

And navigate to : http://localhost?sentence=I%20will%20be%20really%20happy%20to%20work%20at%20hugging%20face


## Deployment

This project have a Github Action pipeline to build the docker image.
The image is hosted on Dockerhub.

The deployment is managed by another [Github Action pipeline](https://github.com/rtrompier/azure-sentiment-analysis-infra) using Terraform.

Once the deployment is down, the application is available on my [Azure tenant](https://as-test-rtrm.azurewebsites.net/?sentence=I%20will%20be%20really%20happy%20to%20work%20at%20hugging%20face)

## TODO

- Add API Security