from aiohttp import web

import views

app = web.Application()
app.add_routes(
    [
        web.post('/comment', views.comment),
        web.get('/{tail:.*}', views.default_get),
    ]
)
