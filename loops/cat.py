# print meow 3 times

# WHILE
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# #FOR
# # invés de i pode usar _ para representar uma variavel fds
# for _ in range(100):
#     print("meow")

# while True:
#     n = int(input("Fale um numero positivo: "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    n = get_number()
    meow(n)


def get_number():
    n = int(input("Say a number: "))
    return n


def meow(n):
    for _ in range (n):
        print("meow")


main()