# A deeper dive to understand Oauth2 and secured api


## Requirements

* Be able to lock access to certain API if there is no valid token
* Be able to use Swagger UI still
* Be able to run unit and integration tests

**OAuth2** is a specification that defines several ways to handle authentication and authorization. **OpenID Connect** is another specification, based on OAuth2, to make it more interoperable.

OAuth2 was designed so that the backend or API could be independent of the server that authenticates the user.

OpenAPI defines the `apiKey`, `http`, `oauth2`, `openIdConnect` security schemes. Http with a bearer: a header Authorization with a value of Bearer plus a token

## FastAPI and security

There are different libraries available. We can try to use the bare minimum and leverage FastAPI. [FastAPI ways to support authentication and authorization.](https://fastapi.tiangolo.com/tutorial/security/). FastAPI provides several tools for each of the security schemes in the `fastapi.security` module that simplifies using these security mechanisms.

A "token" is just a string with some content that we can use to verify a user. It is set to expire after some time. The frontend stores that token temporarily somewhere. 

Add to the main.py the security module and `OAuth2PasswordBearer`

```python
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

It declares that the URL /token will be the one that the client should use to get the token. `token` is an URL relative to the current web context.

The `oauth2_scheme` can be used in Depends of endpoints. This callable will go and look in the request for that Authorization header, check if the value is Bearer plus some token, and will return the token as a str.

```python
@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
```

When we create an instance of the OAuth2PasswordBearer class we pass in the tokenUrl parameter. This parameter contains the URL that the client (the frontend running in the user's browser) will use to send the username and password in order to get a token

In OAuth2 a "scope" is just a string that declares a specific permission required.

## How to validate

```
pip install "fastapi[standard]"
```

* run it: `fastapi dev main.py`  URL [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Deploy with Helm

The helm chart was created using `helm create demo-openid`

* `docker build -t j9r/fast-openid .`
*  

## Source of information

* [FastAPI doc](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#oauth2passwordrequestform)
* [Securing FastAPI with Keycloak](https://medium.com/@buffetbenjamin/securing-fastapi-with-keycloak-the-adventure-begins-part-1-e7eae3b79946)
* [Part 2](https://medium.com/@buffetbenjamin/securing-fastapi-with-keycloak-part-2-a-tale-of-roles-660ab5963ee5)
* [Keycloak doc](https://www.keycloak.org/documentation)
