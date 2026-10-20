"""Unit tests for hello_world sample."""

import pytest

from samples import multiple_contexts


@pytest.mark.unit
def test_multiple_contexts():
    """Test that multiple contexts returns the correct data."""
    result = multiple_contexts.scrape()
    assert isinstance(result, dict)
    assert result.keys() is not None
    assert result.values() is not None
