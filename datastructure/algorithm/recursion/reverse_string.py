import parent

from timer import performance

@performance
def reversse_string(string):
    # i am using for loop instead of python buildin list reverse so it shows the iterative approach
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    
    return reversed_string

def reverse_recursion(string):
    if len(string) <= 1:
        return string
    else:
        return reverse_recursion(string[1:]) + string[0]

# reverse_recursion = performance(reverse_recursion)
performance(reverse_recursion)('hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay')
reversse_string('hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay hi how are you i am fine what about you are you okay')