import asyncio

loop = asyncio.get_event_loop()


async def notify(str):
    await asyncio.sleep(60)
    print(str)


def count():
    print("comment done")
    str="notify"
    loop.run_in_executor(None, notify, str)
    print('done')


count()
