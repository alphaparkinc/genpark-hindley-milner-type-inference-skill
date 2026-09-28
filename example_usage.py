from client import HindleyMilnerInference

hm = HindleyMilnerInference()
int_t = hm.PrimType("Int")
bool_t = hm.PrimType("Bool")

f1 = hm.ArrowType(int_t, bool_t)
f2 = hm.ArrowType(int_t, bool_t)
f3 = hm.ArrowType(int_t, int_t)

print(f"Unify {f1} with {f2}:", hm.unify(f1, f2))
print(f"Unify {f1} with {f3}:", hm.unify(f1, f3))
