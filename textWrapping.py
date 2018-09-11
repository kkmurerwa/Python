import textwrap

def wrap(string, max_width):
    wrapreturn = ""
    wrapped = textwrap.wrap(string,max_width)
    for i in wrapped:
        wrapreturn += i+"\n"
    return wrapreturn

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)