counts={'a':1,'b':2}
lst=[]
print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )