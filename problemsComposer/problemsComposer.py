from __future__ import division
from console import ConsoleLoader
from folderLoader import FolderLoader
# from configReader import ConfigReader
# from generator import Generator
# from latexGen import LatexGen
import logging
from latexGen import latexGen


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main_logger = logging.getLogger(__name__)
    main_logger.disabled = False

    console_loader = ConsoleLoader()
    foldername = console_loader.get_folder_name()
    main_logger.info("Got foldername %s" % (foldername))

    # configs_filenames = FolderLoader(foldername)
    folder_loader = FolderLoader(foldername)
    configs_filenames = folder_loader.get_config_list()
    main_logger.info("Folder was correctly processed")
    
    if configs_filenames is None or len(configs_filenames) == 0:
        print("No config files were found in your folder. Remember the .prtml format")

    latex_template_name = "ltxtml"

    latex_gen = latexGen(foldername, latex_template_name, configs_filenames)
    latex_gen.generate_file()



    
