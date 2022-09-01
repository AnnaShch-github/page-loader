#!/usr/bin/python3
import sys

import requests

from page_loader.loader import download

from page_loader.parse_cli_args import parse_cli_args


def main():
    # The main function of tha library
    try:
        args = parse_cli_args()
        print(download(args.link, args.output))
    except requests.HTTPError:
        print('Sorry, an HTTP error has occurred.'
              'The program will be closed')
        sys.exit(1)
    except requests.ConnectionError:
        print('Sorry, failed to establish a connection to the web site.'
              'Please check your internet connection.')
        sys.exit(1)
    except requests.URLRequired:
        print('Sorry, an URL error has occurred.'
              'The program will be closed')
        sys.exit(1)
    except requests.TooManyRedirects:
        print('Sorry, too many redirects occurred.'
              'The program will be closed')
        sys.exit(1)
    except requests.Timeout:
        print('Sorry, the server has not issued a response for timeout. '
              'Please repeat.')
        sys.exit(1)
    except FileNotFoundError as error:
        print(f'The system cannot find the path: {error.filename}')
        sys.exit(1)
    except PermissionError as e:
        print(f"Sorry, you don't have the permission to {e.filename}")
        sys.exit(1)
    except Exception as exception:
        print(f'Sorry, an error has occurred: {exception}.'
              'The program will be closed')
        sys.exit(1)


if __name__ == '__main__':
    main()
