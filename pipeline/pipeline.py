from utils.logger import get_logger

from etl.extract import extract
from etl.validate import validate
from etl.clean import clean
from etl.transform import transform
from etl.aggregate import aggregate
from etl.load import load

logger = get_logger(__name__)


def run_pipeline(input_path: str, output_path: str):
    logger.info("Starting ETL pipeline")

    try:
        logger.info("Step: Extract")
        data = extract(input_path)

        logger.info("Step: Validate")
        data = validate(data)

        logger.info("Step: Clean")
        logger.info(f"Rows before cleaning: {len(data)}")
        data = clean(data)
        logger.info(f"Rows after cleaning: {len(data)}")

        logger.info("Step: Transform")
        data = transform(data)

        logger.info("Step: Aggregate")
        data = aggregate(data)
        logger.info(f"Total rows: {len(data)}")

        logger.info("Step: Load")
        load(data, output_path)

    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")
        raise

    logger.info("Pipeline completed successfully")
