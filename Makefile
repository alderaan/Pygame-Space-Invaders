ENV_NAME = pygame_1 

.PHONY: create_env remove_env 

ENVIRONMENT := development

# Export the environment variable for all commands in this Makefile
.EXPORT_ALL_VARIABLES:

create_env:
	conda env create -n $(ENV_NAME) -f environment.yml

remove_env:
	conda env remove -n $(ENV_NAME)


run_example:
	python3 -m pygame.examples.aliens