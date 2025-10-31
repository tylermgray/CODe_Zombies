from app.rng import *
from app.io_utils import *
from app.ui import *
from app.logic import *
from app.sound import *
from app.models import render_enemy
from app.enemy_classes import *
import copy

images_json = load_json(DATA_DIR / "images.json")
zombie_file = images_json["zombie"]["render"]
hell_hound_file = images_json["hell_hound"]["render"]
vermin_file = images_json["vermin"]["render"]

zombie = render_enemy(zombie_file)
hell_hound = render_enemy(hell_hound_file)
vermin = render_enemy(vermin_file)


def player_attack(state, enemy):
    player = state['player']
    player_weapon = player['weapon']
    damage_bonus = player_weapon['attack_bonus']


    if random.randint(1, 5) >= 2:
        player_hit = 1
    else:
        player_hit = 0
    
    if player['favored_type'] == player_weapon['type']:
        damage_bonus += 25

    damage = (player_weapon['attack'] + damage_bonus) * player_weapon['fire_rate'] * player_hit

    gun_image = f"""⠀
 ⣤⣄⣴⣶⣿⣿⣶⣶⣦⣤⣤⣤⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣶⣀⣶⣆⣶⣦
⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿ {yellow}*{red} PEW PEW {yellow}*{white}
⢀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ 
⠈⠛⠛⢿⣿⣿⣿⣿⣿⠛{black}⡟{white}⠛⢿⡿⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⣿⣿⣿⣿⣧⣀⣀⣀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼{black}⣿⣿⣿⣿⣿{white}⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰{black}⣿⣿⣿⣿⣿{white}⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿{black}⣿⣿⣿⣿{white}⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼{black}⣿⣿⣿⣿⣿{white}⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠙⠛⠿⠿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

    
        
    render_text(state, gun_image, 0.001)
    #mixer.play(gun_1911)
    #play_sound(gun_1911)
    if damage == 0:
        render_text(state, f"\n{red}You need to hit the firing range, {yellow}you missed...{white}")
    else:
        state['player']['points'] += 10
        render_text(state, f"\nYou did {red}{damage} damage{white} to {enemy['name']}!")
        
        enemy['base_hp'] -= damage
        

        if enemy['base_hp'] <= 0:
            state['player']['points'] += 250
            play_random_zomb_sound(zomb_death)
            render_text(state, f"\n{yellow}You have {red}defeated{yellow} {enemy['name']}!{white}")
        
        else:
            render_text(state, f"\n{enemy['name']} has {yellow}{enemy['base_hp']} health{white} remaining.")
    

def player_heals(state):
        player = state['player']
        player['base_hp'] += 50
        render_text(state, f"\n{green}You healed{white}, your health is now {green}{player['base_hp']}{white}.")


def player_input(state):
    player = state['player']
    player_choices = [f"{red}[S]{white}hoot", f"{green}[H]{white}eal", f"{black}[M]{white}enu"]

    if player['base_hp'] >= 150:
        player_choices.remove(f"{green}[H]{white}eal")
    
    
    return typewriter_input(f"\nChoose an option:\n{"    ".join(player_choices)}\n>  ").upper() 


def enemy_attack(state, enemy):
    player = state['player']
    damage = enemy['attack']
    
    #damage = enemy.attack

    hit = random.randint(0, 1)
    
    if enemy['base_hp'] > 0:
        if hit == 1:
            player['base_hp'] -= damage
            play_random_zomb_sound(zomb_attk)
            render_text(state, f"\n{enemy['name']} hit you for {red}{damage} damage{white}!")
            #mixer.play(zomb_attack)
            

        else:
            play_random_zomb_sound(zomb_attk)
            render_text(state, f"\n{enemy['name']} swung at you and {yellow}missed!{white}")
            #mixer.play(zomb_attack)
            
            
        if player['base_hp'] <= 0:
            #mixer.play(game_over_sound())
            play_random_zomb_sound(game_over_sounds)
            typewriter_print(f"\nBeep bop bope beep. You died!")
            time.sleep(30.00)
            sys.exit()
        

def start_combat(state, enemy_type) -> None:
    enemies_json = load_json(DATA_DIR / "enemies.json")
    enemies = enemies_json[enemy_type]
    keys = list(enemies.keys())
    
    
    if state['player']['round'] % 6 == 0 and enemy_type == 'special':
        enemy = enemies_json['special']['hell_hound']
    else:
        enemy = enemies[random.choice(keys)]

    original_enemy = copy.deepcopy(enemy)

    for x in range(math.ceil(state['player']['round'] * 1.5)):

        if enemy['tags'] == ['normal']:
            render_text(state, zombie, 0.003)
            if state['player']['round'] < 8:
                #mixer.play(growl1)
                play_random_zomb_sound(zomb_amb)
            else:
                #mixer.play(sprinter1)
                play_random_zomb_sound(zomb_sprint)
            
        elif enemy['tags'] == ['special'] and enemy['name'] == 'Hell Hound':
            render_text(state, hell_hound, 0.003)

        elif enemy['tags'] == ['special'] and enemy['name'] == 'Vermin':
            render_text(state, vermin, 0.003)

        render_text(state, f"\nYou've encountered a {enemy['name']}!")

        while enemy['base_hp'] > 0 and state['player']['base_hp'] > 0:
            player_choice = player_input(state)

            if player_choice == 'S':
                player_attack(state, enemy)
                
            elif player_choice == 'H':
                if state['player']['base_hp'] >= 150:
                    render_text(state, "\nInvalid input. Try again\n")
                else:
                    player_heals(state)
            elif player_choice == 'M':
                between_round_menu(state)
            else:
                render_text(state, "Invalid input, try again.")
                return    

            
            enemy_attack(state, enemy)
        
        if state['player']['base_hp'] <= 0:
            break

        enemy = copy.deepcopy(original_enemy)
                
            



    if state['player']['base_hp'] > 0:
        state['player']['round'] += 1
        typewriter_print(f"\nWelcome to {red}Round {state['player']['round']}{white}")
        if state['player']['round'] % 6 == 0:
            #mixer.play(r6_start)
            #mixer.play(fetch)
            play_sound(r6_start)
            play_sound(fetch)
        elif state['player']['round'] % 6 == 1:
            #mixer.play(r6_end)
            play_sound(r6_end)
        else:
            #mixer.play(round_start)
            play_random_zomb_sound(rounds)
            return True
    else:
        state['player']['round'] = 0
        return False
        

# def 

