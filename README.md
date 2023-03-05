# connexion_experiment
repro a bug

# Installation

```bash
pipenv install
pipenv shell
pip install git+https://github.com/spec-first/connexion.git@3.0.0a1
```

# Usage

```bash
uvicorn connexion_experiment.uwsgi_config:APP --port=5000
```

In browser [http://localhost:5000/version](http://localhost:5000/version)

See stdout for trace
