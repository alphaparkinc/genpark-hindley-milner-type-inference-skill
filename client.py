class HMType:
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or []

    def __repr__(self):
        if not self.args:
            return self.name
        return f"({self.name} {' '.join(str(a) for a in self.args)})"

class HMInference:
    """
    Hindley-Milner Type Inference Engine with first-order unification.
    """
    def __init__(self):
        self.var_count = 0

    def fresh_var(self):
        self.var_count += 1
        return HMType(f"a{self.var_count}")

    def unify(self, t1, t2, subst):
        t1 = self.apply_subst(t1, subst)
        t2 = self.apply_subst(t2, subst)
        if t1.name == t2.name and len(t1.args) == len(t2.args):
            for a1, a2 in zip(t1.args, t2.args):
                self.unify(a1, a2, subst)
            return
        if t1.name.startswith("a") and not t1.args:
            subst[t1.name] = t2
            return
        if t2.name.startswith("a") and not t2.args:
            subst[t2.name] = t1
            return
        raise TypeError(f"Cannot unify {t1} with {t2}")

    def apply_subst(self, t, subst):
        if t.name in subst:
            return self.apply_subst(subst[t.name], subst)
        return HMType(t.name, [self.apply_subst(a, subst) for a in t.args])
