# このリポジトリについて

Python Machine Learningを学ぶためのipython notebookの置き場になる予定

# Setup

```
brew install pyenv
pip install virtualenv
pyenv install 3.4.3
pyenv rehash
pyenv local 3.4.3
virtualenv env
source env/bin/activate
python -V
>>3.4.3
```

これでもpythonのバージョンがシステムと一緒だと

```
virtualenv -p ~/.pyenv/versions/3.4.3/bin/python3.4 env
```

を試す

```
pip install -r requirements.txt
pip install --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-0.6.0-py3-none-any.whl
ipython notebook
```

で完了。

動かなかったら、`.zshenv`に

```
aliasipy="python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()’"
```

を追加する
