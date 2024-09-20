import os
import glob
from pathlib import Path

# default path for splice samples is: %USERPROFILE%/Documents/Splice/Samples/packs

AVAILABLE_INSTRUMENTS = [
    "kick",
    "snare",
    "clap",
    "hat",
    "vocal"
]

def auto_detect_splice():
    print("Trying to autodetect your splice folder")
    if os.name == "nt":
        home_path = Path.home()
        guessed_path = home_path / "Documents/Splice/Samples/packs"
        if guessed_path.exists():
            print("Found splice packs under: ", guessed_path)
            return guessed_path

def find_instrument(file_stem):
    tmp_stem = file_stem.lower()
    for instrument in AVAILABLE_INSTRUMENTS:
        if instrument in tmp_stem:
            return instrument


def dive_until_ext(extension: str = ".wav"):
    all_sound_files = []
    guessed_path = auto_detect_splice()
    if guessed_path:
        all_sound_files = [sound_file for sound_file in glob.glob(str(guessed_path / "**" / f"*{extension}"), recursive=True)]
    return all_sound_files




all_sound_files = dive_until_ext()