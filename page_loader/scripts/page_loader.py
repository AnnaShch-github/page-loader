#!/usr/bin/python3
import sys

import requests

from page_loader.loader import loader
from page_loader.logger import logger

from page_loader.parsing import parse_cli_arguments


def download():
    # The main function of tha package
    try:
        args = parse_cli_arguments()
        print(loader(args.link, args.output))
    except requests.HTTPError:
        sys.exit(1)
    except requests.ConnectionError:
        sys.exit(1)
    except requests.URLRequired:
        sys.exit(1)
    except requests.TooManyRedirects:
        sys.exit(1)
    except requests.Timeout:
        sys.exit(1)
    except PermissionError:
        logger.error("Unfortunately, you don't have permission")
        sys.exit(1)


if __name__ == '__main__':
    download()
