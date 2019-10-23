#!/bin/bash
pyenv install 2.7.1
pyenv install 3.7.1
pyenv virtualenv 2.7.1 env_for_2_7_1
pyenv virtualenv 3.7.1 env_for_3_7_1
pyenv versions
