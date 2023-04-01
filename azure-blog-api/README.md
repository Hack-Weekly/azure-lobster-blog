Install [Poetry](https://python-poetry.org/docs/#installation)

### Configure poetry and vscode if you would like
Run: 
`poetry config virtualenvs.in-project true`


### Build Dockerfile
`docker build -t azure_blog_api .`

### Run Container
`docker run -p 8000:8000 azure_blog_api` or run detached with
`docker run -dp 8000:8000 azure_blog_api`


### Format 
`poetry run black azure_blog_api/ tests/`

### Lint
`poetry run flake8 azure_blog_api/`

### Test
`poetry run pytest`

