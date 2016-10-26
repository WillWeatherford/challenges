"""Challenge from reddit.com/r/dailyprogrammer.

Description

In the popular Pokémon games all moves and Pokémons have types that determine
how effective certain moves are against certain Pokémons.

These work by some very simple rules, a certain type can be super effective,
normal, not very effective or have no effect at all against another type.
These translate respectively to 2x, 1x, 0.5x and 0x damage multiplication.
If a Pokémon has multiple types the effectiveness of a move against this
Pokémon will be the product of the effectiveness of the move to it's types.

Formal Inputs & Outputs
Input

The program should take the type of a move being used and the types of the
Pokémon it is being used on.

Example inputs

 fire -> grass
 fighting -> ice rock
 psychic -> poison dark
 water -> normal
 fire -> rock

Output

The program should output the damage multiplier these types lead to.

Example outputs

2x
4x
0x
1x
0.5x

Notes/Hints

Since probably not every dailyprogrammer user is an avid Pokémon player that
knows the type effectiveness multipliers by heart here is a Pokémon type chart.
Bonus 1

Use the Pokémon api to calculate the output damage.

Like

http://pokeapi.co/api/v2/type/fire/

returns (skipped the long list)

{
    "name":"fire",
    "generation":{
        "url":"http://pokeapi.co/api/v2/generation/1/",
        "name":"generation-i"
    },
    "damage_relations":{
        "half_damage_from":[
            {
                "url":"http://pokeapi.co/api/v2/type/7/",
                "name":"bug"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/9/",
                "name":"steel"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/10/",
                "name":"fire"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/12/",
                "name":"grass"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/15/",
                "name":"ice"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/18/",
                "name":"fairy"
            }
        ],
        "no_damage_from":[

        ],
        "half_damage_to":[
            {
                "url":"http://pokeapi.co/api/v2/type/6/",
                "name":"rock"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/10/",
                "name":"fire"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/11/",
                "name":"water"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/16/",
                "name":"dragon"
            }
        ],
        "double_damage_from":[
            {
                "url":"http://pokeapi.co/api/v2/type/5/",
                "name":"ground"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/6/",
                "name":"rock"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/11/",
                "name":"water"
            }
        ],
        "no_damage_to":[

        ],
        "double_damage_to":[
            {
                "url":"http://pokeapi.co/api/v2/type/7/",
                "name":"bug"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/9/",
                "name":"steel"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/12/",
                "name":"grass"
            },
            {
                "url":"http://pokeapi.co/api/v2/type/15/",
                "name":"ice"
            }
        ]
    },
    "game_indices":[
       ...
    ],
    "move_damage_class":{
        ...
    },
    "moves":[
        ...
    ],
    "pokemon":[
        ...
    ],
    "id":10,
    "names":[
        ...
    ]
    }

If you parse this json, you can calculate the output, instead of hard coding
it.

Bonus 2

Deep further into the api and give the multiplier for folowing

fire punch -> bulbasaur
wrap -> onix
surf -> dwegong

side note

the api replaces a space with a hypen (-)
"""

import requests

DDT = 'double_damage_to'
HDT = 'half_damage_to'

DAMAGES = {
    DDT: 2,
    HDT: 0.5,
}
API_TYPE_URL = 'http://pokeapi.co/api/v2/type'


def calculate(attack_string):
    """Calculate damage multiplyer."""
    attack_type, defenders = parse_input(attack_string)
    type_data = get_type_data(attack_type)
    damage = parse_damage_relations(type_data, attack_type, defenders)


def parse_input(attack_string):
    """Parse input."""
    try:
        attack, defenders = attack_string.split(' -> ')
    except TypeError:
        raise ValueError(
            'Correct format: '
            '"attack1 [attack2 ...] -> defend1 [defend2 ...]"'
        )
    defenders = set(defenders.split())
    return attack, defenders


def get_type_data(attack_type):
    """Get JSON data about a given Pokemon attack type."""
    url = '/'.join((API_TYPE_URL, attack_type))
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError('Invalid Pokemon attack type.')
    return response.json()


def parse_damage_relations(type_data, attack, defenders):
    """Reduce and simplify type_data on damage relations."""
    output = dict.fromkeys(defenders, 1)
    damage_relations = type_data['damage_relations']

    for damage_rel, multiplier in DAMAGES.items():
        damage_types = damage_relations[damage_rel]

        for damage_type in damage_types:
            if damage_type['name'] in defenders:
                output[damage_type['name']] = multiplier

    return output
