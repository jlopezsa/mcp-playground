import json
import subprocess
import sys


def send_message(proc, message):
  """Send a message to the child process."""
  print(f"[CLIENT] Sending message to server Message: {message.strip()}")
  proc.stdin.write(message)
  proc.stdin.flush()


def serialize_message(message):
  """Serialize a message to JSON format."""
  return json.dumps(message) + "\n"


def main():
  proc = subprocess.Popen(
    [sys.executable, "-m", "mcp_playground.server"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
  )

  list_tools_message = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
  }
  message = "hello\n"

  send_message(proc, message)

  response = proc.stdout.readline()
  print(f"[SERVER]: {response.strip()}")

  send_message(proc, serialize_message(list_tools_message))

  response = proc.stdout.readline()
  print(f"[SERVER]: {response.strip()}")

  send_message(proc, "exit\n")

  proc.stdin.close()
  exit_code = proc.wait()
  print(f"Child process exited with code {exit_code}")


if __name__ == "__main__":
  main()
