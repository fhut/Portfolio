def arithmetic_arranger(problems, solve=False):


    # LIMITS
    MAX_DIGIT_LENGTH = 4
    MAX_PROBLEM_LIMIT = 5
    ADDITION = "+"
    SUBTRACTION = "-"

    # FORMATTING
    R_PADDING = "    "
    L_PADDING = 2

    problems_split = []
    problems_arranged = []
    max_operation_length_list = []
    max_op_length = 0
    operation_length = 0

    # Split problems into 2d list
    for problem in problems:
        problems_split.append(problem.split())

    # Set operand length
    for operation in problems_split:
        for operand in operation:
            if len(operand) > max_op_length:
                max_op_length = len(operand)

    # Set prob len
    for prob in problems_split:
        if len(prob) > operation_length:
            operation_length = len(prob)

    # Set max length of each operation
    for o in problems_split:
        max_o_l = 0
        for p in o:
            if len(p) > max_o_l:
                max_o_l = len(p)
        max_operation_length_list.append(max_o_l)

    # num of problems passed
    num_problems = len(problems)

    # Function conditions
    # Max number of problems to pass as argument
    if num_problems > MAX_PROBLEM_LIMIT:
        return "Error: Too many problems."


    # Max operand length
    elif max_op_length > MAX_DIGIT_LENGTH:
        return "Error: Numbers cannot be more than four digits."

    for problem in problems_split:
        for each in prob:
            if len(each) > 4:
                return "Error: Numbers cannot be more than four digits."

    # Indicate division or subtraction only
    for prob in problems_split:
        if prob[1] == ADDITION or prob[1] == SUBTRACTION:
            continue
        else:
            return "Error: Operator must be '+' or '-'."

    #Check is digit
    for problem in problems_split:
        for prob in problem:
            for char in prob:
                try:
                    if char == ADDITION or char == SUBTRACTION:
                        continue
                    int(char) % 1
                except:
                    return "Error: Numbers must only contain digits."

    # Arrange problems in order of sequential operands
    for p in range(operation_length):
        for i in range(num_problems):
            problems_arranged.append(problems_split[i][p])

    # formatted list
    formatted_problems = []

    #calculations
    sums = []

    # top operand lists
    top_operand = list(problems_arranged[:num_problems])

    # operator lists
    operators = list(problems_arranged[num_problems:num_problems * -1])

    # bottom operand lists
    bottom_operands = list(problems_arranged[num_problems * -1:])

    # Calcs
    for problem in problems:
        sums.append(eval(problem))

    # append top operand formatting
    index = 0
    padding = 0
    for op in top_operand:
        if len(op) == max_operation_length_list[index]:
            formatted_problems.append(" " * L_PADDING + op)
        else:
            formatted_problems.append(" " * (len(bottom_operands[index]) - len(top_operand[index]) + len(
                operators[index]) + 1) + op)
        if padding < num_problems - 1:
            formatted_problems.append(R_PADDING)
        index += 1
        padding += 1
    formatted_problems.append("\n")

    # append operator and bottom operand combined
    padding = 0
    for index in range(num_problems):
        if len(bottom_operands[index]) == max_operation_length_list[index]:
            formatted_problems.append(operators[index] + " " + bottom_operands[index])
        elif len(top_operand[index]) == max_operation_length_list[index]:
            formatted_problems.append(operators[index] + " " * (len(top_operand[index]) - len(bottom_operands[index]) + 1) + bottom_operands[index])
        if padding < num_problems - 1:
            formatted_problems.append(R_PADDING)
        padding += 1
    formatted_problems.append("\n")

    # append lines to formatted_problems
    index = 0
    padding = 0
    for each in range(num_problems):
        formatted_problems.append("-" * (max_operation_length_list[index] + L_PADDING))
        if padding < num_problems - 1:
            formatted_problems.append(R_PADDING)

        padding += 1
        index += 1



    #return func
    if solve is True:
        formatted_problems.append("\n")
        # append sums to formatted_problems
        padding = 0
        for index in range(num_problems):
            formatted_problems.append(
                " " * (max_operation_length_list[index] + L_PADDING - len(str(sums[index]))) + str(sums[index]))
            if padding < num_problems - 1:
                formatted_problems.append(R_PADDING)
            padding += 1
        return "".join(formatted_problems)
    else:
        return "".join(formatted_problems)

print(arithmetic_arranger(["455 - 657"], solve=True))