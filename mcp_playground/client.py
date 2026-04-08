import json
import subprocess
import sys

from mcp_playground.utils.messages import (
  initialized_message,
  initialize_message,
  list_tools_message,
)

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
  print("🏁🏁🏁  Connecting to the server...  🏁🏁🏁")
  # 1. Ask for capabilities
  print("[🤵 CLIENT 1] Asking for capabilities...")
  send_message(proc, serialize_message(initialize_message))
  # print("[🤵 CLIENT 1] Asking for capabilities... Done.")

  # Read response from child
  response = proc.stdout.readline()
  print_response(response, prefix='[🤵 CLIENT <- 💻 SERVER]: \n')

  # 2. Send initialized notification
  print("[🤵 CLIENT 2] Sending initialized notification...")
  send_message(proc, serialize_message(initialized_message))
  # print("[🤵 CLIENT 2] Sending initialized notification... Done.")


def list_tools():
  # 3. send a message to list tools
  # send a JSON-RPC message
  print("[🤵 CLIENT 3] Requesting list of tools...")
  send_message(proc, serialize_message(list_tools_message))
  # print("[🤵 CLIENT 3] Requesting list of tools... Done.")

  response = proc.stdout.readline()
  print_response(response, prefix='[🤵 CLIENT <- 💻 SERVER]: \n')


def close_server():
  print("[🤵 CLIENT 4] Closing server...")
  send_message(proc, 'exit\n')
  # print("[🤵 CLIENT 4] Closing server... Done.")

  exit_code = proc.wait()
  print(f"[🤵 CLIENT 4] Child exited with code {exit_code}")


def main():
  connect()
  list_tools()
  close_server()


if __name__ == "__main__":
  main()
