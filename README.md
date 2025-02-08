# trainer
i wrote a quick app to help me create problemsets from a list of problems for exam preparations.
```
usage: . [-h] [-o] bank_dir num_problems num_sets

generate a problemset from a question bank.

positional arguments:
  bank_dir         path to the question bank directory.
  num_problems     number of problems per set.
  num_sets         number of total sets.

options:
  -h, --help       show this help message and exit
  -o, --overwrite  delete existing sets before creating new ones.
```
the question bank must be in the following format:
```
bank_dir
├── qs
│   ├── problem1.png
│   ├── whatever_name_works_actually.jpg
```
the problemsets will be generated in the `set` directory
```
bank_dir
├── qs
│   ├── problem1.png
│   ├── whatever_name_works_actually.jpg
├── sets
│   ├── 1
│   │   ├── 1.jpg
│   │   ├── 2.png 
```
i've included sample datasets that i created for personal use.