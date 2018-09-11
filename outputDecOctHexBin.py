def format_output(raw_mat):
    temp = list(raw_mat)
    result = ""
    for i in range(2,len(raw_mat)):
        if (i<10):
            result += str(raw_mat[i]).upper()
    return result


def print_formatted(number):
    for i in range(1,(number+1)):
        pad= 5
        print(str(i) +format_output(oct(i)).ljust(pad)
              +format_output(hex(i)).ljust(pad) +format_output(bin(i)).ljust(pad))


n = int(input())
print_formatted(n)