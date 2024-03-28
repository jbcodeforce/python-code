
## The localization examples

How to make a string translated in another language using GNU gettext.

See the code test_localize.py

* install poedit
* upadte PATH to point to `C:\Program Files (x86)\Poedit\GettextTools\bin`
* get the localizable string from the python program
* xgettext -d app -o localize/app.pot test_localize.py
* then create localize/fr/LC_MESSAGES/app.po from the created app.po under localize
* Compile the po to mo: msgfmt -o localize/fr/LC_MESSAGES/app.mo localize/fr/LC_MESSAGES/app
* export LANG=fr
* python test_localize.py



