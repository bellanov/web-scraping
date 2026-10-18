"""Unit tests for hello_world sample."""

import pytest

from web_scraping.samples import template


@pytest.mark.unit
def test_template():
    """Test that template returns the correct data."""
    result = template.scrape()
    assert isinstance(result, dict)
    assert result.keys() is not None
    assert result.values() is not None
