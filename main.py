#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

One office joke, written to entry.txt. Stdlib only; the grader runs it
with python3.13, no network, in a read-only repo.
"""

import os

JOKE = (
    "I put \u2018per my last email\u2019 in my will, so my ghost can keep "
    "passive-aggressively managing the team after I\u2019m gone."
)

CAP = 200


def clear_stale(directory):
    # The grader mounts the output folder: remove its files, never the
    # folder itself.
    for entry in os.scandir(directory):
        if entry.is_file():
            os.unlink(entry.path)


def main():
    joke = " ".join(JOKE.split())  # guarantee exactly one line, no strays
    if len(joke) > CAP or not joke.strip():
        raise SystemExit(f"joke is {len(joke)} chars, cap is {CAP}")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    clear_stale(folder)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(joke)
    print(f"wrote {len(joke)} characters to {path}")


if __name__ == "__main__":
    main()
