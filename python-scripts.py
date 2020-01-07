#Replace lines in a file
insensitive_string = re.compile(re.escape('SecureListener=true'), re.IGNORECASE)
with fileinput.FileInput("BFileName", inplace=True, backup='.ORG') as file:
    for line in file:
    print(insensitive_string.sub("SecureListener=false", line), end='')

lpattern = re.compile("ListenAddress=")
Spattern = re.compile("SecureListener=")
with fileinput.FileInput("BFileName", inplace=True, backup='.ORG') as file:
    for line in file:
        if Spattern.search(line):
            print(re.sub (r"SecureListener=*", "SecureListener=", "SecureListener=false"), end='\n')
        elif lpattern.search(line):
            print(re.sub (r"ListenAddress=*", "ListenAddress=", "ListenAddress=11111.111.111"), end='\n')
        else:
            print(line, end='\n')

#############################################################
