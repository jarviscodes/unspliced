import os
import glob
from pathlib import Path
import shutil

# default path for splice samples is: %USERPROFILE%/Documents/Splice/Samples/packs

AVAILABLE_INSTRUMENTS = [
    "kick",
    "snare",
    "clap",
    "hat",
    "vocal",
    "bass",
    "perc",
    "songstarter",
    "fill"
]

def auto_detect_splice():
    print("Trying to autodetect your splice folder")
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


def create_file_structure(root="/"):
    new_sample_path = Path(root) /  "samples"
    if not new_sample_path.exists():
        new_sample_path.mkdir()

    for instrument in AVAILABLE_INSTRUMENTS:
        instrument_path = new_sample_path / instrument
        if not instrument_path.exists():
            instrument_path.mkdir()

    # create "other" dir
    other_dir = new_sample_path / "other"
    if not other_dir.exists():
        other_dir.mkdir()

    return new_sample_path

def main():
    new_root = create_file_structure()
    all_sound_files = dive_until_ext()
    for sound_file in all_sound_files:
        stem = Path(sound_file).stem
        instrument = find_instrument(stem)

        if not instrument:
            print("Could not find instrument for: ", stem)
            instrument = "other"

        shutil.copy(Path(sound_file), new_root / instrument)


main()