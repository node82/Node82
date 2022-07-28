import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150) 
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#engine.save_to_file('That I want it that way                 Tell me why              Ain't nothin' but a heartache                 Tell me why             Ain't nothin' but a mistake', '/tellmewhy.mp3')
engine.say('Let’s say, hypothetically, I am a barbie girl. Okay let’s even say I’m in a barbie world. Right so, in this scenario, I would obviously know from personal experience that life in plastic is fantastic. Wouldn’t it be reasonable to assume you could brush my hair and undress me literally everywhere? Imagination; you can derive from the fundamentals of basic logic that life is your creation.')
engine.runAndWait()
