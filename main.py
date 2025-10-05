import asyncio
from threading import Thread
from Inspector_Lestreid.Lestraid import main as lestraid_main
from John_Watson.Watson import main as watson_main

def start_lestraid():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(lestraid_main())

def start_watson():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(watson_main())

if __name__ == "__main__":
    thread1 = Thread(target=start_lestraid)
    thread2 = Thread(target=start_watson)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
