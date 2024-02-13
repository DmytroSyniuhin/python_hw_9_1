def popular_words(text, words):
    numbers_ = []
    my_dict = {}

    for i in range(len(words)):
        quantity = text.lower().count(' ' + words[i] + ' ')
        if quantity > 0:
            numbers_.append(quantity)
        else:
            numbers_.append(0)

    for i in range(len(words)):
        my_dict.update({words[i]: numbers_[i]})

    return my_dict


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
