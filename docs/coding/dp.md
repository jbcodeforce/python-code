# Design Patterns

Here are some examples on how to implement some classical design pattern in Python.

## Singleton

Singleton Pattern ensures that only one instance of a class exists and provides a global point of access to it.

```python
class _Glossary:
    _instance = None

    # method for the singleton class....

def Glossary(path:str ) -> _Glossary:
    """Factory method to access to the unique instance"""
    if _Glossary._instance is None:
        _Glossary._instance = _Glossary()
        _Glossary._instance.load_glossary(path)
    return _Glossary._instance
```

Access to a singleton from a FastAPI app using dependency injection for example

```python 
def get_db() -> Optional[Database]:
    return Database()

app = FastAPI()

@app.get("/")
def read_root(db: Optional[Database] = Depends(get_db)):
    if db:
        result = db.db.my_collection.find_one()
        return {"message": result}
```


## Dependency injection

