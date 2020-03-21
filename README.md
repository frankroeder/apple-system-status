# Apple System Status 

This tool scrapes information about the status of services by apple.

## Docker

To not pollute your system with any temporary files, one can build and execute
it via docker:

- `docker build --rm -t apple-system-status .`
- `docker run --rm -it apple-system-status`

or just pull it from my [dockerhub](https://hub.docker.com/u/bassstring) and run it directly:

- `docker run --rm -it bassstring/apple-system-status`


## Virtual Environment

For docker haters:
- `python3 -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
- `python main.py`
