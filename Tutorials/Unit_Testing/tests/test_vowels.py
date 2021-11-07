from programs.vowels import vowels

def test_vowel_count():
    assert vowels("pneumonoultramicroscopicsilicovolcanoconiosis") == 20

def test_sentence():
    assert vowels("The quick brown fox jumps over the lazy dog.") == 11

