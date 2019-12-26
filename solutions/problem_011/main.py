
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@'
]

vocab = ['a', 'i', 'deer', 'deal', 'dog', 'dogs', 'daily', 'coding', 'problem']


def add_word_to_tree(word, tree):

    if word:
        subtree = tree.setdefault(word[0], {})
        add_word_to_tree(word[1:], subtree)


def get_words_from_tree(tree):

    if not tree:
        return ['']

    words = []

    for letter in tree:
        subtree_words = get_words_from_tree(tree[letter])
        words.extend([letter + word for word in subtree_words])

    return words


index = {}

for entry in vocab:
    add_word_to_tree(entry.lower().strip() + '@', index)


def query(prefix):
    subtree, query_string = index, prefix

    while prefix:

        if prefix[0] in subtree:
            subtree = subtree[prefix[0]]
            prefix = prefix[1:]

        else:
            return set()

    return {query_string + word[:-1] for word in get_words_from_tree(subtree)}


if __name__ == '__main__':
    assert query('de') == {'deer', 'deal'}
    assert query('d') == {'daily', 'deer', 'deal', 'dog', 'dogs'}
    assert query('a') == {'a'}
    assert query('codi') == {'coding'}
