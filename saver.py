from os import listdir, getcwd, makedirs, path
from shutil import copy, rmtree
from json import loads
from time import sleep

PATH = getcwd()[:-11]

classes = {
0 : 'barbarian',
1 : 'warrior',
2 : 'healer',
3 : 'rogue',
4 : 'wanderer',
5 : 'cleric',
6 : 'merchant',
7 : 'wizard',
8 : 'arcanist',
9 : 'joker',
10 : 'sexton',
11 : 'ninja',
12 : 'monk',
13 : 'conjurer',
14 : 'accursed',
15 : 'mesmer',
16 : 'brewer',
17 : 'mechanist',
18 : 'punisher',
19 : 'shaman',
20 : 'hunter'
}

races = {
0 : 'human',
1 : 'skeleton',
2 : 'vampire',
3 : 'succubus',
4 : 'goatman',
5 : 'automaton',
6 : 'incubus',
7 : 'goblin',
8 : 'insectoid'
}

pic ="                                                                      \n                                                                      \n    ░░██        ██████████        ██        ████                      \n    ██▒▒██  ████          ████  ██▒▒██    ██▒▒▒▒██                    \n    ██▒▒▒▒██                  ██▒▒▒▒██    ██▒▒▒▒██                    \n    ██▒▒▒▒                      ▒▒▒▒██      ██▒▒▒▒██                  \n    ██▒▒                          ▒▒██      ██▒▒▒▒██    ░░            \n  ██      ████  ▒▒▒▒▒▒▒▒▒▒  ████      ██      ██▒▒▒▒██                \n██        ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████        ██    ██▒▒▒▒██                \n██          ▒▒▒▒▒▒██████▒▒▒▒            ██    ██▒▒▒▒██                \n██        ▒▒▒▒██▒▒▒▒██▒▒▒▒██▒▒          ██░░  ██▒▒▒▒██  ░░      ░░    \n  ██      ▒▒▒▒▒▒████▒▒████▒▒▒▒        ████    ██▒▒▒▒██                \n    ██      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ██    ████▒▒▒▒██                  \n      ████    ▒▒▒▒▒▒▒▒▒▒▒▒      ████        ██▒▒▒▒██                  \n        ████████          ████████          ██▒▒██                    \n        ██      ██████████                        ██                  \n        ██                                        ██                  \n        ██                                        ██            ░░    \n        ██                                      ▒▒██                  \n        ██▒▒    ██        ██      ██      ██▒▒▒▒▒▒██                  \n          ██▒▒▒▒██        ██  ▒▒  ██  ██████▒▒▒▒██                    \n          ██▒▒▒▒▒▒██████████▒▒▒▒██████▒▒██▒▒▒▒▒▒██                    \n          ██▒▒▒▒▒▒██    ██▒▒▒▒  ██  ██▒▒██▒▒▒▒██                      \n            ██▒▒▒▒██    ██▒▒▒▒██    ████▒▒▒▒▒▒██                      \n            ██▒▒▒▒██    ██▒▒▒▒██      ██▒▒▒▒██                        \n    ░░        ████        ████          ████                          \n                                                                      \n"


def get_new_save(): # runs to collect the new game data
    wait = True
    old_dir = [save for save in listdir(PATH) if save[-11:] == '.baronysave']
    prev = len(old_dir)

    while wait:
        read_dir = [save for save in listdir(PATH) if save[-11:] == '.baronysave']

        if len(read_dir) != prev:
            new_save = [x for x in read_dir if x not in old_dir][0]
            wait = False
        else:
            sleep(10)

    return new_save


def save_selection(location): # presents save data options to load and returns choice
    save_data = listdir(location)
    games = {}
    val = 1

    for game in save_data:
        latest = ("", 0, 0)

        if game == 'saveloader':
            continue
        elif game[-11:] != '.baronysave':
            for save in listdir(location + "\\" + game):
                source = location + "\\" + game + "\\" + save
                with open(source, "r") as save_file:
                    data = loads(save_file.read())

                dungeon_lvl = data['dungeon_lvl']
                level_track = data['level_track']

                if dungeon_lvl >= latest[1] and level_track <= latest[2]:
                    latest = (save, dungeon_lvl, level_track)

                save_file.close()
            source = location + "\\" + game + "\\" + latest[0]
        else:
            source = location + "\\" + game

        with open(source, "r") as save_file:
            data = loads(save_file.read())

        game_name = data['game_name']
        gamekey = data['gamekey']
        timestamp = data['timestamp']
        dungeon_lvl = data['dungeon_lvl']
        level_track = data['level_track']
        player_level = data['players'][0]['stats']['LVL']
        player_race = data['players'][0]['race']
        player_class = data['players'][0]['char_class']
        game_path = source

        save_file.close()

        name = '[' + str(val) + '] ' + str(game_name) + ' ' + str(dungeon_lvl) + '_' + str(level_track) + ' ' + 'lvl' + str(player_level) + ' ' + races[player_race] + ' ' + classes[player_class] + ' ' + timestamp
        print(name)

        games[val] = (gamekey, dungeon_lvl, level_track, game_path, name, timestamp)
        val += 1

    valid = False
    while not valid:
        selection = input('\n')
        print('\n')
        if selection in [str(x) for x in range(1,val + 1)]:
            valid = True
        else:
            print('invalid choice, try again!!! >w<\n')

    return games[int(selection)]


