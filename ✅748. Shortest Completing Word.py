def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    variants = []
    letters = [i.lower() for i in licensePlate if i.isalpha()]
    for word in words:
        letters_word = list(word)
        print(f"letters {letters}, letters_word {letters_word}")
        for item in letters:
            if letters.count(item) <= letters_word.count(item):
                continue
            else:
                break
        else:
            variants.append(word)
    return variants


licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
print(shortestCompletingWord(licensePlate, words))
