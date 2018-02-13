# https://www.acmicpc.net/problem/1181

def print_words_in_order(words):
    prev = ""
    sw = sorted(words)
    sw2 = sorted(sw, key=len)
    for w in sw2:
        if w != prev:
            print(w)
        prev = w

if __name__ == "__main__":
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    print_words_in_order(words)
