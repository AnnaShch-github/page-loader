#!/usr/bin/python3
import sys

import requests

from page_loader.loader import download
from page_loader.logger import logger

from page_loader.parse_cli_args import parse_cli_args


def main():
    # The main function of tha library
    try:
        args = parse_cli_args()
        print(download(args.link, args.output))
    except requests.HTTPError:
        logger.error('Sorry, an HTTP error has occurred.'
                     'The program will be closed')
        sys.exit(1)
    except requests.ConnectionError:
        logger.error('Sorry, failed to establish a connection to the web site.'
                     'Please check your internet connection.')
        sys.exit(1)
    except requests.URLRequired:
        logger.error('Sorry, an URL error has occurred.'
                     'The program will be closed')
        sys.exit(1)
    except requests.TooManyRedirects:
        logger.error('Sorry, too many redirects occurred.'
                     'The program will be closed')
        sys.exit(1)
    except requests.Timeout:
        logger.error('Sorry, the server has not issued a response for timeout. '
                     'Please repeat.')
        sys.exit(1)
    except FileNotFoundError as error:
        logger.error(f'The system cannot find the path: {error.filename}')
        sys.exit(1)
    except PermissionError as e:
        logger.error(f"Sorry, you don't have the permission to {e.filename}")
        sys.exit(1)


if __name__ == '__main__':
    main()
