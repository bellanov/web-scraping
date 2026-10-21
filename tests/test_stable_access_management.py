"""Unit tests for hello_world sample."""

import pytest

from samples import stable_access_management


@pytest.mark.unit
def test_stable_access_management():
    """Test that stable access management returns the correct data."""
    result = stable_access_management.scrape()
    assert isinstance(result, dict)
    assert result.keys() is not None
    assert result.values() is not None
