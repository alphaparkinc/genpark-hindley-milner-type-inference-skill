import sys
import json
from client import HMInference, HMType

def main():
    hm = HMInference()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "unify":
            t1 = HMType(params.get("t1"))
            t2 = HMType(params.get("t2"))
            subst = {}
            hm.unify(t1, t2, subst)
            res = {"subst": {k: str(v) for k, v in subst.items()}}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
