def love(subject: str) -> str:
    return f"I love you {subject}!"

#print(love("klyer"))

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note = ""
    count: int = 0

    while count < n:
        love_note += love(to) + "\n" 
        count += 1
    return love_note

#print(spread_love("ally", 4))