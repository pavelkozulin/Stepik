def count_repetitions(sequence):
    j, result = 1, []
    if len(sequence) == 1:
        result.append(str(sequence) + '1')
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            j += 1
        else:
            result.append(str(sequence[i - 1] + str(j)))
            j = 1
        if i == len(sequence)-1:
            result.append(str(sequence[i] + str(j)))
    result = ''.join(result)
    print(result)
    return result
    
count_repetitions('a')
count_repetitions('aa')
count_repetitions('aab')
count_repetitions('aabb')
count_repetitions('abb')
