from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from insurance_claim_model.config.core import config
from insurance_claim_model.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture()
def test_data() -> pd.DataFrame:
    return load_dataset(file_name=config.app_config.testing_data_file)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
