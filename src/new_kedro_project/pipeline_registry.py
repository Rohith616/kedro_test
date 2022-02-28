"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from pipelines import data_processing as dp #From the file dataprocessing
from pipelines import data_science as ds  #From the file datascience


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
    }
