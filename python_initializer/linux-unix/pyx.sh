!#/bin/bash

{
    python runner.py $1 
} || {
    mkdir python
    cd python
    wget https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tgz 
    tar -xf Python-3.10.5.tgz
    cd Python-3.10.5
    ./configure
    make
    make install
    echo "Rerun after installation is complete"
}
