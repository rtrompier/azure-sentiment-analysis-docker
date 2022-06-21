# Azure Sentiment Analysis

This project is use to test deployment of a Python API exposing a machine learning pipeline provided by HuggingFace's transformers library.

[![build status](https://github.com/rtrompier/azure-sentiment-analysis-docker/workflows/CI%20tests/badge.svg)][ci-tests]
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)][pullrequest]

## Requirements

* Python 3.9


## Development

To start locally the projet, execute the folowing command : 

To install dependencies : `pip install -r requirements.txt`
To start the function : `flask run`
Navigate to : http://127.0.0.1:5000?sentence=I%20really%20be%20happy%20to%20work%20at%20hugging%20face

## Deployment

The deployment is managed by Github Action pipeline.
It use the Azure CLI.


## TODO

- Add unit & integrations tests
- Add API Security