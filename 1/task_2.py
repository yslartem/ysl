ms = float((input("Distance in meters:\n")))
cms = float((input("Distance in cms:\n")))
cmsinms = cms * 100
if cmsinms > ms:
    print ("Shortest distance: ", ms)
else:
    print ("Shortest distance: ", cmsinms)