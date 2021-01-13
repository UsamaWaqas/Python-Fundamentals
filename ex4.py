name ,char =input("enter comma separated Name and character:").split(",")
print(f"lenght of your name is:{len(name)}")
print(f"character count : {name.lower().count(char.lower())}")
