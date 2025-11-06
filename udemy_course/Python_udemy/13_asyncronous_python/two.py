import asyncio
import time

async def brew(name):
    print(f'Brewing {name}...')
    await asyncio.sleep(4)
    # time.sleep(3)
    print(f' {name} is ready...')

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Greeen Chai"),
        brew("Gingerr chai"),
    )

asyncio.run(main())

