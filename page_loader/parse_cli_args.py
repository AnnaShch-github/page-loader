import argparse


def parse_cli_args():
    # Parsing of the arguments
    parser = argparse.ArgumentParser(
        description='Download html page from a website'
    )
    parser.add_argument('link',
                        help='The address of the page for downloading',
                        type=str)
    parser.add_argument('-o', '--output',
                        help='The directory where the page is downloaded',
                        default='os.getcwd')
    args = parser.parse_args()
    return args
