#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update;
    brew outdated pyenv || brew upgrade pyenv;
    brew install pyenv-virtualenv
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile;
    exec $SHELL;
    pyenv install $PYTHON
    export PYENV_VERSION=$PYTHON
    export PATH="/Users/travis/.pyenv/shims:${PATH}"
    brew install swig;
    pyenv virtualenv $PYTHON venv;
    pyenv activate venv;
    python --version;
    pip install tox;

    case "${TOXENV}" in
        py27)
            # Install some custom Python 3.2 requeriments
            brew install python;
            pip install tox-travis;
            ;;
        py35)
            # Install some custom Python 3.5 requeriments
            pip3 install tox-travis;
            ;;
    esac

else
    # Install some custom requeriments por Linux
    pip install tox-travis;
    eval "$(gimme 1.10)"
    sudo apt-get update && sudo apt-get install swig
fi
