if __name__ == '__main__':
    sentence = list(input().split())
    sentence.reverse()
    string = " ".join(sentence)
    string.swapcase()
    print(string)