import random
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Generate a random permutation of input lines."
    )

    # Treat each command-line operand as an input line.
    parser.add_argument(
        "-e", "--echo",
        action="store_true", dest="echo", default=False,
        help="Treat each command-line operand as an input line."
    )

    # Act as if input came from a file containing the range of unsigned decimal integers lohi, one per line.
    parser.add_argument(
        "-i", "--input-range",
        type=str, dest="input_range",
        help="Act as if input came from a file containing the range of unsigned decimal integers lohi, one per line."
    )

    # Output at most n lines. By default, all input lines are output.
    parser.add_argument(
        "-n", "--head-count",
        type=int, dest="count",
        help="Output at most n lines. By default, all input lines are output."
    )

    # Repeat output values, i.e., select with replacement.
    parser.add_argument(
        "-r", "--repeat",
        action="store_true", dest="repeat", default=False,
        help=(
            "Repeat output values, that is, select with replacement. With this option the output is not a "
            "permutation of the input; instead, each output line is randomly chosen from all the inputs. "
            "This option is typically combined with --head-count; if --head-count is not given, shuf repeats indefinitely."
        )
    )
    options, args = parser.parse_known_args(sys.argv[1:])
    
    # Variables
    count = -1
    input_range = []
    range_min = -1
    range_max = -1
    input_file = None
    input_list = []

    # Handle input source
    # In the case of echo, input is a list from the command line.
    # In the case of no file input, input is a list from the command line.
    # In the case of -i, input is a range of values. 
    # In the case of anything else, input is a filename. 
    if options.echo:
        if options.input_range is not None:
            parser.error("Incongruent arguments: ECHO and RANGE")
            sys.exit(1)
        input_list = args
    elif options.input_range is not None:
        input_range = options.input_range.split('-')
        range_min = int(input_range[0])
        range_max = int(input_range[1])
        if range_min > range_max or len(input_range) > 2:
            parser.error("Invalid RANGE")
            sys.exit(1)
    elif len(args) == 0 or args[0] == "-":
        input_list = sys.stdin.read().splitlines()
    else:
        with open(args[0], 'r') as f:
            input_list = [line.rstrip('\n') for line in f]

    if options.input_range and len(args) > 0:
      parser.error("Cannot specify both --input-range and file input.")
      sys.exit(1)
    
    # Determine Count
    if options.count is not None: # if count is explicitly given
        count = options.count
    else:
        if not options.repeat:
            if input_file or input_list: # if input is a file, echo, or stdin
                count = len(input_list)
            else: # if input is a -i
                count = 1 + range_max - range_min

    # Error-Checking Count
    if not options.repeat:
        if input_list or input_file:
            available = len(input_list)
        else:
            available = 1 + range_max - range_min
        if count > available:
            parser.error("Requested more lines than available without --repeat.")
            sys.exit(1)

    # Do range-shuffle
    if input_range:
        i = 0
        if not options.repeat:
            input_list = random.sample(range(range_min, range_max+1), count)
            for i in input_list:
                sys.stdout.write(str(i) + "\n")
        else:
            while count == -1 or i < count:
                sys.stdout.write(str(random.randint(range_min, range_max)) +  "\n")
                if count != -1:
                  i += 1
        sys.exit(0)

    # Echo, stdin, and standard output. 
    if input_list:
        if not options.repeat:
            random.shuffle(input_list)
            for i in range(min(count, len(input_list))):
                sys.stdout.write(input_list[i] + "\n")
        else:
            i = 0
            while count == -1 or i < count:
                rand = random.randint(0, len(input_list) - 1)
                sys.stdout.write(input_list[rand] + "\n")
                if count != -1:
                  i += 1
        sys.exit(0)
    if not input_list and not input_range:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()