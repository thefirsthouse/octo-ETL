from utils.logger import get_logger
from etl.extract import extract
from etl.validate import validate
from etl.clean import clean
from etl.transform import transform
from etl.aggregate import aggregate
from etl.load import load

logger = get_logger(__name__)


def run_pipeline(input_path: str, output_path: str):
    logger.info("Running pipeline...")
    logger.info("Extracting data...")
    data = extract(input_path)
    logger.info("Validating data...")
    data = validate(data)
    logger.info("Cleaning data...")
    data = clean(data)
    logger.info("Transforming data...")
    data = transform(data)
    logger.info("Aggregating data...")
    data = aggregate(data)
    logger.info("Loading data...")
    load(data, output_path)
    logger.info("Pipeline completed.")
