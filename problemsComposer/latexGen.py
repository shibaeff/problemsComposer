from generator import *
from configReader import *
import logging
import os
import re 

class latexGen:
        def __init__(self, dir, template_name, config_filenames):
            self.dir = dir
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)
            self.logger.disabled = False

            self.config_filenames = config_filenames

            template_file = open(os.path.join(dir, template_name), "r")
            self.latex_template = template_file.read()
            template_file.close()

            self.pattern = re.compile("&&[\w]*.prtml&&")
            self.positions = self.pattern.findall(self.latex_template)
            self.config_names = []
            for position in self.positions:
                self.config_names.append(position[2:-2])
                # self.logger.info("Required question from file %s" % self.config_names[-1])

            

        def generate_file(self, name = "test"):
            
            text = self.latex_template
            for config_name in self.config_names:
                
                config_reader = ConfigReader(os.path.join(self.dir, config_name))

                config_holder = config_reader.construct_config_holder()
                problems_generator = Generator(config_holder)
                problem = problems_generator.generate_problem()

                text = text.replace("&&" + config_name + "&&", problem[0], 1)
                
                self.logger.info(text)

            latex_file = open(os.path.join(self.dir, name), "w+")
            latex_file.write(text)
            latex_file.close()

            


           
        
