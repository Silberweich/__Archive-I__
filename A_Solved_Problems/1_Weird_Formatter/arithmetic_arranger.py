def arithmetic_arranger(problems, show_ans = False):
    # some variables
    first_line_num = list()
    second_line_sig = list()
    second_line_num = list()
    answer_line_num = list()
    length_line_max = list()
    arranged_problems = ""

    # Some conditions
    if len(problems) > 5:
        return "Error: Too many problems."

    # each string split() the second index will always be sign
    for problem in problems:
        fir, sig, sec = problem.split()
        first_line_num.append(fir) 
        second_line_sig.append(sig)
        second_line_num.append(sec)

    # calculate problem
    try:
        for n in range(0, len(problems)):
            answer = int()
            if(second_line_sig[n] == "+"):
                answer =  int(first_line_num[n]) + int(second_line_num[n])
            elif(second_line_sig[n] == "-"):
                answer =  int(first_line_num[n]) - int(second_line_num[n])
            else:
                return "Error: Operator must be '+' or '-'."

            answer_line_num.append(answer)

    except: return "Error: Numbers must only contain digits."
    
    
    # Checker here
    # if not something something return error
    # formatting maybe
    #----------------------------------------------------------#
    # find max length of each line
    for n in range(0, len(problems)):
        this_line_max = len(first_line_num[n])
        if len(second_line_num[n]) > len(first_line_num[n]):
            this_line_max = len(second_line_num[n])
            if this_line_max > 4:
                return "Error: Numbers cannot be more than four digits."
        length_line_max.append(int(this_line_max) + 2)

        
    # First line block by block
    for tBloc in range(0, len(problems)):
        arranged_problems += first_line_num[tBloc].rjust(length_line_max[tBloc], " ")
        if tBloc < len(problems) - 1:
            arranged_problems += "    "

    arranged_problems += "\n"

    # Second line block by block
    for bBloc in range(0, len(problems)):
        arranged_problems += second_line_sig[bBloc]
        arranged_problems += second_line_num[bBloc].rjust(length_line_max[bBloc] -1, " ")
        if bBloc < len(problems) - 1:
            arranged_problems += "    "

    arranged_problems += "\n"

    # Bar line block by block
    for line in range(0, len(problems)):
        liner = "-" * length_line_max[line]
        arranged_problems += liner
        if line < len(problems) - 1:
            arranged_problems += "    "

    # if need calculation
    if show_ans:
        arranged_problems += "\n"
        for aBloc in range(0, len(problems)):
            arranged_problems += str(answer_line_num[aBloc]).rjust(length_line_max[aBloc], " ")
            if aBloc < len(problems) - 1:
                arranged_problems += "    "
    print(arranged_problems)
    return arranged_problems
