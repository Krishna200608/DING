import argparse
from src import data


def init(args):
    data.init(args.path)


def hash_objects(args):
    data.hash_objects(args)


def parse_args():
    parser = argparse.ArgumentParser(prog="ding")

    commands = parser.add_subparsers(dest="command", required=True)

    init_parser = commands.add_parser(
        "init", help="initializes an empty ding repository"
    )

    init_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="directory to initialize the ding repository in (default: current directory)",
    )
    init_parser.set_defaults(func=init)

    hash_parser = commands.add_parser("hash", help="hashes the file and folders")
    hash_parser.add_argument(
        "file", help="the file to be hashed"
    )
    hash_parser.set_defaults(func=hash_objects)

    return parser.parse_args()


def main():
    print("Ding Dong, who's there?\nThe IRS\nOh Shit\n")
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
