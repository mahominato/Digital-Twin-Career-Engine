import subprocess
import json
import time

def call_mcp():
    print("Starting MCP server...")
    env = {"NOTEBOOKLM_URL": "https://notebooklm.google.com/notebook/6ab9840f-8fb7-4fac-8477-b756e6886c27"}
    import os
    merged_env = os.environ.copy()
    merged_env.update(env)
    
    proc = subprocess.Popen(
        ["npx.cmd", "-y", "notebooklm-mcp-server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=merged_env,
        text=True,
        bufsize=1
    )
    
    # Let's write a simple initialize request (newline delimited)
    init_req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    print("Sending init...")
    proc.stdin.write(json.dumps(init_req) + "\n")
    proc.stdin.flush()
    
    print("Reading response...")
    out = proc.stdout.readline()
    if not out:
        err = proc.stderr.read()
        print("Process died! Stderr:", err)
        return
    print("Response:", out)
    
    # send initialized notification
    init_notif = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    proc.stdin.write(json.dumps(init_notif) + "\n")
    proc.stdin.flush()
    
    # call notebook_list
    list_req = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "notebook_list",
            "arguments": {}
        }
    }
    proc.stdin.write(json.dumps(list_req) + "\n")
    proc.stdin.flush()
    
    out = proc.stdout.readline()
    if out:
        data = json.loads(out)
        result = data.get("result", {})
        content = result.get("content", [])
        if content:
            print("Notebooks:", content[0].get("text"))
        else:
            print("No notebooks found or error:", result)
    else:
        print("No response from notebook_list")
    
    proc.kill()
    return


if __name__ == "__main__":
    call_mcp()
