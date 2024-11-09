gVar=100
def g_l_var():
    global gVar
    lVar=200
    gVar=500
    print("lVar is:",lVar)
    print("gVar is:",gVar)
g_l_var()
print("After func call:")
print("GVar is:",gVar)
print("lVar is:",lVar)
