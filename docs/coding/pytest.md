# Pytest Summary and Usage

Pytest is a mature, full-featured Python testing framework that makes it easy to write small tests while scaling to support complex functional testing.

## Installation

```bash
pip install pytest
```

## Basic Usage

### Writing Tests

Test functions must be prefixed with `test_` and placed in files named `test_*.py` or `*_test.py`:

```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string_concatenation():
    assert "hello " + "world" == "hello world"
```

### Running Tests

```bash
# Run all tests in current directory
pytest

# Run with verbose output
pytest -v

# Run a specific file
pytest test_example.py

# Run a specific test function
pytest test_example.py::test_addition

# Run tests matching a keyword expression
pytest -k "addition"
```

## Assertions

Pytest uses plain Python `assert` statements with detailed failure introspection:

```python
def test_equality():
    assert [1, 2, 3] == [1, 2, 3]
    
def test_membership():
    assert "hello" in "hello world"
    
def test_comparison():
    assert 10 > 5
```

### Testing Exceptions with `pytest.raises`

Use `pytest.raises` to assert that specific exceptions are raised:

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_exception_message():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        raise ValueError("Exception 123 raised")

def test_access_exception_info():
    with pytest.raises(RuntimeError) as excinfo:
        raise RuntimeError("Something failed")
    assert "failed" in str(excinfo.value)
    assert excinfo.type is RuntimeError
```

---

## Fixtures

Fixtures provide a mechanism for test setup, teardown, and dependency injection. They are defined using the `@pytest.fixture` decorator.

### Basic Fixture

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_name(sample_data):
    assert sample_data["name"] == "Alice"
```

### Fixture with Setup and Teardown (yield)

Use `yield` to separate setup and teardown logic:

```python
import pytest
import sqlite3

@pytest.fixture
def database(tmp_path):
    """Create a temporary database for testing."""
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")
    conn.commit()

    yield conn  # Provide the connection to the test

    # Cleanup happens after test completes
    conn.close()

def test_query_users(database):
    cursor = database.cursor()
    cursor.execute("SELECT name FROM users ORDER BY name")
    results = [row[0] for row in cursor.fetchall()]
    assert results == ['Alice', 'Bob']
```

### Fixture Scope

The `scope` parameter controls how often a fixture is invoked:

| Scope | Description |
|-------|-------------|
| `function` | (default) Run once per test function |
| `class` | Run once per test class |
| `module` | Run once per module |
| `package` | Run once per package |
| `session` | Run once per test session |

```python
@pytest.fixture(scope="session")
def api_token():
    """Session-scoped fixture that runs once for all tests."""
    return "test-token-12345"

@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)
```

### Autouse Fixtures

Fixtures with `autouse=True` are automatically invoked for all tests within their scope:

```python
@pytest.fixture(autouse=True)
def setup_logging():
    """Automatically runs before every test."""
    print("Setting up logging...")
    yield
    print("Tearing down logging...")

@pytest.fixture(scope="class", autouse=True)
def class_setup(order):
    """Runs once per class automatically."""
    order.append("class_setup")
```

When an autouse fixture has dependencies, those dependencies are also invoked automatically.

### Sharing Fixtures with `conftest.py`

Place fixtures in a `conftest.py` file to share them across multiple test files:

```python
# conftest.py
import pytest

@pytest.fixture
def shared_resource():
    return {"shared": True}

# test_a.py - can use shared_resource
def test_a(shared_resource):
    assert shared_resource["shared"]

# test_b.py - can also use shared_resource
def test_b(shared_resource):
    assert "shared" in shared_resource
```

---

## Markers (Decorators)

Markers are decorators that add metadata to tests. List all available markers with:

```bash
pytest --markers
```

### `@pytest.mark.skip`

Unconditionally skip a test:

```python
@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    pass
```

### `@pytest.mark.skipif`

Skip a test based on a condition:

```python
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_posix_only():
    pass

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_new_feature():
    pass
```

### `@pytest.mark.xfail`

Mark a test as expected to fail:

```python
@pytest.mark.xfail(reason="Known bug in library")
def test_known_bug():
    assert False

@pytest.mark.xfail(raises=RuntimeError)
def test_specific_failure():
    raise RuntimeError("Expected error")
```

Run xfail tests as normal with:

```bash
pytest --runxfail
```

### `@pytest.mark.parametrize`

Run a test with multiple sets of arguments:

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (10, 11),
])
def test_increment(input, expected):
    assert input + 1 == expected

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_combinations(x, y):
    # Runs 4 times: (0,2), (0,3), (1,2), (1,3)
    pass
```

Combine parametrize with skip/xfail markers:

```python
import sys

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        pytest.param(
            10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
        ),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected
```

### `@pytest.mark.usefixtures`

Apply fixtures to a test without explicitly requesting them:

```python
@pytest.mark.usefixtures("clean_database", "mock_api")
class TestUserService:
    def test_create_user(self):
        pass
    
    def test_delete_user(self):
        pass
```

### Custom Markers

Define custom markers in `pytest.ini` or `pyproject.toml`:

```ini
# pytest.ini
[pytest]
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

Use custom markers:

