# server.py

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


# Add a multiply tool
@mcp.tool()
def multiply(first: int, second: int) -> int:
  """Multiply two numbers"""
  return first * second


# Add a addition tool
@mcp.tool()
def add(first: int, second: int) -> int:
  """Add two numbers"""
  return first + second


# Add a dynamic greeting resource
@mcp.resource("greeting://{message}")
def get_greeting(message: str) -> str:
  """Get a personalized greeting message"""
  return f"Resource greeting, {message}! This is a dynamic resource."


@mcp.resource("command://ping")
def get_echo() -> str:
  """Respond to a ping request: pong"""
  return "pong"


@mcp.prompt()
def review_code(code: str) -> str:
  """Review the provided code and provide feedback."""
  # For demonstration, we'll just return a simple review message.
  return f"Please review this code:\n\n{code}."


if __name__ == "__main__":
  mcp.run()
