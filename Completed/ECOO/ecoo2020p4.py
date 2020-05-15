import sys
input = sys.stdin.readline

tc = int(input().rstrip())
            
for _ in range(tc):
    commands = {}
    inCommand = True
    command = []
    cname = []
    num = 0
    
    def doCommands(cmd):
        global commands, cname, command, depth, num
        cmd = cmd.split(";")
        for i in cmd:
            if i == "": continue
            c = i.split(" ")
            if len(c) < 2:
                if len(cname) > 1:
                    for i in range(len(command)):
                        command[i] += "END;"
                    commandName = cname.pop()
                    commands[commandName] = command.pop()
                else:
                    commandName = cname.pop()
                    commands[commandName] = command.pop()
            else:
                arg, val = c
                if arg == "ADD":
                    if len(cname) == 0:
                        num += int(val)
                    else:
                        for i in range(len(command)):
                            command[i] += "ADD " + val + ";"
                        
                elif arg == "MULT":
                    if len(cname) == 0:
                        num *= int(val)
                    else:
                        for i in range(len(command)):
                            command[i] += "MULT " + val + ";"
                elif arg == "SUB":
                    if len(cname) == 0:
                        num -= int(val)
                    else:
                        for i in range(len(command)):
                            command[i] += "SUB " + val + ";"
                elif arg == "FUN":
                    if len(cname) == 0:
                        cname.append(val)
                        command.append("")
                    else:
                        for i in range(len(command)):
                            command[i] += "FUN " + val + ";"
                        cname.append(val)
                        command.append("")
                elif arg == "CALL":
                    if len(cname) == 0:
                        doCommands(commands[val])
                    else:
                        for i in range(len(command)):
                            command[i] += "CALL " + val + ";"
            
    instruct= int(input().rstrip())
    for __ in range(instruct):
        doCommands(input().rstrip())

    sys.stdout.write(str(num%1000000007) + "\n")
        
            
                
                
