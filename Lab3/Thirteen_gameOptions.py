'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
          >start
           Car had already started!!
        > stop
          Car stopped..
          >stop
           Car had already stopped!!
        > quit
'''
while True:
    options = input("Type help/start/stop/quit : ")
    if options == "start":
        print("Car started .... Ready to go !")
        options1 = input("Type help/start/stop/quit : ")
        if options1 == "start":
            print("Car had already started !!")
    elif options == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif options == "stop":
        print("Car stopped ..")
        options1 = input("Type help/start/stop/quit : ")
        if options1 == "stop":
            print("Car had already stopped !!")
    elif options == "quit":
        break
    else:
        print("I don't understand this")

"""
def opt():  # for repeated stop
    options = input("Type help/start/stop/quit : ")
    if options == "stop":
        print("Car had already stopped !!")
    elif options == "start":
        print("Car started...")
        opt2()
    elif options == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif options == "quit":
        print("")
    else:
        print("I don't understand this")

def opt2():   # for repeated start
    options = input("Type help/start/stop/quit : ")
    if options == "stop":
        print("Car had already stopped !!")
        opt()
    elif options == "start":
        print("Car started... Ready to go !")
    elif options == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif options == "quit":
        print("")
    else:
        print("I don't understand this")
while True:
    options = input("Type help/start/stop/quit : ")
    if options == "start":
        print("Car started .... Ready to go !")
        opt2()
    elif options == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif options == "stop":
        print("Car stopped ..")
        opt()
    elif options == "quit":
        break
    else:
        print("I don't understand this")
        """
