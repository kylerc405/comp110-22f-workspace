# start from first index
# loop through each index of list
    # test if equal to needle
        # yes: return true
# return false

def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i+=1

    return False

print(contains("poo", ["pee", "fard", "shid"]))