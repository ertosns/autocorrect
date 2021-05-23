# autocorrect
- it's an auto correction built with simple argmax function over the most likely transformation of each word within 2 edits maximum.
- note that the auto-correction isn't perfect, the algorithm has no sense of the semantics.

# execution example
``` shell
naive@bayes:~/autocorrect$ python3 ar_autocorrect.py
corpus with 9203724 words
write your sentence:
بيفول ان الكلام قارع
suggestion for wordبيفول is بيقول
suggestion for wordان is ان
suggestion for wordالكلام is الكلام
suggestion for wordقارع is قارع
بيقول ان الكلام قارع
write your sentence:
النعلم هو امتل استثماز
suggestion for wordالنعلم is العلم
suggestion for wordهو is هو
suggestion for wordامتل is احتل
suggestion for wordاستثماز is استثمار
العلم هو احتل استثمار

```

# dataset
- the vocabulary is built from [Egyptian Arabic wikipedia](https://drive.google.com/file/d/1bgDu-LFQRB0wHGtRCCqJW5Gg_4DDDB0G/view?usp=sharing), make sure to install it under directory data
