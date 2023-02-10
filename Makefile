flake8:
	flake8 .

isort:
	sh -c "isort . "

clean-build:
	rm -rf *.egg-info dist build

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

trim:
	trim corevps

unify:
	unify --in-place -r .

trail-comma:
	find . -name '*.py' -exec add-trailing-comma {} +

style-fix:
	sh -c "isort . "
	trim corevps
	unify --in-place -r .
	find . -name '*.py' -exec add-trailing-comma {} +
