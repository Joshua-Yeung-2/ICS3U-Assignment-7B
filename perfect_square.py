# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the prefect square


def on_all(loop_number, loop_number_2):
    # this function is to calculate the prefect square
    total = 0
    loop_counter = 0
    for loop_counter in loop_number:
        total = loop_number[loop_counter] * loop_number_2[loop_counter]
    total = total

    return total

def main():
    # this function is to shows the prefect square

    loop_number = []
    loop_number_2 = []
    
    # process
    print("starting ...")
    print("")

    for loop_counter in range(0, 21):
        loop_number.append(loop_counter)

    for loop_counter_2 in range(0, 21):
        loop_number_2.append(loop_counter_2)
        
    # call function
    on_all_2 = on_all(loop_number, loop_number_2)
    
    # output
    for loop_counter_3 in range(0, len(loop_number)):
        print("{0} x {1} = {2}".format(loop_counter_3, loop_counter_3, on_all_2[loop_counter_3]))

    print("\nDone")


if __name__ == "__main__":
    main()
