#  ejemplo solamente para montar un servidor SSE en una aplicación web Starlette existente

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
  return JSONResponse({'hello': 'world'})


app = Starlette(debug=True, routes=[
  Route('/', homepage),
])
