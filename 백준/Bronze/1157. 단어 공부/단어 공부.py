random_str = input()
chr_dict = {}

for i in range(0, len(random_str)):
    num = ord(random_str[i])
    if num > 90:
        num = num - 32
    if (num in chr_dict):
        chr_dict[num] = chr_dict[num] + 1
    else:
        chr_dict[num] = 1

chr_max = 0
max_ord = []

for key, value in chr_dict.items():
    if (value > chr_max):
        chr_max = value
        max_ord = []
        max_ord.append(key)
    elif (value == chr_max):
        chr_max = value
        max_ord.append(key)

if (len(max_ord) > 1):
    print("?")
else:
    print(chr(max_ord[0]))