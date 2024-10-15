import asyncio
import cProfile
import os

import numpy as np

yield_task_count = 0
yield_task_count_2 = 0
cpu_bound_task_count = 0
cpu_bound_task_count_2 = 0


async def yield_task():
    global yield_task_count
    yield_task_count += 1
    print("yield_task_count", yield_task_count)
    for _ in range(1000):
        await asyncio.sleep(0.01)


async def yield_task_2():
    global yield_task_count_2
    yield_task_count_2 += 1
    print("yield_task_count_2", yield_task_count_2)
    for _ in range(1000):
        await asyncio.sleep(0.01)


async def cpu_bound_task():
    n = 3000
    global cpu_bound_task_count
    cpu_bound_task_count += 1
    print("cpu_bound_task_count", cpu_bound_task_count)
    for i in range(30):
        print("cpu_bound_task", i)
        matrix1 = np.random.rand(n, n)
        matrix2 = np.random.rand(n, n)
        _ = np.dot(matrix1, matrix2)


async def cpu_bound_task_2():
    n = 3000
    global cpu_bound_task_count_2
    cpu_bound_task_count_2 += 1
    print("cpu_bound_task_count_2", cpu_bound_task_count)
    for i in range(30):
        print("cpu_bound_task_2", i)
        matrix1 = np.random.rand(n, n)
        matrix2 = np.random.rand(n, n)
        _ = np.dot(matrix1, matrix2)


async def main():
    yield_task_future = asyncio.create_task(yield_task())
    yield_task_2_future = asyncio.create_task(yield_task_2())
    # cpu_bound_task_future = asyncio.create_task(cpu_bound_task())
    # cpu_bound_task_2_future = asyncio.create_task(cpu_bound_task_2())

    # await asyncio.gather(yield_task_future, cpu_bound_task_future)
    # await asyncio.gather(cpu_bound_task_future, cpu_bound_task_2_future)
    await asyncio.gather(yield_task_future, yield_task_2_future)


if __name__ == "__main__":
    cProfile.run(asyncio.run(main()), "profile_data")
