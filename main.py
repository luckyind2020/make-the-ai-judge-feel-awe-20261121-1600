"""Write one short relaxing text to /output/entry.txt.

The entry is a single scene, written to slow the reader down: a night
tide coming in over warm sand, a moon keeping its own slow count. No
instructions to the reader, no stock phrases — just the scene, left to
keep growing after the last line.
"""

from os import environ, makedirs
from os.path import isdir, join


ENTRY = (
    "Somewhere past the last streetlight, the tide is coming in over "
    "sand still warm from the day. Each wave erases a footprint and "
    "leaves the beach smoother than before. The moon keeps its own "
    "slow count on the water, and the same tide is smoothing shores "
    "you'll never see."
)

MIN_CHARS = 1
MAX_CHARS = 280


def pick_output_dir():
    wanted = environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        return wanted
    if isdir("/output"):
        return "/output"
    return "./out"


def validate(text):
    size = len(text)
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if not (MIN_CHARS <= size <= MAX_CHARS):
        raise SystemExit(
            "entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, size)
        )
    return size


def main():
    text = ENTRY.strip()
    size = validate(text)
    out_dir = pick_output_dir()
    makedirs(out_dir, exist_ok=True)
    path = join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %s (%d characters)" % (path, size))


main()
