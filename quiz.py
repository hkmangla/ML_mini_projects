"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    l = s.split();
    occurrenceList = {}
    for i in l:
        if i in occurrenceList.keys():
            occurrenceList[i] += 1
        else:
            occurrenceList[i] = 1
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top_n = occurrenceList.items()
    top_n.sort(key=lambda score: (-score[1],score[0]))
    # top_n.sort()    
    # print top_n[:n]
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
