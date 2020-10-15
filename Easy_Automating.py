import pywhatkit as pt

# To search anything on "You-Tube"
pt.playonyt("Born to shine")

# Will open a tutorial on how to use this library on YouTube in respective language
pt.watch_tutorial_in_English()
pt.watch_tutorial_in_Hindi()

# To send anyone one Whatsapp message
pt.sendwhatmsg("+919123297586", 'I am sending this message using my laptop', 1, 22)

# This will perform a Google search about Python
pt.search("Machine-Learning")

# Will show information of all the messages sent using this library
pt.showHistory()

# Will shutdown the system in 100 seconds
pt.shutdown(time=100)

# Will cancel the scheduled shutdown
pt.cancelShutdown()

# For more information
pt.help()
