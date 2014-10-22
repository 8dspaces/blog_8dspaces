def split_string(source, splitlist):
    output = ['']
    split = False    
    for char in source:

        if char in splitlist:
            split = True 
        else:
            if split == True:
                output.append("")
                split = False 
            output[-1] = output[-1] + char
            
            
    return output 
    
str = "This is a, my testing,and#exit"
splitlist = [' ',',','#']

print split_string(str, splitlist)