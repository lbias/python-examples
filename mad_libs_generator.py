def mad_input() :
    print("Welcome to Mad Libs, I garantee you that you will spend a great time. \n")

    name = raw_input("Enter a Name:")
    location = raw_input("Enter a Location:")
    adjective_er = raw_input("Enter an Adjective ending in ER:")
    adjective = raw_input("Enter an Adjective:")

    print ('''%s entered the cave, never before had they felt so scared. Yet, they knew all of %s was/
     counting on them, so they had to venture forward. As they progressed, they felt as if the cave was/
     getting %s and %s''' % (name,location,adjective_er,adjective))


mad_input()
