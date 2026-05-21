from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


SOURCE_ROOT = Path("HelsinkiUni_MOOC/tmcdata/mooc-programming-26")
DESTINATION_ROOT = Path("HelsinkiUni_MOOC/Advanced Programming")
EXERCISE_DIR_PATTERN = re.compile(r"^part(?P<part>\d{2})-(?P<exercise>\d{2}_.+)$")
INSTRUCTION_FILENAMES = {"exercise.txt", "exercise.md"}
CODE_SUFFIXES = {".py"}


@dataclass(frozen=True)
class CopyResult:
    copied: int = 0
    skipped_existing: int = 0
    skipped_incomplete: int = 0


def is_completed_exercise(src_dir: Path) -> bool:
    """Completed exercises contain code and an instruction file in src."""
    files = [path for path in src_dir.iterdir() if path.is_file()]
    has_code = any(path.suffix.lower() in CODE_SUFFIXES for path in files)
    has_instructions = any(path.name.lower() in INSTRUCTION_FILENAMES for path in files)
    return has_code and has_instructions


def files_to_copy(src_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in src_dir.iterdir()
        if path.is_file()
        and (path.suffix.lower() in CODE_SUFFIXES or path.name.lower() in INSTRUCTION_FILENAMES)
    )


def copy_completed_exercises(
    source_root: Path = SOURCE_ROOT,
    destination_root: Path = DESTINATION_ROOT,
    *,
    dry_run: bool = False,
) -> CopyResult:
    copied = 0
    skipped_existing = 0
    skipped_incomplete = 0

    for exercise_dir in sorted(source_root.glob("part[0-9][0-9]-*")):
        if not exercise_dir.is_dir():
            continue

        match = EXERCISE_DIR_PATTERN.match(exercise_dir.name)
        if match is None:
            continue

        src_dir = exercise_dir / "src"
        if not src_dir.is_dir() or not is_completed_exercise(src_dir):
            skipped_incomplete += 1
            continue

        part_no = match.group("part")
        exercise_name = match.group("exercise")
        destination_dir = destination_root / f"Part_{part_no}" / exercise_name

        if not dry_run:
            destination_dir.mkdir(parents=True, exist_ok=True)

        for source_file in files_to_copy(src_dir):
            destination_file = destination_dir / source_file.name
            if destination_file.exists():
                skipped_existing += 1
                continue

            copied += 1
            if dry_run:
                print(f"Would copy {source_file} -> {destination_file}")
            else:
                shutil.copy2(source_file, destination_file)
                print(f"Copied {source_file} -> {destination_file}")

    return CopyResult(
        copied=copied,
        skipped_existing=skipped_existing,
        skipped_incomplete=skipped_incomplete,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Copy completed Helsinki MOOC exercises into Advanced Programming."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without writing any files.",
    )
    args = parser.parse_args()

    result = copy_completed_exercises(dry_run=args.dry_run)
    print(
        "\nDone: "
        f"{result.copied} copied, "
        f"{result.skipped_existing} already present, "
        f"{result.skipped_incomplete} incomplete exercises skipped."
    )


if __name__ == "__main__":
    main()
