import logging 
import os


class FolderLoader:
    def __init__(self, foldername):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.disabled = False
        self.foldername = foldername
        self.find_configs()

    def find_configs(self):
        self.fileslist = []
        try:
            for file in os.listdir(self.foldername):
                if file.endswith(".prtml"):
                    self.fileslist.append(os.path.join(self.foldername, file))
        except FileNotFoundError:
            print("File you have given does not exist or there's another problem. Try again")

    def get_config_list(self):
        return self.fileslist


