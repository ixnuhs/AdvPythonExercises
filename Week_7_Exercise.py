import asyncio
from timeit import default_timer
from aiohttp import ClientSession
import aiofiles

async def get_and_write_html(url):
    async with ClientSession() as session:
        async with session.get(url) as resp:
                return await resp.text()

async def write_html(name, data):
    async with aiofiles.open(name, 'w+', encoding="utf-8") as f:
        await f.write(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()    
    urls = ['https://nytimes.com',
                'https://github.com',
                'https://google.com',
                'https://reddit.com',
                'https://producthunt.com']
    for url in urls:
        html = loop.run_until_complete(get_and_write_html(url))
        name = url.split(".")[-2]
        f_name = name.split("//")[1] + '.txt'
        loop.run_until_complete(write_html(f_name, html))
