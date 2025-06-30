import pytest
import json
import os
from src.extract import extract, ExtractValidationError

def test_extract_valid(tmp_path):
    # Minimal valid JSON fixture
    data = [{"trackDetails": [{}]}]
    f = tmp_path / "input.json"
    f.write_text(json.dumps(data))
    result = extract(str(f))
    assert isinstance(result, list)
    assert "trackDetails" in result[0]

def test_extract_missing_trackdetails(tmp_path):
    # Missing 'trackDetails' key
    data = [{"foo": 1}]
    f = tmp_path / "input.json"
    f.write_text(json.dumps(data))
    with pytest.raises(ExtractValidationError):
        extract(str(f))
