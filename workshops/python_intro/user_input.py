
def calculate_rolling_average(number_of_elements, current_average, new_value):
    new_num_elements = number_of_elements + 1
    new_avg = (1.0*current_average*number_of_elements + new_value) / new_num_elements
    return (new_num_elements, new_avg)

def main():
    print('hello world')
    num_elements = 0
    current_average = 0
    entry = ''

    while (entry != 'end'):
        entry = input("please enter numbers you'd like to know a rolling average of. enter 'end' to end the sequence: ")
        if (entry == 'end'): break
        else: 
            entry = int(entry)
            (num_elements, current_average) = calculate_rolling_average(num_elements, current_average, entry)
        print(f"""you've entered {num_elements} so far.""")
        print(f"""the average of these elements is {current_average}""")

    # maybe perform save to csv, then read from
    # alternatively, do fake data example w/ random seed example

if __name__ == "__main__":
    main()