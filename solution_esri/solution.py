import argparse


def next_number_generator(n: int) -> int:
    while n > 1:
        n = n//2 if n % 2 == 0 else 3*n + 1
        yield n


def calculate_seq_len(n: int) -> int:
    if n == 0:
        raise SequenceError

    return len(list(next_number_generator(n)))


def get_the_nth_number(n: int, index: int) -> int:
    if n == 0:
        raise SequenceError

    for i, nth in enumerate(next_number_generator(n)):
        if i+1 == index:
            return nth


class SequenceError(ValueError):
    """
    Custom Error to indicate the sequence does not end un 1.
    """
    def __init__(self):
        super().__init__("Sequence does not end in 1")


def parse_arguments():
    """
    Parse the command line arguments through argparse.
    Print the help on the command line if cant be parsed.
    :return:
    """
    parser = argparse.ArgumentParser(description='To run the solution')
    parser.add_argument('n', type=int, help='number to start the sequence')
    parser.add_argument('--len', help='get the length of the sequence', action='store_true')
    parser.add_argument('--nth', type=int, help='get the nth number of the sequence')
    try:
        args = parser.parse_args()
        return args
    except argparse.ArgumentError:
        parser.print_help()


def dispatch(args):
    """
    Call the selected function in the command line argumments.
    :param args: (namespace) parsed arguments.
    :return: (int or None)
    """
    # if --len argument was entered
    if args.len:
        return calculate_seq_len(args.n)
    # if --nth argument was entered
    elif args.nth:
        return get_the_nth_number(args.n, args.nth)
    else:
        return None


if __name__ == "__main__":
    args = parse_arguments()
    print(dispatch(args))

