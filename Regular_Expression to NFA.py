j=0  #intializing the counter ro keep track of states
#k=2;
 # Class to convert the expression
class Conversion:
     
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack 
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':4, '.' :2}
     
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
     
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
     
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
     
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op) 
 
    # A utility function to check is the given character
    # is operand 
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError: 
            return False
             
    # The main function that converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
         
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand, 
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
             
            # If the character is an '(', push it to stack
            elif i  == '(':
                self.push(i)
 
            # If the scanned character is an ')', pop and 
            # output from the stack until and '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
 
        str1= ("".join(self.output))
        return str1     
# conssd

class Nfa():     #create a class of NFA   to create states

     
     def __init__(self):
          self.start=None;
          self.end=None;
          self.transaction=[]   # transaction for visited nodes // store the path// element of tranaction list is an dictinory 

     def insert(self,start,end):   #insert the initial and final state
        self.start=start
        self.end=end
     def transactionfun(self,start,end,inpu):   
        #create a dic to store  start,input and end  for a nfa
        transac={}
        transac['start']=start;
        transac['input']=inpu;
        transac['end']=end;
        self.transaction.append(transac)
        #print(self.transaction)

       
           
          
          
     
#def constructnfa(x):

# Driver program to test above function
exp = input("Enter expresion")
obj = Conversion(len(exp))
str1=obj.infixToPostfix(exp)
print(str1)
stack=[]       #to push states in the stack
def union(op,op2):
     
     ''' for union  create 2 new states and add the transcation b/w those  states'''
     news=Nfa()
     news.insert('Q'+str(j),'Q'+str(j+1))
     end=op.end
     end1=op2.end
     start=op.start;
     start1=op2.start;
    
     for i in range (0,len(op.transaction)):     #adding all the tranaction of  op
       #print( "op" ,op.transaction[i])
        news.transaction.append(op.transaction[i])
     for i in range (0,len(op2.transaction)):
         #print("oop2",op2.transaction[i])
         news.transaction.append(op2.transaction[i])   #adding other transactio of op2
    
     news.transactionfun(news.start,start,'e')
     news.transactionfun(news.start,start1,'e')
     news.transactionfun(end,news.end,'e')
     news.transactionfun(end1,news.end,'e')
     #print(news.start)
     #print(news.end)
     for i in news.transaction:
         print(i)
     stack.append(news)  #push new state into the stack
        
def concat(op2,op):
     '''a news nfa of concatination  no new state is required  so don't insert data .  A new nfa is created having initial state as op.satrt and final state as op2.end'''
     news=Nfa()    
     end=op.end
     end1=op2.end
     start=op.start;
     start2=op2.start;
    

     news.insert(start,end1)
     for i in range (0,len(op.transaction)):
       #print(op.transaction[i])
       news.transaction.append(op.transaction[i])
     for i in range (0,len(op2.transaction)):
         #print(op2.transaction[i])
         #pass
         news.transaction.append(op2.transaction[i])
     news.transactionfun(end,start2,'e')
     for i in news.transaction:
         #print(i)
         pass
     stack.append(news)  #push new state into the stack
     
     
def star(op):

     '''  in this create 2 new states AND  b/w the initial and final state add all the transaction of op'''
     news=Nfa()
     news.insert('Q'+str(j),'Q'+str(j+1))
     
     end=op.end
     start=op.start
     print(start,end)
     for i in range (0,len(op.transaction)):              
       news.transaction.append(op.transaction[i])
     
     news.transactionfun(news.start,start,'e')
     news.transactionfun(news.start,news.end,'e')
     news.transactionfun(end,news.end,'e')
     news.transactionfun(start,end,'e')
    
     #for i in news.transaction:
         #print(i)
     stack.append(news)   #push new state into the stack  
 
 
 
# here is we are creating the nfa chrachter by character  

for i in range(0,len(str1)):

    #print(str1[i])
    if(str1[i].isalpha()):
         # print(str1[i] , "iska onf bange")
          myobj=Nfa()   #create Nfa's of all the input symbol 
          myobj.insert('Q'+str(j),'Q'+str(j+1))
          myobj.transactionfun(myobj.start,myobj.end,str1[i]) #add the trancation b/w initial and final state
          stack.append(myobj)
          j=j+2;
          
    elif(str1[i]=="+"):   #handle union
         #print("fiubg")
         union(stack.pop(),stack.pop())   #pop two states from   stack  and perform union in it
         j=j+2;
    elif(str1[i]=="."):
         #print(len(stack))
         concat(stack.pop(),stack.pop()) #pop two states from   stack  and perform concatination in it
    elif(str1[i]=="*"):
        star(stack.pop())
        j=j+2
x=stack.pop()  #pop the final state
print("starring point is : ",x.start)
print("Ending point is :",x.end)
print("start\t  input\t end\t")
for i in x.transaction:
    print(i['start'],"\t", i['input'],"\t",i['end'],"\t")
    
         
         
         
        
    
        
        
