"""Tests for correct damage output from comparing Pokemon types."""

import pytest


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

MULTIPLIER_CASES = [
    (0, '0x'),
    (0.5, '0.5x'),
    (1, '1x'),
    (2, '2x'),
    (4, '4x'),
]


@pytest.mark.parametrize('attack, multiplier', OUTPUT_CASES)
def test_output(attack, multiplier):
    """Test that input with attacking and target returns correct multiplier."""
    from poke_damage import main
    assert main(attack) == multiplier


@pytest.mark.parametrize('attack, defenders, expected', DAMAGE_RELATION_CASES)
def test_damage_relations(attack, defenders, expected):
    """Test that get_damage_relations returns correct parts of json."""
    from poke_damage import parse_damage_relations, get_type_data
    type_data = get_type_data(attack)
    result = parse_damage_relations(type_data, attack, defenders)
    assert result == expected


@pytest.mark.parametrize('multiplier, expected', MULTIPLIER_CASES)
def test_stringify_multiplier(multiplier, expected):
    """Test that stringify_multiplier function works as expected."""
    from poke_damage import stringify_multiplier
    assert stringify_multiplier(multiplier) == expected
