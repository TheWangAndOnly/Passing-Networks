default: pylint

pylint:
	find . -iname "*.py" -not -path "./tests/*" | xargs -n1 -I {}  pylint --output-format=colorized {}; true
# ----------------------------------
#         LOCAL SET UP
# ----------------------------------

# run_locally:
# 	@python -W ignore -m Passing-Networks.run

install_requirements:
	@pip install -r requirements.txt

# ----------------------------------
#    LOCAL INSTALL COMMANDS
# ----------------------------------
install:
	@pip install . -U

clean:
	@rm -fr */__pycache__
	@rm -fr build
	@rm -fr dist
	@rm -fr Passing-Networks-*.dist-info
	@rm -fr Passing-Networks.egg-info
	-@rm model.joblib
