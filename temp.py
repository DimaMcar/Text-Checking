from copy import copy

def is_copy(source, target):
    for i, symbol in enumerate(source):
        test = copy(source)
        test[i:i] = [symbol]
        if test == target:
            return symbol
        print(test)
        
    return False 

def is_merge(source, target):
    return is_copy(target,source)
    """
    for i, symbol in enumerate(target, 1):
        if i<len(target) and symbol == target[i]: 
            test = copy(target)
            del test[i]        
            if test == source:
                return True
        
            print(test)
        
    return False     
    """
def is_move(source, target):
    for i, symbol in enumerate(source[1:], 1):
        print (symbol)

        for k in range(i):
            test = copy(source)
            del test[i]
            test[k:k] = [symbol]
            print (test)
            if test == target:
                return symbol 
    return False
    
    
def solution(S, T):
    if S == T: return "EQUAL"
    source = list(S)
    target = list(T)
    
    result = is_copy(source, target)
    if result: return "COPY "+result
    
    result = is_merge(source, target)
    if result: return "MERGE "+result
    
    result = is_move(source, target)
    if result: return "MOVE "+result
    
    
    return is_move(source,target)

print(solution("bac","abc"))
print(solution("acb","abc"))
print(solution("bac","abc"))
print(solution("abc","abc"))
   
        
        
   

