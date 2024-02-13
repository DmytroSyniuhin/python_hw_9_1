def popular_words(text, words):
    num_ = []
    my_dict = {}

    text_low = text.lower().split()

    for i in range(len(words)):
        num_.append(text_low.count(words[i]))

    for i in range(len(words)):
        my_dict.update({words[i]: num_[i]})

    return my_dict


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
