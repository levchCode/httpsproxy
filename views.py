import os
from urllib.parse import urljoin
import aiohttp
from aiohttp import web

TARGET_URL = os.environ.get('TARGET_URL')


def get_new_url(url: web.Request.url) -> str:
    new_url = urljoin(TARGET_URL, url.path) if url.path != '/' else TARGET_URL
    new_url = urljoin(new_url, url.query_string)
    return new_url


async def comment(request: web.Request) -> web.Response:
    async with aiohttp.ClientSession() as session:
        new_url = get_new_url(request.url)
        print(new_url)
        data = await request.read()
        print(data)
        print(request.headers)
        async with session.post(new_url, data=data, headers={'content-type': 'application/json'}) as resp:
            content = await resp.read()
            return web.Response(body=content, status=resp.status, headers=resp.headers)


async def default_get(request: web.Request) -> web.Response:
    async with aiohttp.ClientSession() as session:
        new_url = get_new_url(request.url)
        async with session.get(new_url) as resp:
            content = await resp.read()
            return web.Response(body=content, status=resp.status, headers=resp.headers)
