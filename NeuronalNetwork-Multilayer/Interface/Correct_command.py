def correct_command(command, commands_mapping):
    percents = {}
    max_percent = 0
    probable_cm = []

    for i in commands_mapping:
        percents[i] = 0

        # Len letters test - 1/5
        cm_likeness = [x for x in command if x in i]
        percent = (len(cm_likeness) / len(i)) * 100
        percent = 100 - abs(100 - percent)
        percents[i] += percent
        
        
        # Likness test - 2/5
        cm_likeness = [command[0:n] for n in range(len(command)+1) if command[0:n] in i[0:n]]
        percent = (len(cm_likeness[-1]) / len(i)) * 100
        percent = 100 - abs(100 - percent)
        percents[i] += percent
        

        # Likness reverse test - 3/5
        cm_likeness = [command[::-1][0:n] for n in range(len(command)+1) if command[::-1][0:n] in i[::-1][0:n]]
        percent = (len(cm_likeness[-1]) / len(i)) * 100
        percent = 100 - abs(100 - percent)
        percents[i] += percent
        

        # Words test 4/5
        cm_likeness = command.split("_")
        percent = (len(i.split("_")) / len(cm_likeness)) * 30
        percent = 30 - abs(30 - percent)
        percents[i] += percent
        
        
        # Len compare test 5/5
        percent = (len(command) / len(i)) * 70
        percent = 100 - abs(100 - percent)
        percents[i] += percent
        
        
        percents[i] = percents[i] / 4

        if max_percent < percents[i]:
            max_percent = percents[i]
            probable_cm.append(i)
    
    return probable_cm[-1], percents[probable_cm[-1]]