WORDLIST = pathlib.Path("wordlist.txt")

words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]
word = random.choice(words)
