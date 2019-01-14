from __future__ import division
from console import ConsoleLoader
from folderLoader import FolderLoader
from configReader import ConfigReader
from generator import Generator
import logging


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

    for config_file in configs_filenames:
        config_reader = ConfigReader(config_file)
        config_holder = config_reader.construct_config_holder()

        main_logger.info("Config object has been generated")

        problems_generator = Generator(config_holder)
        problems = problems_generator.generate_problems()

        for problem in problems:
            print(problem)


    
