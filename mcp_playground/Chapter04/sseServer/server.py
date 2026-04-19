# Servidor SSE en una aplicación web Starlette existente

from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")


@mcp.tool()
def add(a: int, b: int) -> int:
  """A simple tool that adds two numbers together."""
  return a + b


# Mount the SSE server to the existing Asynchronous Server Gateway Interface (ASGI) server
app = Starlette(routes=[
  Mount('/', app=mcp.sse_app()),
])

# Or dynamically add the SSE server to an existing ASGI app
app.router.routes.append(Host("mcp.acme.corp", "app=mcp.sse_app()"))
