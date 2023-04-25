def next_num(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (num * 3) + 1
# end of next_num

def collatz2(num):
    result = [num]
    while result[-1] != 1:
        value = next_num(result[-1])
        result.append(value)

    return len(result)
# end of simple collatz

def collatz(num, tracker):
    size = 1
    next_value = next_num(num)
    if next_value in tracker:
        tracker[num] = size + tracker[next_value]
        return tracker[num]
    else:
        unseen = [num]
        while unseen[-1] != 1 and next_value not in tracker:
            unseen.append(next_value)
            next_value = next_num(unseen[-1])
        # end of while
        size = len(unseen)
        if unseen[-1] != 1:
             size += tracker[next_value]

        for value in unseen:
            if value not in tracker:
                tracker[value] = size
            else:
                break
            size -= 1
        return tracker[num]
# end of collatz

c_dict = {1:1}
current_answer = 0
max_length = 0
for value in range(1,1000000):
    current_length = collatz(value, c_dict)
    if current_length > max_length:
        current_answer = value
        max_length = current_length

print("Longest Sequence Generated By:", current_answer)
print("The length:", max_length)
