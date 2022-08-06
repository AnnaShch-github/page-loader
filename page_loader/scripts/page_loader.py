#!/usr/bin/python3
from page_loader.loader import loader

from page_loader.parsing import parse_cli_arguments


def download():
    # The main function of tha package
    args = parse_cli_arguments()
    print(loader(args.link, args.output))


if __name__ == '__main__':
    download()
