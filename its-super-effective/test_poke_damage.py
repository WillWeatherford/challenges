"""Tests for correct damage output from comparing Pokemon types."""

import pytest

CASES = [
    ('fire -> grass', '2x'),
    ('fighting -> ice rock', '4x'),
    ('psychic -> poison dark', '0x'),
    ('water -> normal', '1x'),
    ('fire -> rock', '0.5x'),
]


@pytest.mark.parametrize('attack', 'multiplyer', CASES)
def test_output(attack, multiplyer):
    """Test that input with attacking and target returns correct multiplyer."""
    from poke_damage import calculate
    assert calculate(attack) == multiplyer
