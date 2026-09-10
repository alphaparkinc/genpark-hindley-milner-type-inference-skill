from client import HMInference, HMType

def main():
    print("=== Testing Hindley-Milner Type Inference ===")
    hm = HMInference()
    t1 = HMType("Int")
    v = hm.fresh_var()
    subst = {}
    hm.unify(v, t1, subst)
    res = hm.apply_subst(v, subst)
    print("Inferred type:", res)

    assert res.name == "Int"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
