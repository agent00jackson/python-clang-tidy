Was experimenting with this repo before I found out that `clang-tidy` is a thing.

My goal was to basically do what [google-readability-casting](https://clang.llvm.org/extra/clang-tidy/checks/google/readability-casting.html) does.

Using google-readability-casting:
```
clang-tidy test.cpp -checks=google-readability-casting --export-fixes=fix.yml
# preprocess fix.yml to remove irrelevant files
clang-apply-replacements . # searches for .yaml (not .yml) files
```