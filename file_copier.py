import os
import shutil
from pathlib import Path

import shutil
from pathlib import Path

# Assuming base_path is defined outside as:
# base_path = Path('tmcdata/mooc-programming-26')

def extract_save(part_no: str, additional_string: str):
    part = 'part' + part_no
    # We turn this into a Path object immediately to make joining easier
    parent_destination_base = Path(f'HelsinkiUni_MOOC/Advanced Programming/Part_{part_no + additional_string}')

    for file_path in base_path.glob(f"{part}-*/src/*"):
        if file_path.suffix in ['.py', '.txt']:
            folder_name = file_path.parent.parent.name
            # partition returns (before, separator, after)
            _, _, after = folder_name.partition(f"part{part_no}-")
            
            # after is now '01_smallest_average'
            dest_path = parent_destination_base / after

            # Create the folder if it doesn't exist
            dest_path.mkdir(parents=True, exist_ok=True)

            # Copy the file into the new folder
            shutil.copy2(file_path, dest_path)


            
if __name__ == '__main__':
    return None