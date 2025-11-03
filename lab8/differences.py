def most_similar(a):
    score_dict = {}
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            score_dict[(a[i],a[j])] = count_differences(a[i], a[j])
    return min(score_dict, key = score_dict.get)

def count_differences(s1, s2):
    return sum(s1[i] != s2[i] for i in range(len(s1)))

print(most_similar(['abc', 'xac', 'axc']))
print(most_similar(['abc', 'def', 'ghi']))