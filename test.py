# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the prefect square


def main():
    # this function is to shows the prefect square

    loop_number = []
    loop_number_2 = [] 

    # process
    print("starting ...")
    print("")

    for loop_counter_1 in range(0, 21):
        loop_number.append(loop_counter_1)

    for loop_counter_2 in range(0, 21):
        loop_number_2.append(loop_counter_2)
        
    for loop_counter in loop_number:
        total = loop_number[loop_counter] * loop_number_2[loop_counter]
        print("{0} x {1} = {2}".format(loop_counter, loop_counter, total))

    print("\nDone")


if __name__ == "__main__":
    main()
