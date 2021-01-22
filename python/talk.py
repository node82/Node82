import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 25) 
voices = engine.getProperty('voices')        #getting details of current voice
engine.setProperty('voice', voices[0].id)    #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#engine.say(" That I want it that way                 Tell me why              Ain't nothin' but a heartache                 Tell me why             Ain't nothin' but a mistake          Tell me why     I never wanna hear you say        I               Want         It            That             Way")
engine.save_to_file('So oh-oh, oh-oh, oh-oh, oh-oh, oh-oh You need to calm down, you are being too loud', 'ohno.mp3')
engine.runAndWait()
