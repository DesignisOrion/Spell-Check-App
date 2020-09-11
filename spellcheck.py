# SpellChecker in Python

# This program allows you to make corrections to mispelled words. The goal is to add this to the Forde Text Editor build prior. Enjoy

# pip install pySpellChecker

from spellchecker import SpellChecker


spell = SpellChecker()

missplelled = spell.unknown(
    ['somethoing', 'is', 'happening', 'here', 'pheone', 'goalz', 'keeboard'])

for word in missplelled:
    print(spell.correction(word))
