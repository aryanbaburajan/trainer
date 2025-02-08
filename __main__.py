import os
import shutil
import random
from pathlib import Path
import argparse

def move_random_images(bank_dir, num_problems, num_sets, overwrite):
    source_path = Path(bank_dir) / "qs"
    output_path = Path(bank_dir) / "sets"

    if not source_path.exists() or not source_path.is_dir():
        print(f"source directory '{source_path}' does not exist or is not a directory.")
        return

    if overwrite and output_path.exists():
        shutil.rmtree(output_path)
    
    output_path.mkdir(parents=True, exist_ok=True)

    image_files = list(source_path.glob("*.jpg")) + list(source_path.glob("*.png"))

    if not image_files:
        print(f"no images found in '{source_path}'.")
        return

    image_files = list(source_path.glob("*.jpg")) + list(source_path.glob("*.png"))
    unique_id = len(list(output_path.iterdir())) + 1

    for i in range(num_sets):
        selected_images = random.sample(image_files, min(len(image_files), num_problems))

        target_dir = output_path / str(unique_id)
        target_dir.mkdir(parents=True)

        for index, img in enumerate(selected_images, start=1):
            shutil.copy(str(img), target_dir / f"{index}{img.suffix}")

        unique_id += 1

    print(f"created {num_sets} problemset(s)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate a problemset from a question bank.")
    parser.add_argument("bank_dir", type=str, help="path to the question bank directory.")
    parser.add_argument("num_problems", type=int, help="number of problems per set.")
    parser.add_argument("num_sets", type=int, help="number of total sets.", default=1)
    parser.add_argument("-o", "--overwrite", action="store_true", help="delete existing sets before creating new ones.")
    args = parser.parse_args()

    move_random_images(args.bank_dir, args.num_problems, args.num_sets, args.overwrite)