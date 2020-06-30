```
pipenv install && pipenv shell
export FLASK_APP='scantree_recursive.py'
export FLASK_ENV=development
flask run
```

scantree_recursive.py usable from commandline without `pipenv shell` via `pipenv-shebang`