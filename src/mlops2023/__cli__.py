"""Command line interface for mlops2023"""

# Importing the libraries

from cleo.application import Application

from . import __version__
from .models.download import DownloadCommand


app = Application("mlops2023", __version__)
app.add(DownloadCommand())


def main():
    app.run()


if __name__ == "__main__":
    main()
