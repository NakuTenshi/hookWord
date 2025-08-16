# hookWord
**hookWord** is a simple Python tool for generating **hook wordlists** to improve fuzzing accuracy. It takes a main word as input and creates a shuffled list of numbers and repetitions of that word, saving the output to a file.

---

## Features

- Generates a hook wordlist based on a main word.
- Mixes the main word with numerical sequences for more effective fuzzing.
- Outputs the result to `hook.txt`.

---

## Installation

Make sure you have **Python 3** installed. Then simply clone or download this script.

```bash
git clone <your-repo-url>
cd hookWord
```
No additional dependencies are required.

## Usage
Run the script with the -w flag to specify the main word:
```python3
python hookWord.py -w <main_word>
```
#### example:
```python3
python hookWord.py -w main
```
the output is going to be somthing like this 

```
0
main
10
30
50
...
main
```

---
*** Created By:*** NakuTenshi


