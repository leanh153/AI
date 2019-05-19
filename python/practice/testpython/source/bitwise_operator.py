a = 5  # 101
b = 4  # 100


def print_dec_and_bit(value):
    print("Dec: {:d} | Bit: {:3d}".format(value, value))


c = a & b  # => Bits 101 and 100

print("User rights ===============")

view = 1  # 001
edit = 2  # 010
credit = 4  # 100


print_dec_and_bit(credit | edit)
