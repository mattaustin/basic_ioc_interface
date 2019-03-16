# Tests

Tests can be run using the built docker image:

```bash
docker run --entrypoint=/opt/venv/bin/python basiciocinterface_web_put -m unittest
```


In development, you;ll probably want to mount the web_put directory so you don't need to rebuild the image with every code modification:

```bash
docker run --tty --volume="${PWD}/web_put":/opt/project --entrypoint=/opt/venv/bin/python --env=PYTHONPATH=/opt/project/src basiciocinterface_web_put -m unittest
```
