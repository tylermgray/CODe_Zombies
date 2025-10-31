## Entry Point

from __future__ import annotations
from app.io_utils import *
from app.ui import *
from app.logic import *
from app.combat import *
from app.models import *
from app.mixer import *
from concurrent.futures import ThreadPoolExecutor
import sys
import threading



def start() -> None:
    ensure_dirs()
    characters = load_json(DATA_DIR / "characters.json")
    weapons = load_json(DATA_DIR / "weapons.json")

    #mixer.play(gamestart_sound(), 4000)
    play_sound(gamestart_sound())

    while True:
        
        choice = main_menu()
        if choice == "q":
            typewriter_print(f"\nGoodbye, thanks for playing!\n")
            sys.exit()
        elif choice == "c":
            state = load_game()
            if not state:
                print(f"{red}No save found or save was corrupt.{white}")
            else:
                print(f"{green}Loaded:{white} {state['player']['name']} ({state['player']['character']}) — Current Round: {red}{state['player']['round']}{white}")
            press_any_key()
            break
        elif choice == "n":
            name = typewriter_input("\nEnter your save name: ").strip() or "Player"
            char_id = character_select(characters)
            state = start_new_game(name, char_id, characters, weapons)
            confirm(f"\nYou chose {state['player']['character']} (favored: {state['player']['favored_type']}).")
            typewriter_print(f"Starter weapon: {state['player']['weapon']['name']}")
            typewriter_print(f"{green}Autosaved to saves/{yellow}save.json{white}")
            press_any_key()
            break
        else:
            print("Choose N, C, or Q.")

def run() -> None:
    ensure_dirs()
    
    state = load_game()
    
    while True:
        
        
        if state['player']['base_hp'] == 0:
            state['player']['base_hp'] = 150
            start()
        
        if state['player']['round'] == 1:           # For loading from a save
            # mixer.play(round_start)
            play_random_zomb_sound(rounds)
        if state['player']['round'] % 6 == 0:       # For loading from a save
            # mixer.play(r6_start)
            # mixer.play(fetch)
            play_sound(r6_start)
            play_sound(fetch)
            start_combat(state, 'special')
        else:
            start_combat(state, 'standard')

def game() -> None:
    start()
    run()

        


if __name__ == "__main__":


    game()
    
    
    
    
    
    
    # mixer = Mixer()

    # mixer_thread = threading.Thread(target=mixer.listen)
    # mixer_thread.start()

    # game_thread = threading.Thread(target=game, args=(mixer,))
    # game_thread.start()
    # game_thread.join()
    #game(mixer)


    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     mixer = Mixer()

    #     executor.submit(mixer.listen)
    #     executor.submit(game, mixer)
        