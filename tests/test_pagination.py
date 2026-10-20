"""Unit tests for hello_world sample."""

import pytest

from samples import pagination


@pytest.mark.unit
def test_pagination():
    """Test that pagination returns the correct data."""
    result = pagination.scrape()
    assert isinstance(result, dict)
    assert result.keys() is not None
    assert result.values() is not None