def catch_saves(gamekey, latest_lvl, latest_track, backup_path=''):
    wait = True
    target_dir = PATH + "\saveloader\saves" + "\\" + str(gamekey)
    dir = [save for save in listdir(PATH) if save[-11:] == '.baronysave']

    count = len(dir)

    found = False
    for save in dir:  # finds save file corresponding to chosen game to load
        source = PATH + "\\" + str(save)
        with open(source, "r") as save_file:
            data = loads(save_file.read())
        key = data['gamekey']
        save_file.close()
        if key == gamekey:
            found = True
            active = save
            break

    if not found:  # replaces missing save file
        dir_vals = [int(save[8:-11]) for save in dir]
        if len(dir_vals) == 0:
            label = 0
        else:
            label = max(dir_vals) + 1
        active = 'savegame' + str(label) + '.baronysave'
        copy(backup_path, PATH + "\\" + active)
        print("i couldn't find the save you were looking for, so i restored it from the backup! ;)\n")
        count += 1

    while wait:
        dir = [save for save in listdir(PATH) if save[-11:] == '.baronysave']
        if len(dir) != count:
            print('ohnoo you died!! >w<\n')
            save_dir = listdir(target_dir)
            for save in save_dir:
                with open(target_dir + "\\" + save, "r") as save_file:
                    data = loads(save_file.read())
                lvl = data['dungeon_lvl']
                track = data['level_track']
                if lvl == latest_lvl and track == latest_track:
                    copy(target_dir + "\\" + save, PATH + "\\" + active)
            print('no worries, i restored your save -.^\n')

        source = PATH + "\\" + str(active)
        with open(source, "r") as save_file:
            data = loads(save_file.read())

        dungeon_lvl = data['dungeon_lvl']
        level_track = data['level_track']
        timestamp = data['timestamp']

        save_file.close()

        if dungeon_lvl != latest_lvl or level_track != latest_track:
            copy(source, target_dir + "\\" + "Floor" + str(dungeon_lvl) + "_" + str(level_track) + " " + str(timestamp))
            latest_lvl = dungeon_lvl
            latest_track = level_track
            print(str(timestamp) + ' ' + 'level ' + str(dungeon_lvl) + "_" + str(level_track) + ' ' + 'new save recorded! :)\n')

        sleep(10)


def delete_save():
    print(';w; which save would u like to delete?\n')

    game = save_selection(PATH + "\saveloader\saves")

    print('you selected: ' + game[4] + '\n')
    wish = input("type 'awawa' to confirm your wish to end this innocent file's life...\n")
    print('\n')

    if wish == 'awawa':
        rmtree(PATH + "\saveloader\saves" + "\\" + str(game[0]))

    next = input('delete another? (y/n)\n')
    print('\n')
    if next == 'y' or next == 'Y':
        delete_save()
    else:
        print('\n\n')
        main()


def main():
    if not path.exists(PATH + "\saveloader\saves"):
        makedirs(PATH + "\saveloader\saves")

    print(pic)
    print('hiii :3c\n')

    valid = False
    while not valid:
        play_type = input('what would you like to do?\n\n[1] start a new game\n[2] load a save\n[3] import an old save\n[4] delete a save\n\n')
        print('\n')
        if play_type in ['1','2','3', '4']:
            valid = True
        else:
            print('invalid choice, try again!!! >w<\n')

    if play_type == '1':
        print("waiting for u to start the game...\n")
        new_save = get_new_save()
        print("owo notices your new game,..,,\n")

        source = PATH + "\\" + new_save

        with open(source, "r") as save_file:
            data = loads(save_file.read())

        gamekey = data['gamekey']
        timestamp = data['timestamp']
        dungeon_lvl = data['dungeon_lvl']
        level_track = data['level_track']

        save_file.close()

        target_dir = PATH + "\saveloader\saves" + "\\" + str(gamekey)
        makedirs(target_dir)

        copy(source, target_dir + "\\" + "Floor" + str(dungeon_lvl) + "_" + str(level_track) + " " + str(timestamp))

        catch_saves(gamekey, latest_lvl=0, latest_track=0)
    elif play_type == '2':
        #interface for choosing save then run catch_saves(gamekey)
        print('okie... which save would you like to return to? :>\n')

        game = save_selection(PATH + "\saveloader\saves")

        gamekey = game[0]
        dungeon_lvl = game[1]
        level_track = game[2]
        game_path = game[3]

        print('nice choice! you can now open the save file <3\n')
        catch_saves(gamekey, dungeon_lvl, level_track, backup_path=game_path)
    elif play_type == '3':
        valid = False
        while not valid:
            print('which game file would you like to import into the save loader?\n')
            game = save_selection(PATH)

            save_dir = listdir(PATH + "\saveloader\saves")

            valid = True
            for save in save_dir:
                if game[0] == save: # checks if game keys agree
                    valid = False
                    print('that game has already been imported!!\n')
                    action = input('choose again? (y/n)\n')
                    if not (action == 'y' or action =='Y'):
                        print('\n')
                        main()
                    break

        dungeon_lvl = game[1]
        level_track = game[2]
        timestamp = game[5]
        source_dir = game[3]
        target_dir = PATH + "\saveloader\saves\\" + str(game[0])

        makedirs(target_dir)
        copy(source_dir, target_dir + "\\" + "Floor" + str(dungeon_lvl) + "_" + str(level_track) + " " + str(timestamp))

        print('your game file has been imported-- select it from the load screen when you want to play! ^_^\n\n')

        main()
    elif play_type == '4':
        delete_save()
    else:
        play_type = input('invalid choice!!! >w<\n')
        print('\n')
        sleep(5)


if __name__ == '__main__':
    main()
