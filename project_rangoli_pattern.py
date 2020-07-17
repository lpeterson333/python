def createMainPattern(a, b):
    """User selects two design elements. This function returns a string of length 6 in the pattern aabaab"""
    return f"{a}{a}{b}{a}{a}{b}"

def createPattern(repeating_unit, edge_pattern, rows, max_width):
    """Create diamond pattern with user choices of design elements."""
    # rows = 11
    text = "WELCOME"
    # repeating_unit = user_design
    # max_width = 33
    repeating_segments = []
    sub_unit = repeating_unit[0] + repeating_unit[-1]
    for n in range(rows//2):
        elem = [repeating_unit]*n
        elem.append(repeating_unit[0])
        elem.insert(0,sub_unit)
        repeating_segments.append("".join(elem))


    reverse_segments = sorted(repeating_segments[:-1], reverse = True, key = len)
 


    output= []
    for elem in repeating_segments:
        number_of_dashes = ((max_width - len(elem))//2)
        first_half_list = [edge_pattern] * number_of_dashes
        final_output = [*first_half_list, *elem, *first_half_list]
        output.append("".join(final_output))

    number_of_dashes = ((max_width - len(text))//2)
    first_half_list = [edge_pattern] * number_of_dashes
    final_output = [*first_half_list, text, *first_half_list]
    output.append("".join(final_output))
    for elem in output:
        print(elem)
    output.reverse()
    for elem in output[1:]:
        print(elem)

    print("Nice Pattern:) So Pretty!  Can I make one?")



  



createPattern(createMainPattern("#","%"), "+", 9, 33) #large pattern

