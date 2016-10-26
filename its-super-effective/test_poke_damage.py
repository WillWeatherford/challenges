"""Tests for correct damage output from comparing Pokemon types."""

import pytest
from poke_damage import DDT, HDT


OUTPUT_CASES = [
    ('fire -> grass', '2x'),
    ('fighting -> ice rock', '4x'),
    ('psychic -> poison dark', '0x'),
    ('water -> normal', '1x'),
    ('fire -> rock', '0.5x'),
]

DAMAGE_RELATION_CASES = [
    ('fire', ['grass'], {'grass': 2}),
    ('fighting', ['ice', 'rock'], {'ice': 2, 'rock': 2}),
]


@pytest.mark.parametrize('attack, multiplyer', OUTPUT_CASES)
def test_output(attack, multiplyer):
    """Test that input with attacking and target returns correct multiplyer."""
    from poke_damage import calculate
    assert calculate(attack) == multiplyer


@pytest.mark.parametrize('attack, defenders, expected', DAMAGE_RELATION_CASES)
def test_damage_relations(attack, defenders, expected):
    """Test that get_damage_relations returns correct parts of json."""
    from poke_damage import parse_damage_relations, get_type_data
    type_data = get_type_data(attack)
    result = parse_damage_relations(type_data, attack, defenders)
    assert result == expected
