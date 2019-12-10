#!/usr/bin/env python3
# chained.py

import asyncio
import random
import time
import sys


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result


async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result


async def chain(n: int) -> None:
    startchain = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    endchain = time.perf_counter() - startchain
    print(f"-->Chained result{n} => {p2} (took {endchain:0.2f} seconds).")


async def main(*arg):
    await asyncio.gather(*(chain(n) for n in arg))


if __name__ == "__main__":
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
