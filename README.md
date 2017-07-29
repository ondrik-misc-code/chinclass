EMPTY

Generating secret
=================
```
$ echo "$(python -c 'import random; import string; print("".join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]))')" > secret.txt
```

Rebuilding virtualenv
=====================
```
cd
rm -rf venv
/opt/python/bin/pyvenv venv
source venv/bin/activate
pip install -r app/requirements.txt
```
