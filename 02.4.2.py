def count_repetitions(sequence):
    """
    >>> count_repetitions([1, 1, 1, 2, 2, 3, 1, 1, 1, 1])
    [3, 2, 1, 4]
    """
    if len(sequence) == 1:
        res = (str(sequence[0]) + '1')
        print(res)
    Count_List = []
    Symbol_List = []
    for i in range(1, len(sequence)):
        cnt = 0
        if sequence[i - 1] != sequence[i]:
            cnt = i - sum(Count_List)
            Count_List.append(cnt)
            Symbol_List.append(sequence[i - 1])
        if i == len(sequence) - 1:
            cnt = i - sum(Count_List) + 1
            Count_List.append(cnt)
            Symbol_List.append(sequence[-1])
    #print(Count_List)
    Count_List = [str(item) for item in Count_List]
    #print(Symbol_List)
    zipped = list(zip(Symbol_List, Count_List))
    #print(zipped)
    res = ''.join([''.join(sub) for sub in zipped])
    #print(res)
    print(res)
    return res

count_repetitions('a')
count_repetitions('aaa')
count_repetitions('aaab')
count_repetitions('aaabbb')
count_repetitions('abbb')
count_repetitions('aaaaaabbbddddcccggrthhh')
