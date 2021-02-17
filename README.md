# Computability - Turing machine runner
### Script created by: Martan van der Straaten

## Usage
1. Add a state:
```python
q0 = state(0, transitions = [])
``` 
2. Add transitions to the state:
```python
q0.add_transition("B", (1, "B", "R") )
``` 
3. For each transition the first argument is the letter which does the parsing, and the second argument is a tuple.
The tuple contains three parts: 1. The next state, 2. the new symbol on the tape and 3. the movement of the tapehead.

4. Repeat this for every state and its transitions

5. Define your set of states
```python
states = [q0,q1,q2,q3,q4,q5,q6,q7]
``` 

6. Possibly set an input for your tape, depending on whether you want to manually test, or you want to use the test function later defined.
```python
inp = "aaaabbbbcccc"
``` 

7. Define Three functions:
```python
def random_w(alphabet, length):

def random_correct_w(alphabet, length):

def is_really_false(word):
``` 
The first should generate a random word from the alphabet with word.length = length.
The second should generate a random word from the alphabet with word.length = length, that should be accepted by the machine.
The third should check for a given word if it should be accepted.

8. Call a function from the created machine. For example:
```python
M.test(random_w, random_correct_w, is_really_false)
```
Which will use the functions we have defined to create several thousands of testcases and print the results to a file.

Other methods are:
```python
M.eval()
M.run()
```
Both of these require input on the tape to be set in (6), and will return their obvious output depending on that.