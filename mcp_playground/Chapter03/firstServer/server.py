# server.oy

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


# Add a multiply tool
@mcp.tool()
def multiply(first: int, second: int) -> int:
  """Multiply two numbers"""
  return first * second


# Add a dynamic greeting resource
@mcp.resource("greeting://{message}")
def get_greeting(message: str) -> str:
  """Get a personalized greeting message"""
  return f"Resource greeting, {message}!"


@mcp.prompt()
def review_code(code: str) -> str:
  """Review the provided code and provide feedback."""
  # For demonstration, we'll just return a simple review message.
  return f"Please review this code:\n\n{code}."
