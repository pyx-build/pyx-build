try {
    python runner.py $1
}
catch {
    mkdir python
    cd python
    Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe' -OutFile 'python-3.8.2-amd64.exe'
    ./python-3.8.2-amd64.exe 
    echo "Rerun the scipt after the installation completes"
}
