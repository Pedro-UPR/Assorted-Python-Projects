programLoop = 1

while programLoop == 1:
    
    print('\nFrom what format are you converting?')
    print('A • Seconds')
    print('B • Minutes')
    print('C • Hours\n')
    userInput = input()

    if userInput.upper() == 'A': # Seconds to H:M:S
        
        timeInSeconds = int(input('\nEnter the amount of seconds: '))
        hours = timeInSeconds // 3600
        minutes = (timeInSeconds // 60) % 60
        seconds = timeInSeconds % 60
        print('\nThe amount of time is:',hours,':',minutes,':',seconds)
        
    elif userInput.upper() == 'B': # Minutes to H:M:S
        
        timeInMinutes = float(input('\nEnter the amount of minutes: '))
        hours = int(timeInMinutes) // 60
        minutes = int(timeInMinutes) % 60
        seconds = int((timeInMinutes * 60) % 60)
        print('\nThe amount of time is:',hours,':',minutes,':',seconds)
        
    elif userInput.upper() == 'C':  # Hours to H:M:S
        
        timeInHours = float(input('\nEnter the amount of hours: '))
        hours = int(timeInHours)
        minutes = int((timeInHours * 60) % 60)
        seconds = int((timeInHours * 3600) % 60)
        print('\nThe amount of time is:',hours,':',minutes,':',seconds)

    else: print('\nThat\'s not a valid character!')

    continueLoop = 1

    while continueLoop == 1:
        continuePrompt = input('\nDo you wish to continue? Y/N ')

        if continuePrompt.upper() == 'Y': continueLoop = 0
        elif continuePrompt.upper() == 'N': continueLoop = 0; programLoop = 0
        else: print('\nThat\'s not a valid character!')

print('\nThank you for using!')

    

        
