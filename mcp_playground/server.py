import json
import sys


def send_response(response):
  print(json.dumps(response))
  sys.stdout.flush()


def main():
  for line in sys.stdin:
    message = line.strip()
    if message == "hello":
      send_response("hello there")
    elif message.startswith('{"jsonrpc":'):
      # parse it as JSON message
      json_message = json.loads(message)

      match json_message['method']:
        case "tools/list":
          response = {
            "jsonrpc": "2.0",
            "id": json_message["id"],
            "result": ["tool1", "tool2"]
          }
          send_response(response)
          break
        case _:
          send_response(f"Unknown method: {json_message['method']}")
          break
    elif message == "exit":
      send_response(f"Exiting server.")
      sys.exit(0)
    else:
      send_response(f"Unknown message: {message}")


if __name__ == "__main__":
  main()
