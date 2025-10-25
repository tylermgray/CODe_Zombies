from __future__ import annotations
from typing import Dict, Any
from app.ui import *

def make_player(name: str, character_id: str, characters: Dict[str, Any], weapons: Dict[str, Any]) -> Dict[str, Any]:
    char = characters[character_id]
    starter_weapon = weapons["pistol"]["colt_1911"]
    return {
        "name": name,
        "character": char["name"],
        "favored_type": char["favored_weapon"],
        "weapon": starter_weapon,
        "base_hp": 150,
        "max hp": 250,
        "round": 1,
        "points": 0
    }


def render_enemy(image):
    enemy = str()

    for row in image:
        for char in row:
            confirmedchar = ""
            match char:
                case "r": 
                    confirmedchar = red
                case "y": 
                    confirmedchar = yellow
                case "w":
                    confirmedchar = white
                case "b":
                    confirmedchar = black
                case _:
                    confirmedchar = char
            enemy += confirmedchar    
        enemy += "\n"


    return enemy