import time
activities = {}
activity = ""

def getMinutesSeconds(seconds):
    minutes = int(seconds / 60)
    seconds = int(seconds % 60)
    return [minutes, seconds]

def help():
    print("Add a new timer by typing 'new' and follow the instructions.")
    print("To finish your activity type 'finish'. ")
    print("To see your times today type 'today'. ")

def main():
    while True:
        startTime = time.time()
        cmd = input("> ")
        
        if cmd == "help":
            help()
        

        if cmd == "new":
            print("What are you doing?")
            activity = input("> ")
            print("Started the TimeTracker")
            startTime = time.time()

        if cmd == "finish":
            finishTime = time.time()
            finalTime = finishTime - startTime
            converted = getMinutesSeconds(finalTime)
            formattedTime = "{}:{}".format(converted[0], converted[1])
            try:
                activities[activity] += finalTime
            except:
                activities.update({activity : formattedTime})
            print("You were doing {} for {} minutes.".format(activity, formattedTime))
            
        if cmd == "today":
            if activities == {}:
                print("You haven't tracked something yet.")
            else:
                for key in activities:
                    val = activities[key]
                    print("You were doing {} for {} minutes today.".format(key, val))
            
help()
main()