def naive_search(text, pattern):

    positions = []

    for i in range(len(text) - len(pattern) + 1):

        if text[i:i+len(pattern)] == pattern:
            positions.append(i)

    return positions