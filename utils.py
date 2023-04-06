
def contains_number(s: str) -> bool:
    if False in [c.isdigit() for c in s]:
        return False
    return True
