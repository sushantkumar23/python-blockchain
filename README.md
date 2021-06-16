**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**

```
pip install -r requirements.txt
```

**Run the tests**
Make sure you have the virtual environments activated before you run the tests

```
python -m pytest backend/tests
```

**Run the application and the API**
Make sure to activate the virtual environment.

```
python -m backend.app
```

**Run a peer instance**

```
export PEER=True && python -m backend.app
```
