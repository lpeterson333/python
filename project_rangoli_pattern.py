rows, max_width = list(map(int,(input().split())))
text = "WELCOME"
repeating_unit = "..|..|"
repeating_segments = []
for n in range(rows//2):
    elem = [repeating_unit]*n
    elem.append(".")
    elem.insert(0,".|")
    repeating_segments.append("".join(elem))


reverse_segments = sorted(repeating_segments[:-1], reverse = True, key = len)
rows, max_width = list(map(int,(input().split())))
text = "WELCOME"
repeating_unit = "..|..|"
repeating_segments = []
for n in range(rows//2):
    elem = [repeating_unit]*n
    elem.append(".")
    elem.insert(0,".|")
    repeating_segments.append("".join(elem))


reverse_segments = sorted(repeating_segments[:-1], reverse = True, key = len)


output= []
for elem in repeating_segments:
    number_of_dashes = ((max_width - len(elem))//2)
    first_half_list = ["-"] * number_of_dashes
    final_output = [*first_half_list, *elem, *first_half_list]
    output.append("".join(final_output))

number_of_dashes = ((max_width - len(text))//2)
first_half_list = ["-"] * number_of_dashes
final_output = [*first_half_list, text, *first_half_list]
output.append("".join(final_output))
for elem in output:
    print(elem)
output.reverse()
for elem in output[1:]:
    print(elem)


output= []
for elem in repeating_segments:
    number_of_dashes = ((max_width - len(elem))//2)
    first_half_list = ["-"] * number_of_dashes
    final_output = [*first_half_list, *elem, *first_half_list]
    output.append("".join(final_output))

number_of_dashes = ((max_width - len(text))//2)
first_half_list = ["-"] * number_of_dashes
final_output = [*first_half_list, text, *first_half_list]
output.append("".join(final_output))
for elem in output:
    print(elem)
output.reverse()
for elem in output[1:]:
    print(elem)
