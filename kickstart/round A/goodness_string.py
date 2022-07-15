# Si != SN-i+1


def main():

    for count in range(int(input(""))):
        N, K = list(map(int, input("").split(' ')))
        s = input("")
        goodness_score = 0
        correction = 0
        for i in range(int(N/2)):
            if s[i] != s[N-(i+1)]:
                goodness_score += 1
        if goodness_score < K:
            result = K - goodness_score 
        elif goodness_score > K:
            result = goodness_score - K
        elif goodness_score == K:
            result = 0
        print(f"Case #{count+1}: {result}")

if __name__ == '__main__':
    main()
