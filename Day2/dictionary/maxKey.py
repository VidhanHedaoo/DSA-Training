#waf to find the key with the maximum value in a dictionary

dict ={"A":50,"B":30,"C":70}

maxval = max(dict,key=dict.get)

print(maxval)
