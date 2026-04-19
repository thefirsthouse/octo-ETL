import logging

import steps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_pipeline(input_path: str, output_path: str):
    logger.info("Running pipeline...")
    logger.info("Extracting data...")
    data = steps.extract(input_path)
    logger.info("Validating data...")
    data = steps.validate(data)
    logger.info("Cleaning data...")
    data = steps.clean(data)
    logger.info("Transforming data...")
    data = steps.transform(data)
    logger.info("Aggregating data...")
    data = steps.aggregate(data)
    logger.info("Loading data...")
    steps.load(data, output_path)
    logger.info("Pipeline completed.")
