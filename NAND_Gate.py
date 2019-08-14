def NAND(A, B):
    nand = 0
    
    if A > 0 and B > 0:
        nand = 1
    else: 
        nand = 0
    
    if nand > 0:
        nand = 0
    else:
        nand = 1
        
    print(str(nand))


NAND(0,0)
NAND(1,0)
NAND(0,1)
NAND(1,1)