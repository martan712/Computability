import sys
import random

sys.setrecursionlimit(15000)

class tester:
    m = 0
    
    def __init__(self, machine):
        self.m = machine
            
    def test(self, random_word, random_word_correct, is_really_false):
            all_succes = True

            test_case = 0
            for i in range(2, 25,2):
                for j in range(i*5):
                    s = random_word_correct(["a","b"], i)
                    test_case +=1
                    f.write(f"Testcase: {test_case}\n")
                    f.write(f"WORD: {s}\n")
                    newtape = "B"+s+"B"
                    self.m.set_tape(newtape)
                    
                    ev = self.m.eval()
                    f.write(f"success: {ev}\n\n")
                    if(not ev):
                        print(f"{M.tape}= {ev}")
                        all_succes = False

            f.write(f"Should all fail!\n")

            for i in range(25):
                for j in range((i+1)*25):
                    s = random_word(["a","b"], i)
                    test_case +=1
                    f.write(f"Testcase: {test_case}\n")
                    f.write(f"WORD: {s}\n")
                    newtape = "B"+s+"B"
                    self.m.set_tape(newtape)

                    ev = self.m.eval()
                    f.write(f"success: {ev}\n\n")
                    if(ev and is_really_false(s)):
                        print(f"Testcase {test_case} might be wrong: {M.tape}= {ev}")
                        
                        all_succes = False
            if all_succes:
                print("all tests seem to have completed succesfully")

class machine:
    tape = ""
    head = 0
    states = []
    start_state = 0
    t = 0

    def __init__(self,tape, head, states, start_state):
        self.tape   = tape
        self.head   = head
        self.states = states
        self.t = tester(self)

    def eval(self):
        return states[self.start_state].evaluate(self.tape,self.head,self.states)

    def run(self):
        states[self.start_state].run(self.tape,self.head,self.states)

    def test(self, r, r_correct, really_false):
        self.t.test(r, r_correct, really_false)
        
    def set_tape(self, newtape):
        self.tape=newtape

class state:
    transitions=[]
    current = 0
    final_state=False
    
    def __init__(self, c, transitions=[], final_state = False):
        self.transitions = transitions
        self.current = c
        self.final_state = final_state

    def show_string(self,newtape, head):
        intermediate = newtape.copy()
        intermediate.insert(head, "q"+str(self.current))
        return ''.join(intermediate)+"\n"
        
    def run(self, tape, head, states):
        for (token, function) in self.transitions:
            if(tape[head] == token):
                n, t, m = function
                
                newtape = list(tape)
                print(self.show_string(newtape, head))
                newtape[head] = t
                
                if(m == "R"):
                    head+=1
                else:
                    head-=1

                if(newtape[len(newtape)-1]!="B"):
                    newtape.append("B")
                    
                tape = ''.join(newtape)
                states[n].run(tape, head, states)
                return
            
        newtape = list(tape)
        print(self.show_string(newtape, head))

    def evaluate(self, tape, head, states):
        for (token, function) in self.transitions:
            if(tape[head] == token):
                n, t, m = function
                
                newtape = list(tape)
                f.write(self.show_string(newtape, head))
                newtape[head] = t
            
                if(m == "R"):
                    head+=1
                else:
                    head-=1
                
                if(newtape[len(newtape)-1]!="B"):
                    newtape.append("B")
                    
                tape = ''.join(newtape)
                return states[n].evaluate(tape, head, states)

        f.write(self.show_string(list(tape), head))
        return self.final_state
        
    def add_transition(self, token, function):
        self.transitions.append( (token,function))






################### EDIT FROM HERE ON! ###################


#STATE MACHINE
q0 = state(0, transitions = [])
q0.add_transition("B", (1, "B", "R") )

q1 = state(1, transitions = [])
q1.add_transition("a", (2, "X", "R"))
q1.add_transition("b", (3, "Y", "R"))
q1.add_transition("X", (1, "X", "R"))
q1.add_transition("Y", (1, "Y", "R"))
q1.add_transition("B", (7, "B", "L"))

q2 = state(2, transitions = [])
q2.add_transition("a", (2, "a", "R"))
q2.add_transition("b", (2, "b", "R"))
q2.add_transition("Y", (2, "Y", "R"))
q2.add_transition("X", (2, "X", "R"))
q2.add_transition("B", (4, "B", "L"))

q3 = state(3, transitions = [])
q3.add_transition("a", (3, "a", "R"))
q3.add_transition("b", (3, "b", "R"))
q3.add_transition("Y", (3, "Y", "R"))
q3.add_transition("X", (3, "X", "R"))
q3.add_transition("B", (5, "B", "L"))

q4 = state(4, transitions = [])
q4.add_transition("Y", (4, "Y", "L"))
q4.add_transition("X", (4, "X", "L"))
q4.add_transition("a", (6, "X", "L"))
q4.add_transition("B", (7, "B", "R"))

q5 = state(5, transitions = [])
q5.add_transition("Y", (5, "Y", "L"))
q5.add_transition("X", (5, "X", "L"))
q5.add_transition("b", (6, "Y", "L"))
q5.add_transition("B", (7, "B", "R"))

q6 = state(6, transitions = [])
q6.add_transition("a", (6, "a", "L"))
q6.add_transition("b", (6, "b", "L"))
q6.add_transition("Y", (6, "Y", "L"))
q6.add_transition("X", (6, "X", "L"))
q6.add_transition("B", (1, "B", "R"))

q7 = state(7, transitions = [], final_state = True)

#SET OF ALL STATES
states = [q0,q1,q2,q3,q4,q5,q6,q7]

#VARIABLES (NO NEED TO CHANGE FOR TEST, ONLY FOR MACHINES THAT GENERATE!)
inp = "aaaabbbbcccc"
head = 0
tape = "B"+str(inp)+"B"

#OPEN FILE FOR OUTPUT OF TEST CASES
f = open("14a/output.txt", "w+")

#CREATE MACHINE
M = machine(tape, head, states, q0)


#FUNCTIONS REQUIRED FOR TEST (REDEFINE THESE FOR YOUR MACHINE

#RANDOM WORD FROM ALPHABET
def random_w(alphabet, length):
    word=""
    for i in range(length):
        index = random.randrange(0,len(alphabet))
        word+=alphabet[index]
    return word

#RANDOM WORD FROM ALPHABET THAT IS CORRECT FOR THIS MACHINE
def random_correct_w(alphabet, length):
    word=""

    word = "a"*int(length/3)+"b"*int(length/3)+"a"*int(length/3)
    return word

#CHECKS IF A GIVEN WORD SHOULD NOT BE ACCEPTED
def is_really_false(word):
    for i in range(int(len(word)/2)):
        if (word[i]!=word[len(word)-1-i]):
            return True
    return False
                    
    if(all_succes):
        print("All tests succeeded")


#EXECUTE MACHINE
M.test(random_w, random_correct_w, is_really_false)

f.close()
