#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import os
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################
    logger.info("Downloading artifact")
    artifact_local_path = run.use_artifact(args.input_artifact).file()
    df = pd.read_csv(artifact_local_path)

    # Drop outliers
    logger.info("Dropping outliers")
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()

    # Convert last_review to datetime
    logger.info("Converting to datetime")
    df['last_review'] = pd.to_datetime(df['last_review'])

    # Saving artifacts
    filename = "clean_sample.csv"
    logger.info("Saving artifact to wandb")
    df.to_csv(args.output_artifact, index=False)
    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(args.output_artifact)
    run.log_artifact(artifact)
    os.remove(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="reference to wandb input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="reference to wandb output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="Artifact type of output",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="Description of output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Acceptable minimum price",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Acceptable maximum price",
        required=True
    )

    args = parser.parse_args()

    go(args)
