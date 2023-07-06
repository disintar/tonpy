#!/bin/bash
/tmp/tonpy/install_prebuilt.sh
python -m pip --default-timeout=1000 install -r /tmp/tonpy/built_requirements.txt
python -m pip --default-timeout=1000 install -r /tmp/tonpy/docs_requirements.txt
python -m pip --default-timeout=1000 install -r /tmp/tonpy/requirements.txt
cd /tmp/tonpy && pytest
cd /tmp/tonpy && python -m build --wheel --outdir dist/ .
cd /tmp/tonpy && python fix_whl_name.py
