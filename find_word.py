def find_word(word: str = "atomic", letters: str = "chenzhongkui"):
    print('要查找所包含的字母%s' % word)

    rul_word = set(letters).intersection(word)

    print('-' * 30)
    print('是否查找到->%s' % bool(rul_word))
    print('要查找的字母有.%d.个' % len(rul_word))
    con = 0
    for i in rul_word:
        con += 1
        print('%s是第%d个被找到的字母' % (i, con))

    print('查找完成...')

    return rul_word


class Person:
    def __init__(self):
        self.name = 'luncheoning'


if __name__ == '__main__':
    find_word()
