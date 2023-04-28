# Radium

## Setup

```commandline
git clone https://github.com/RolfAdolf/radium_test_task.git

cd radium_test_task

poetry install
```

## Run script

```commandline
python3 -m src.main
```

## Run tests

### Tests
```commandline
pytest
# add --cov option to generate code coverage report
```

### Check the coverage
```commandline
coverage report
```

## Use Docker

### Run script in the docker-container

```commandline
docker build . -t test_script:latest

docker run -it --rm --name try_script test_script
```
