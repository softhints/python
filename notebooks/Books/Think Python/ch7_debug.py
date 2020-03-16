def pascal(n):
    row_map = {0: {n: 1}}

    for i in range(1, n):
        row_list = {}

        prev_row = row_map[i - 1]
        for k, v in row_map[i - 1].items():

            if k + 1 in row_list:
                row_list[k + 1] = row_list[k + 1]
            else:
                row_list[k + 1] = prev_row.get(k, 0) + prev_row.get(k + 2, 0)

            if k - 1 in row_list:
                row_list[k - 1] = row_list[k - 1]
            else:
                row_list[k - 1] = prev_row.get(k, 0) + prev_row.get(k - 2, 0)

        row_map[i] = row_list

    for k, v in row_map.items():
        print(f'k: {k}, v: {v}')

    for k, v in row_map.items():
        # print(f'k: {k}, v: {v}')
        count = 0
        for kk, vv in sorted(v.items()):
            count = count + 1
            if count == 1:
                print('   ' * kk + f'{vv:3}', end='')
            else:
                print('   ' + f'{vv:3}', end='')
        print()


def fibMemo(i):
    memo = {}
    if i in memo:
        return memo[i]
    if i <= 2:
        return 1
    else:
        f = fibMemo(i - 1) + fibMemo(i - 2)
        memo[i] = f
    # print("calc", i, memo)
    return f


x = fibMemo(4)
print(x)
pascal(x)
