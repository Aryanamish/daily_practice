
for count in range(int(input(""))):
    no_of_problem_sets, no_of_students = list(map(int, input("").split(' ')))
    problems = []
    for _ in range(no_of_problem_sets):
        temp = list(map(int, input("").split(' ')))
        problems += [i for i in range(temp[0], temp[1]+1)]

    students = list(map(int, input("").split(' ')))
    # print(students, problems)
    problems.sort()
    solution = []
    for student in students:
        total_problems = len(problems)
        half_problems_index = int(total_problems/2)
        solution_found = False
        if student in problems:
            solution.append(student)
            problems.remove(student)
            solution_found = True
        elif student > problems[half_problems_index]:
            p_range = range(half_problems_index, total_problems)
            for i in p_range:
                less_difficult = False
                if student > problems[i]:
                    continue
                elif student == problems[i]:
                    solution.append(problems[i])
                    del problems[i]
                    solution_found = True
                    break
                elif student < problems[i]:
                    solution.append(problems[i])
                    del problems[i]
                    solution_found = True
                    break
        else:
            p_range = range(0, half_problems_index+1)
            for i in p_range:
                less_difficult = False
                if student < problems[i]:
                    continue
                elif student == problems[i]:
                    solution.append(problems[i])
                    del problems[i]
                    solution_found = True
                    break
                elif student > problems[i]:
                    solution.append(problems[i])
                    del problems[i]
                    solution_found = True
                    break
        if solution_found is False:
            solution.append(problems[half_problems_index])
            del problems[half_problems_index]
    print(f"Case #{count+1}:", *solution)
