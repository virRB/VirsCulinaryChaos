good_words = ['pineapple', 'asparagus', 'truffle', 'rasberry', 'zatar', 'crab', 'culinarification', 'cinnamond', 'caramel']

bad_words = ['toxic', 'sludge', 'uraniam', 'radioactive', 'velvet']

score = 0

def test(word):
    global score
    word = word.lower()
    length = len(word)
    base = length * 0.07
    score = base
    for gw in good_words:
        if gw in word:
            score += 1
    for bw in bad_words:
        if bw in word:
            score -= 0.5
    if score < 0:
        score = 0
    elif score > 5:
        score = 5
    score = round(score)
    v = score
    score = 0
    return v