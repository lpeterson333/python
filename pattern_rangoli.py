import itertools
n  = 5
letter = n - 1 # adjust input for 0 letter indexing input is n = 3, but use input value for widths and heights
lowercase_str = "abcdefghijklmnopqrstuvwxyz"
letter_list = list(lowercase_str)
completed_lists = []
output_list = []
output = []
max_width = n + n-1 + n + n - 2

for i in range(n):
    output_list.append(letter_list[i])

output.append(output_list) 
while any(output_list):
    output_list = output_list[1:] 
    if any(output_list):
        output.append(output_list)  
for elem in output:
    reverse_list = sorted(elem, reverse = True)
    mirrored_list = [*reverse_list[:-1],*elem]
    completed_lists.append(mirrored_list)

sorted_completed_lists = sorted(completed_lists[1:], key = len)
for elem in sorted_completed_lists:
    dashed_elem = "-".join(elem)
    number_of_dashes = ((max_width - len(dashed_elem))//2)
    first_half_list = ["-"] * number_of_dashes
    final_output = [*first_half_list, *dashed_elem, *first_half_list]
    print("".join(final_output))
for elem in completed_lists:
    dashed_elem = "-".join(elem)
    number_of_dashes = ((max_width - len(dashed_elem))//2)
    first_half_list = ["-"] * number_of_dashes
    final_output = [*first_half_list, *dashed_elem, *first_half_list]
    print("".join(final_output))









    












