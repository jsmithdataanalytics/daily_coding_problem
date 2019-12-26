
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
]

vocab = ['a', 'i', 'deer', 'deal', 'dog', 'daily', 'coding', 'problem']


def initialise_tree(layers):
    tree = dict.fromkeys(letters)
    layers -= 1

    for letter in tree:
        tree[letter] = initialise_tree(layers) if layers else []

    return tree


index = initialise_tree(layers=2)

for i, word in enumerate(vocab):
    word = word.strip().ljust(2)
    index[word[0]][word[1]].append(i)


def query(string):
    string = string.strip()

    if len(string) == 1:
        entries = [entry for entries in index[string[0]].values() for entry in entries]

    else:
        entries = [entry for entry in index[string[0]][string[1]] if vocab[entry][:len(string)] == string]

    return [vocab[entry] for entry in entries]


if __name__ == '__main__':
    assert query('de') == ['deer', 'deal']
    assert query('d') == ['daily', 'deer', 'deal', 'dog']
    assert query('a') == ['a']
    assert query('codi') == ['coding']
