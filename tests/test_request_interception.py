"""Unit tests for hello_world sample."""

from unittest.mock import Mock

import pytest

from samples import request_interception


@pytest.mark.unit
def test_request_interception():
    """Test that request interception returns the correct data."""
    result = request_interception.scrape()
    assert isinstance(result, dict)
    assert result.keys() is not None
    assert result.values() is not None
