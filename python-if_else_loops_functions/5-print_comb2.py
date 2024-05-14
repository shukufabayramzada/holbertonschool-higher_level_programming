#!/usr/bin/python3
for n in range(100):
    if n < 10:
        print(f"0{n}, ", end = '')
    elif 10 <= n < 99:
        print(f"{n}, ", end ='')
    else:
        print(f"{n}")
