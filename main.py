# import subprocess
# from datetime import datetime, time

# current_time = datetime.now().time()

# dark_mode_start_time = time(18, 0)  # 6:00 PM
# dark_mode_end_time = time(6, 0)  # 6:00 AM

# if dark_mode_start_time <= current_time <= dark_mode_end_time:
#     subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Tokyonight-Dark-BL'"])
#     print("Dark theme applied")
# else:
#     subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "'Adwaita'"])
#     print("Light theme applied")


# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# # bluetooth_on_script = os.path.join(script_dir, "/scripts/bluetooth_on.sh") # rfkill unblock bluetooth
# print(script_dir + '/script/bluetooth_ff.sh')


from PyDictionary import PyDictionary

# Create a PyDictionary object
dictionary = PyDictionary()

# Get the definition of a word
word = "example part"
definition = dictionary.meaning(word[0])
print(f"Definition of {word}: {definition}")

# Get synonyms of a word
synonyms = dictionary.synonym(word)
print(f"Synonyms of {word}: {synonyms}")

# Get antonyms of a word
antonyms = dictionary.antonym(word)
print(f"Antonyms of {word}: {antonyms}")
