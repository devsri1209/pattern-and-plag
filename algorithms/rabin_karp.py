def rabin_karp_search(text, pattern):

    positions = []

    m = len(pattern)
    n = len(text)

    pattern_hash = hash(pattern)

    for i in range(n - m + 1):

        window = text[i:i+m]

        if hash(window) == pattern_hash:

            if window == pattern:
                positions.append(i)

    return positions