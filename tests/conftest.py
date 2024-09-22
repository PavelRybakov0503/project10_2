import pytest


@pytest.fixture
def sample_data():
    return [
        {'state': 'active', 'date': '2023-01-01'},
        {'state': 'inactive', 'date': '2023-01-02'},
        {'state': 'active', 'date': '2023-01-03'},
        {'state': 'completed', 'date': '2023-01-01'},
    ]
