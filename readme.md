# Project Sign-in and Verification PDF

Created with :gift_heart: by Keluarga Kosimp

## Introduction

## Project Overview

## Collaborators

- [05111940000018 - Pramudya Tiandana Wisnu Gautama](https://github.com/wisnupramoedya)
- [05111940000062 - Thomas Felix Brilliant](https://github.com/ThomasFel)
- [05111940000096 - Stefanus Albert Kosim](https://github.com/yanzkosim)
- [05111940000175 - Muhammad Daffa](https://github.com/daffainfo)

## Requirements

## How to Use The Project

### How to Prepare

1. At very first initialisation, create virtual env.

```
python -m venv venv
```

2. Activate virtual env.

```
./venv/Scripts/activate
```

3. Check where the python refers to (run the code below). If it is in `{this_folder}/venv/Scripts`, then it should be correct.

```
python -c "import os, sys; print(os.path.dirname(sys.executable))"
```

4. Install the requirements needed.

```
pip install -r requirements.txt
```

5. If you want to create/update _requirements.txt_, add freeze.

```
pip3 freeze > requirements.txt
```

### How to Run

1. Activate virtual env.

```
./venv/Scripts/activate
```

2. Start the program after activate the virtual env.

```
# for signing
python signing.py

# for verification
python verification.py
```

## Author's Note

This project is a part of Information and Network Security (C) 2022 course, Department of Informatics, ITS.