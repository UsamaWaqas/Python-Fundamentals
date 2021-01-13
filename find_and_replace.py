string = " he is beautiful and he is a good crickter"
print(string.replace("is","was", 1))
print(string.replace("is","was", 2))



# fine method
pos1=string.find("is")
pos2=string.find("is",pos1)
print(string.find("is", pos1+1))