import json
import sys

from mcp_playground.utils.messages import initializeResponse


def send_response(response):
  print(json.dumps(response))
  sys.stdout.flush()


def example_tool(args):
  arg1 = args.get("arg1", args.get("args1"))
  return f"example_tool received: {arg1}"


def main():
  initialized = False

  while True:
    for line in sys.stdin:
      message = line.strip()
      if message == "hello":
        print("hello there")
        sys.stdout.flush()  # Ensure output is sent immediately
      elif message.startswith('{"jsonrpc":'):
        json_message = json.loads(message)
        method = json_message.get('method', '')

        if not initialized:
          if method != "initialize" and method != "notifications/initialized":
            print(
              f"Server not initialized. Please send an 'initialized' notification first. You sent {method}"
            )
            sys.stdout.flush()
            continue

        match method:
          case "notifications/initialized":
            # print("Server initialized successfully.")
            send_response("Server initialized successfully.")
            initialized = True
            break
          case "initialize":
            send_response(initializeResponse)
            # initialized = True
            break
            # should return capabilities
          case "tools/list":
            response = {
              "jsonrpc": "2.0",
              "id": json_message["id"],
              "result": {
                "tools": [{
                  "name": "example_tool",
                  "description": "An example tool that does something.",
                  "inputSchema": {
                    "type": "object",
                    "properties": {
                      "arg1": {
                        "type": "string",
                        "description": "An example argument."
                      }
                    },
                    "required": ["arg1"]
                  }
                }]
              }
            }
            send_response(response)
            break
          case "tools/call":
            tool_name = json_message['params']['name']
            args = json_message['params']['args']
            # todo create a response for the tool call, i.e call the right tool
            response = {
              "jsonrpc": "2.0",
              "id": json_message["id"],
              "result": {
                "properties": {
                  "content": {
                    "description":
                    "description of the content",
                    "items": [{
                      "type": "text",
                      "text": f"Called tool {tool_name} with arguments {args}"
                    }]
                  }
                }
              }
            }
            send_response(response)
            break
          case _:
            send_response(f"Unknown method: {json_message['method']}")
            break
      elif message == "exit":
        send_response("Exiting server.")
        sys.exit(0)
      else:
        print(f"Unknown message: {message}")


if __name__ == "__main__":
  main()
