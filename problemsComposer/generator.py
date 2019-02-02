import logging
from sympy import *
from random import *

class Generator:
    def __init__(self, config_holder):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.disabled = False

        self.config_holder = config_holder
        # creating numpy symbols
        self.variables = dict([(x[2:], symbols(x[2:])) for x in config_holder.symbol_map])
        self.ranges = config_holder.ranges

    def generate_text(self, subdict, question):
        text = self.config_holder.Problem.CommonBody + question
        
        
        for symbol in subdict:     
            text = text.replace("$$"+str(symbol), str(subdict[symbol]))

        left = set(self.config_holder.symbol_map).difference(set(["$$" + str(symbol) for symbol in subdict]))

        for symbol in left:
            text = text.replace(symbol, self.config_holder.symbol_map[symbol])
        return text

        

    def generate_problem(self):
        # just yields problem-value pairs to the generator

        # list of distinct quesiton types
        
        question_number = randint(0, len(self.config_holder.Problem.Questions)) - 1
        question = self.config_holder.Problem.Questions[question_number]
        value = choice(self.config_holder.Problem.Questions[question_number].values)

        self.logger.info("Chose value %s" % value)
                
        equation = question.answer[value]
        equation = sympify(equation)   
                    
        subdict = dict({
            (self.variables[var[2:]], eval(self.config_holder.ranges[var])) for var in self.config_holder.ranges
            })
                    
        print(subdict)

        ans = equation.subs(subdict)

        return (self.generate_text(subdict, question.Prefix + value + "?"), ans)


        
