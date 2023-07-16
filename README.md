# ✨ Amy's Barony Save Loader ✨
A program for ~~cheating~~ 😵‍💫 _managing save files_ for the game [Barony](https://store.steampowered.com/app/371970/Barony/).

Leaving the program running while you play your game will store saves of your progress at the beginning of each level. Using this, the save loader can restore your progress when you die! 👻

# How to do it 🧠

Here's what you ought to see when you start up the script:

![startscreen](https://github.com/casual-wizardry/barony-save-loader/assets/32003364/a5b34366-7abb-443c-9a17-e091a583cdc9)

Wow! You even have a little buddy there to help! Very cool! :3 

**To use the save loader with a new game**, simply select \[1\] 'start a new game' and then, leaving the console open, you can start a new save as you normally would within the game. The script will save your progress automatically at the beginning of each level and will also automatically restore your save upon death. When you're finished playing, exit the game as you usually would and then close the console window. 

**To resume your game at a later time**, start the script and use option \[2\] to select your save before opening the game. The script will then resuming saving your progress as you play. 

**Oops, did you start a game on Barony without running the save loader that you'd like to start saving progress from?** Using option \[3\] 'import an old save' you can start saving progress on this game too.

Finally, if you'd like to **delete some data** that the save loader has stored you can use \[4\] 'delete a save' to do this. Note that this will leave the files in the ordinary Barony save directory unaffected. 

At any time if you'd like to stop using the save loader you can simply delete the 'saveloader' folder from your save directory!

# Setup Info 🔧

If you'd like to try it out, here are two methods of setting up the program:

### Method 1: Using Python
If you have Python installed on your computer, then you could run the script directly by following these steps:

1. Navigate to your Barony save directory. (If you have the game on Steam, this will be something like "...\Steam\steamapps\common\Barony\savegames")
      
2. Create a folder there and call it 'saveloader'
      
3. Download the script file called 'saver.py' from the repository and place a copy of it in the 'saveloader' folder.
      
4. Now you can launch the save loader however you would usually launch a Python script. (For example, by navigating to the directory with the command prompt and using the command 'python saver.py')
     
### Method 2: Pre-compiled
Otherwise, you could use the pre-compiled version* as follows:
      
1. Navigate to your Barony save directory. (If you have the game on Steam this will be something like "...\Steam\steamapps\common\Barony\savegames")
      
2. Download the zip archive from the releases tab (currently v1)
      
3. Unzip this and copy the folder called 'saveloader' into your Barony save directory.
      
4. Now you can launch the save loader whenever you like using 'launch.exe'

\* A note on the pre-compiled version: This was made using the pyinstaller library. It is a little larger than the script by itself simply because pyinstaller includes the files necessary to run the script on a computer without a Python installation. I don't have a lot of experience with pyinstaller, so if anyone notices any issues with this please let me know!

Anyway, for anyone who happens to stumble across this and try it out, I hope it helps make playing the game just a little more enjoyable!

Have fun,

Amy <3
