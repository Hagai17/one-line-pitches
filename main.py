"""Write one pitch sentence to /output/entry.txt.

The sentence is a single line of at most 240 characters that convinces a
friend who has never coded to let an AI agent build their first app idea
on make.fun.
"""

import os

LINE = (
    "That app idea you've been carrying around all year? Say it on "
    "make.fun in plain words and an AI agent builds the first draft — "
    "all you risk is ten minutes, and you can tell it what to fix."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
