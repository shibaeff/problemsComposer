import argparse
import logging

class ConsoleLoader:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.cli_logger = logging.getLogger(__name__)

        self.cli_logger.disabled = False

        self.parser = argparse.ArgumentParser(
            description="Takes folder with problem templates"
            "and proccesses them into ready-to-go problems in .pdf & LATEX")
        self.parser.add_argument('foldername', metavar='F', 
                            help="name of folder to generate problems")

        self.cli_logger.info("CLI successfully works")
        try:
            self.args = self.parser.parse_args()
        except Exception:
            print("Incorrect foldername arguement was provided."
                  "To run script in the current folder pass .")

    def get_folder_name(self):
        return self.args.foldername

