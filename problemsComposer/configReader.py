import json
import logging

class Question:
    def __init__(self):
        self.Prefix = None
        self.values = list()
        self.answer = dict()
        self.quantity = dict()

class Problem:
    def __init__(self):
        self.CommonBody = None
        self.Questions = list()

class ConfigHolder:
    def __init__(self):
        self.Problem = None
        self.symbol_map = dict() # stores the relation between LATEX and $$<python_variable_name> 

    def generate_assert(self, raw_strng: str):
        self.assert_string = "assert(" + raw_strng.replace("$$", "self.") + ")"

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("Generated assert string %s" % self.assert_string)

    def run_assert(self):
        eval(self.assert_string)

    def generate_debug_msg(self):
        dbg1 = "Got config for problem with body %s. The possible prefixes for the questions are" % self.Problem.CommonBody

        dbg2 = []

        for question in self.Problem.Questions:
            print(question)
            dbg2.append(question.Prefix)

        dbg2 = ";".join(dbg2)
        return dbg1 + dbg2



class ConfigReader:
    def __init__(self, filename):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.disabled = False

        raw = open(filename)
        self.config_data = json.load(raw)

        self.logger.info("Got config from file %s" % filename)

    # after that goes the construciton of config object
    def construct_problem(self, data):
        problem = Problem()
        problem.CommonBody = data["CommonBody"]

        for raw_question in data["Questions"]:
            q = Question()
            q.Prefix = raw_question["Prefix"]
            q.values = raw_question["values"]
            q.answer = raw_question["answer"]
            q.quantity = raw_question["quantity"]
            problem.Questions.append(q)

        return problem

    def construct_config_holder(self):
        config_holder = ConfigHolder()

        config_holder.Problem = self.construct_problem(self.config_data[0])
        config_holder.symbol_map = self.config_data[1]

        config_holder.generate_assert(self.config_data[2])
        config_holder.ranges = self.config_data[3]
        for key in config_holder.ranges:
            key = key[2:]

        # self.logger.info(config_holder.generate_debug_msg())
        return config_holder


        
