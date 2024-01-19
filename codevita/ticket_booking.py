def find_vacancies(input_str):
    return input_str.count('_')


def allocate(row_no, group_no, output, group_count):
    n = len(output[row_no])
    i = 0
    group_count_temp = group_count
    while group_count_temp > 0 and i < n:
        if output[row_no][i] == '_':
            output[row_no] = output[row_no][:i] + \
                str(group_no) + output[row_no][i+1:]
            group_count_temp -= 1
        i += 1


def allocate_spaces(vacancies, group_count, output, prices):
    n = len(group_count)
    mid = n // 2
    v_size = len(vacancies)
    unused_ele = []

    # allocate the below ones first
    for i in range(mid, n):
        unused = True
        for j in range(v_size):
            if vacancies[j] >= group_count[i]:
                unused = False
                if prices[j] != -1:
                    global sum_used
                    sum_used += (prices[j] * group_count[i])
                allocate(j, i - mid + 1, output, group_count[i])
                vacancies[j] -= group_count[i]
                break
        if unused:
            unused_ele.append(i - mid + 1)

    # allocate the above ones second
    for i in range(mid):
        unused = True
        for j in range(v_size):
            if vacancies[j] >= group_count[i]:
                unused = False
                if prices[j] != -1:
                    sum_used += (prices[j] * group_count[i])
                allocate(j, i + (n - mid) + 1, output, group_count[i])
                vacancies[j] -= group_count[i]
                break
        if unused:
            unused_ele.append(i + (n - mid) + 1)
    return unused_ele


def tokenise_group(input_str):
    return list(map(int, input_str.split(',')))


def tokenise_price(input_str, group_count):
    tokens = []
    j = 0
    for token in input_str.split():
        if token != "?":
            j += 1
            tokens.append(int(token))
        else:
            global question_row
            question_row = j
            tokens.append(-1)
    return tokens


def main():
    global sum_used, question_row
    question_row = 0
    sum_used = 0

    rows = int(input())
    seating = []
    vacancies = []
    for i in range(rows):
        row_input = input()
        seating.append(row_input)
        vacancy = find_vacancies(row_input)
        vacancies.append(vacancy)
    copy_vacancy = vacancies

    groups_input = input()
    group_count = tokenise_group(groups_input)

    price_input = input()
    price_val = tokenise_price(price_input, group_count)

    total_collection = int(input())

    group_n = len(group_count)
    assigned = [0] * group_n
    output = seating.copy()
    unused = allocate_spaces(vacancies, group_count, output, price_val)
    print(*output, sep="\n")

    total_vacancy = sum(vacancies)
    print(total_vacancy, *unused)

    used_people = copy_vacancy[question_row] - vacancies[question_row]
    final_num = total_collection - sum_used
    print(final_num // used_people)


if __name__ == "__main__":
    main()
