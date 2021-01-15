# WordCounter

## Counts 3 Word trios within one or more file

Note:
This will read from stdin OR take one or more files as inputs, but not both

Usage:
```
./count_words.py mobydick.txt
# or
cat mobydick.txt | ./count_words.py
```

Assumptions:
- The following punctionation characters are removed: . ? " { } [ ] ( ) , ! : ; *
- Also a starting or ending ' or - are removed, however in a word they are allowed to account for contractions, hypenated words and most possessive singular nouns

Notes:
- Possessive plural nouns and possessive singular nouns that end in s have the trailing ' removed.  Ex. the program treats Chris' and Chris are the same word
