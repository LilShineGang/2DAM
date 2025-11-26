# python main.py 5
import sys
import asyncio

from datetime import datetime


async def main(secs: int):
    while True:
        with open("web/index.html", "a") as fd:
            fd.write(f"{str(datetime.now())}\n")
        await asyncio.sleep(secs)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Error: usage: python {sys.argv[0]} <seconds>")
        exit(1)

    s = int(sys.argv[1])

    asyncio.run(main(s))
