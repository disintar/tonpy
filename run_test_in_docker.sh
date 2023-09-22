#!/bin/bash

python -m pip install --default-timeout=100 --upgrade pip
python -m pip install --default-timeout=100 -r /tmp/tonpy/requirements.txt
python -m pip install --default-timeout=100 -r /tmp/tonpy/built_requirements.txt
cd /tmp/tonpy && pytest
cd /tmp/tonpy && python -m build -n --wheel --outdir dist/ .
cd /tmp/tonpy && python fix_whl_name.py
