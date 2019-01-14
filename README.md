# Simple math test generator - Простой генератор задач
## In a nutshell
This project will help with routine generation of simple math problems.
Суть проекта в том, что довольно часто возникает необходимость сгенерировать массив однотипных задач.

## Workflow
You run a script with command  - Запуск скрипта по bash команде
```sh
python3 problemsComposer.py .
```
or 
```
python3 problemsComposer.py <absolute or relative path>
```

Then script will search directory for config files ending with ```.prtml```. After that it would generate a bunch of pdf documents with problems. Latex sources will also be provided. - 
Далее скрипт генерирует задачи в pdf-файлы, принимая настройки из конфиг-файлов, оканчивающихся на ```.prtml```. Все происходит в указанной скрипту директории.

## The config file structure
Configuration file should be JSON-formatted. Here's a sample:
```
[{
        // script generates a collection of similar problems according to your config
        // clearly, these problems have some common template body. Put it here
		"CommonBody": "Пусть в мешке есть $$L шариков, из них $$M - белые. $$PA - вероятность достать белый, $$PB - вероятность достать черный",
        
        // now, using the very same, you can generate different questions with various numerical inputs 
		"Questions": [{
		    // as questions are similar (we expect them to have similar body)
			"Prefix": "Какова вероятность ",
			// each question corresponds to some unknown value. Here're these values
			"values": ["$$PA", "$$PB"],
			
			// provide simple fomulas to calculate the answer. They must satisfy Python grammar
			"answer": {
				"$$PA": "M  / L",
				"$$PB": "1 - (M / L)"
			},

			"quantity": {
			// for each unknown value we might want to generate a certain number of questions. Put it here.
				"$$PA": "1",
				"$$PB": "1"
			}
		}]
	},

    // this JSON stores the relation between Python variables and their LATEX notation
	{
		"$$PA": "$P(A)$",
		"$$PB": "$P(B)$",
		"$$L": "$L$",
		"$$M": "$M$"
	},
    
    // you don't want your students to suffer from incorrect inputs
    // put your assertions here as a single Pythonic logical expression
	"$$PA < 1 and $$PB < 1 and $$M < $$L",
    
    // finally, you want the script to generate random values resctricted to your taste
    // put some Pythonic expression to assign value to input values
	{
		"$$M": "randint(0, 100)",
		"$$L": "randint(0, 200)"
	}
]
```
