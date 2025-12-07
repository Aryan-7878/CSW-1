import sys

def main():
    # Get command-line arguments, excluding the script name
    args = sys.argv[1:]
    
    # If no numbers are given
    if not args:
        print("Usage: python q8.py <num1> <num2> <num3> ...")
        return

    total = 0  # variable to store the sum

    for arg in args:
        try:
            total += float(arg)  # convert argument to number and add
        except ValueError:
            print(f"Error: Invalid input '{arg}'. Please enter only numbers.")
            return  # exit the program if an invalid input is found

    print(f"Sum of numbers: {total:g}")  # :g removes unnecessary .0 for integers


if __name__ == "__main__":
    main()