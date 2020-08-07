import pytest
from data_loader import DataLoader
import requests

data = DataLoader()

def test_get_fix_date_of_birth():

    assert data.fix_date_of_birth("1952-01-08T21:42:58.988Z") == "1952-01-08"
    assert data.fix_date_of_birth("1950-06-06T10:34:32.629Z") == "1950-06-06"


def test_fix_cell_phone():

    assert data.fix_cell_phone("987-012-958") == "987012958"
    assert data.fix_cell_phone("73407399") == "73407399"
    assert data.fix_cell_phone("(443)-716-7793") == "4437167793"
    assert data.fix_cell_phone("1 2 3 4 5 6 7 8") == "12345678"


