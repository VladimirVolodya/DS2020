def countSplittings(number, max_number_of_terms, max_term):
    table = [[[0 for i in range(max_term + 1)] for j in range(max_number_of_terms + 1)] for l in range(number + 1)]
    sum = 0
    for n in range(number + 1):
        for m in range(max_number_of_terms + 1):
            for k in range(max_term + 1):
                if 0 < m <= n and 0 < k <= n:
                    table[n][m][k] = table[n][m][k - 1] + table[n - k][m - 1][k]
                elif k > n:
                    table[n][m][k] = table[n][m][n]
                elif n == 0 and m == 0:
                    table[n][m][k] = 1
                else:
                    table[n][m][k] = 0
    for num in range(1, number + 1):
        for num_of_terms in range(max_number_of_terms + 1):
            sum += table[num][num_of_terms][max_term]
    return sum


print(countSplittings(54, 8, 7))
