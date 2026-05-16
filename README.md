# ioc-feed

## Run the app

From the project root, execute:

- `python -m app.main`
- or `uvicorn app.main:app --reload`

This ensures Python treats `app` as a package and resolves imports like `from .routes` correctly.