```python
@pytest.mark.slow
def test_large_dataset():
    pass

@pytest.mark.integration
def test_database_connection():
    pass
```

Run only tests with specific markers:

```bash
pytest -m slow
pytest -m "not slow"
pytest -m "slow and integration"
```

### Reusable Skip Markers

Create reusable conditional skip markers by assigning `pytest.mark.skipif` to a variable:

```python
import pytest
import httpx

# Define a URL to check for network availability
API_URL = "https://api.example.com/health"

def is_url_accessible(url: str, timeout: float = 10.0) -> bool:
    """Check if a URL is accessible."""
    try:
        response = httpx.head(url, timeout=timeout, follow_redirects=True)
        return response.status_code == 200
    except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPError):
        return False

# Create a reusable skip marker
requires_network = pytest.mark.skipif(
    not is_url_accessible(API_URL),
    reason=f"URL {API_URL} is not accessible"
)

# Apply to tests or classes
@pytest.mark.integration
@requires_network
class TestAPIIntegration:
    """Tests requiring network access."""
    
    def test_fetch_data(self):
        # Test runs only if API is accessible
        pass

@requires_network
def test_external_service():
    pass
```

This pattern is useful for:

- Skipping tests when external services are unavailable
- Environment-specific test filtering
- Combining multiple skip conditions with custom markers

---

## Async Testing with pytest-asyncio

The `pytest-asyncio` plugin enables testing of async/await code.

### Installation

```bash
pip install pytest-asyncio
```

### `@pytest.mark.asyncio`

Mark async test functions to be executed with an event loop:

```python
import pytest

@pytest.mark.asyncio
async def test_async_operation():
    result = await fetch_data()
    assert result == "expected"

@pytest.mark.asyncio
async def test_async_sleep():
    import asyncio
    await asyncio.sleep(0.01)
    assert True
```

### Asyncio Modes

Configure pytest-asyncio behavior in `pyproject.toml`:

**Strict Mode (default)** - Requires explicit `@pytest.mark.asyncio` on all async tests:

```toml
[tool.pytest.ini_options]
asyncio_mode = "strict"
```

**Auto Mode** - Automatically detects and runs async tests without markers:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

```python
# With asyncio_mode = "auto", no decorator needed
async def test_auto_detected():
    await asyncio.sleep(0.01)
    assert True
```

### Async Fixtures

Use `@pytest_asyncio.fixture` for async fixtures:

```python
import pytest_asyncio

@pytest_asyncio.fixture
async def async_client():
    client = await create_async_client()
    yield client
    await client.close()

@pytest.mark.asyncio
async def test_with_async_fixture(async_client):
    result = await async_client.get("/api/data")
    assert result.status_code == 200
```

In auto mode, regular `@pytest.fixture` works for async fixtures as well.

### Complete Example

```python
"""Integration tests with async and conditional skipping."""

import pytest
import httpx

FLINK_URL = "https://nightlies.apache.org/flink/flink-docs-master/"

def is_url_accessible(url: str) -> bool:
    try:
        response = httpx.head(url, timeout=10.0, follow_redirects=True)
        return response.status_code == 200
    except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPError):
        return False

requires_network = pytest.mark.skipif(
    not is_url_accessible(FLINK_URL),
    reason=f"URL {FLINK_URL} is not accessible"
)

@pytest.mark.integration
@requires_network
class TestWebsiteLoader:
    """Tests for loading website content."""

    @pytest.mark.asyncio
    async def test_load_website(self, document_loader):
        """Test loading website content asynchronously."""
        documents = await document_loader.load(FLINK_URL, "website")
        assert len(documents) >= 1
        assert documents[0].content is not None
```

---

## Fixture Annotation Summary Table

| Decorator/Parameter | Purpose |
|---------------------|---------|
| `@pytest.fixture` | Define a fixture function |
| `scope="function"` | Fixture invoked per test (default) |
| `scope="class"` | Fixture invoked once per test class |
| `scope="module"` | Fixture invoked once per module |
| `scope="session"` | Fixture invoked once per session |
| `autouse=True` | Fixture auto-invoked without explicit request |
| `params=[...]` | Parametrize the fixture with multiple values |
| `yield` | Separate setup (before) from teardown (after) |

---

## Common Command-Line Options

| Option | Description |
|--------|-------------|
| `-v` / `--verbose` | Increase verbosity |
| `-q` / `--quiet` | Decrease verbosity |
| `-x` | Stop on first failure |
| `--maxfail=N` | Stop after N failures |
| `-k EXPRESSION` | Only run tests matching expression |
| `-m MARKER` | Only run tests with specific marker |
| `--collect-only` | Show tests that would run without executing |
| `--tb=short` | Shorter traceback format |
| `--tb=no` | Disable traceback |
| `-s` | Disable output capture (show print statements) |
| `--durations=N` | Show N slowest tests |
| `--lf` | Re-run only last failed tests |
| `--ff` | Run last failed tests first |

---

## Project Configuration

Configure pytest in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_functions = ["test_*"]
python_classes = ["Test*"]
markers = [
    "slow: marks tests as slow",
    "integration: integration tests",
]
addopts = "-v --tb=short"
```

Or in `pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py *_test.py
markers =
    slow: marks tests as slow
    integration: integration tests
```
