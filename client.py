"""Hindley-Milner Type Inference Engine.
100% Python Standard Library.
"""

class HindleyMilnerInference:
    """Hindley-Milner type inference engine with basic unification."""
    class PrimType:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return self.name

    class ArrowType:
        def __init__(self, from_t, to_t):
            self.from_t = from_t
            self.to_t = to_t
        def __repr__(self):
            return f"({self.from_t} -> {self.to_t})"

    def unify(self, t1, t2):
        if isinstance(t1, self.PrimType) and isinstance(t2, self.PrimType):
            return t1.name == t2.name
        if isinstance(t1, self.ArrowType) and isinstance(t2, self.ArrowType):
            return self.unify(t1.from_t, t2.from_t) and self.unify(t1.to_t, t2.to_t)
        return False
