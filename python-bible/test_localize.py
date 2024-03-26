import gettext


localizator = gettext.translation('app', localedir='localize', languages=['fr'])
localizator.install()

_ = localizator.gettext 
# ...
print(_('This is a translatable string.'))

print(_('Your name.'))