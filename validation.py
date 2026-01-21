from warnings import warn
class ValidationError(Exception):
    pass
class Validator:
    error = ValidationError
    def __init__(self, *, strict=False):
        self.strict = strict
    def fail(self, msg):
        if self.strict:
            raise self.error(msg)
        warn(msg, RuntimeWarning)
    def validate(self, value):
        return value  # override
class Require(Validator):
    def __init__(self, condition, *, strict=False):
        super().__init__(strict=strict)
        self.condition = condition
    def validate(self, value=None):
        if not self.condition:
            self.fail("requirement failed")
        return value
class TypeCheck(Validator):
    def __init__(self, *types, strict=False):
        super().__init__(strict=strict)
        self.types = types
    def validate(self, value):
        if not isinstance(value, self.types):
            names = ", ".join(t.__name__ for t in self.types)
            self.fail(f"expected {names}, got {type(value).__name__}")
        return value
class NonEmpty(Validator):
    def validate(self, value):
        try:
            if len(value) == 0:
                self.fail("value must be non-empty")
        except Exception:
            self.fail("value has no length")
        return value
class InRange(Validator):
    def __init__(self, min=None, max=None, *, strict=False):
        super().__init__(strict=strict)
        self.min = min
        self.max = max
    def validate(self, value):
        if self.min is not None and value < self.min:
            self.fail(f"value {value} < {self.min}")
        if self.max is not None and value > self.max:
            self.fail(f"value {value} > {self.max}")
        return value