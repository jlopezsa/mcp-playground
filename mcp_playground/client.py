import json
import subprocess
import sys

from mcp_playground.utils.messages import (
  initialized_message,
  initialize_message,
  list_tools_message,
)

# proc es un objeto proceso que representa el servidor MCP ejecutándose como un subproceso.
proc = subprocess.Popen([sys.executable, "-m", "mcp_playground.server"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        text=True)


def send_message(proc, message):
  """Send a message to the child process."""
  print(f"[🤵 CLIENT -> 💻 SERVER] Sending message to server Message: {message.strip()}")
  proc.stdin.write(message)
  proc.stdin.flush()


def serialize_message(message):
  """Serialize a message to JSON format."""
  return json.dumps(message) + "\n"


def print_response(response, prefix=""):
  """Print the response from the server."""
  try:
    parsed = json.loads(response)
    print(prefix, json.dumps(parsed, indent=2))
  except json.JSONDecodeError:
    print(prefix, response.strip())


def connect():
  '''Connect to the server and perform the initialization handshake.
  This function sends the initialize message to the server, waits for the response,
  and then sends the initialized notification.
  
  - Send message and Read response
  '''
  print("🏁🏁🏁  Connecting to the server...  🏁🏁🏁")
  # 1. Ask for capabilities, send a JSON-RPC message to the server to ask for its capabilities
  print("[🤵 CLIENT 1] Asking for capabilities...")
  send_message(proc, serialize_message(initialize_message))

  # Read response from child
  response = proc.stdout.readline()
  print_response(response, prefix='[🤵 CLIENT <- 💻 SERVER]: \n')

  # 2. Send initialized notification
  print("[🤵 CLIENT 2] Sending initialized notification...")
  send_message(proc, serialize_message(initialized_message))

  # Read response from child
  response = proc.stdout.readline()
  print_response(response, prefix='[🤵 CLIENT <- 💻 SERVER]: \n')


def list_tools():
  # 3. send a message to list tools
  print("[🤵 CLIENT 3] Requesting list of tools...")
  # send a JSON-RPC message
  send_message(proc, serialize_message(list_tools_message))
  # Lee la respuesta del servidor desde su salida estándar (stdout)
  response = proc.stdout.readline()
  print_response(response, prefix='[🤵 CLIENT <- 💻 SERVER]: \n')
  # Parsea la respuesta JSON y extrae la propiedad ["result"]["tools"]
  return json.loads(response)["result"]["tools"]


def call_tool(tool_name, args):
  # 4. call a tool
  # send a JSON-RPC message
  tool_message = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": tool_name,
      "args": args
    },
    "id": 1
  }
  send_message(proc, serialize_message(tool_message))
  response = proc.stdout.readline()
  return json.loads(response)["result"]["properties"]["content"]["items"]


def close_server():
  print("[🤵 CLIENT 4] Closing server...")
  send_message(proc, 'exit\n')

  exit_code = proc.wait()
  print(f"[🤵 CLIENT 4] Child exited with code {exit_code}")


tools = []


def main():
  connect()
  tool_response = list_tools()
  tools.extend(tool_response)
  print(f"🧰 Tools available: {tools}")

  tool = tools[0]

  tool_call_response = call_tool(tool["name"], {"args1": "hello world!"})
  for content in tool_call_response:
    print_response(content['text'], prefix='[🤵 CLIENT <- 💻 SERVER] tool response: \n')

  close_server()


if __name__ == "__main__":
  main()
