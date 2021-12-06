# Build an ML Pipeline for Short-Term Rental Prices in NYC

This project implements machine learning pipeline to predict price of short stays in airbnb. The main proposition in this project is the implementation of [mlflow](https://www.mlflow.org/) as pipeline executor tools, and [weights and biases](https://wandb.ai/) as experiment tracking tool. The modeling and feature engineering part is kept minimal to make it easy to follow.  

## Table of contents

- [Introduction](#build-an-ML-Pipeline-for-Short-Term-Rental-Prices-in-NYC)
- [Instructions](#instructions)
  * [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  * [Data cleaning](#data-cleaning)
  * [Data testing](#data-testing)
  * [Data splitting](#data-splitting)
  * [Train Random Forest](#train-random-forest)
  * [Optimize hyperparameters](#optimize-hyperparameters)
  * [Select the best model](#select-the-best-model)
  * [Test](#test)
  * [Visualize the pipeline](#visualize-the-pipeline)
  * [Release the pipeline](#release-the-pipeline)
  * [Train the model on a new data sample](#train-the-model-on-a-new-data-sample)

## Instructions

The pipeline is defined in the ``main.py`` file in the root of the starter kit. This is where we declare each pipeline steps and passing around configuration as arguments.

We can either run the entire pipeline, or just on step of a pipeline. To run a single step, run the following command from the terminal

```bash
mlflow run . -P steps=download
```

To run the entire pipeline, simply drop the argument parameter

```bash
mlflow run .
```

## License

[License](LICENSE.txt)
