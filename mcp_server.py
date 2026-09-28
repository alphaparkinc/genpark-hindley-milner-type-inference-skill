import sys
import json
from client import HindleyMilnerInference

hm = HindleyMilnerInference()

def parse_type(spec):
    if isinstance(spec, str):
        return hm.PrimType(spec)
    elif isinstance(spec, dict) and spec.get("type") == "arrow":
        return hm.ArrowType(parse_type(spec["from"]), parse_type(spec["to"]))
    return hm.PrimType("Unknown")

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "unify_types",
                        "description": "Unify two types under Hindley-Milner type system rules",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "type1": {"type": ["string", "object"]},
                                "type2": {"type": ["string", "object"]}
                            },
                            "required": ["type1", "type2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "unify_types":
            t1 = parse_type(args["type1"])
            t2 = parse_type(args["type2"])
            ok = hm.unify(t1, t2)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"unified": ok, "type1": str(t1), "type2": str(t2)})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
