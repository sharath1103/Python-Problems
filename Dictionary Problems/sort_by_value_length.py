words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}
new_words = dict(sorted(words.items(), key = lambda item: len(item[1])))
print(new_words)