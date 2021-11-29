import time

def findEOF(moodFile):
    i = 0
    while(moodFile.read(1) != '-'):
        i += 1

    return i

moodFile = open("mood.txt", "r+")

currentTime = time.gmtime()

moodRating = input("How are you feeling today? (1-10): ")
notes = input("Anything to say? Type it here: ")

moodFile.seek(findEOF(moodFile))
moodFile.write("\n" + str(currentTime.tm_year) + '/' + str(currentTime.tm_mon) + '/' + str(currentTime.tm_mday) + "\n")
moodFile.write("Rating: " + str(moodRating) + "\nNotes: " + str(notes) + '\n-\n')

