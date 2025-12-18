# file=open("./FileHandling.txt","r")

# # content=file.read(10)
# # line=file.readline()
# # line=file.readline()
# # line=file.readline()
# allLines=file.readlines()[2]
# print(allLines)

# file.close()


# a= "the escape char in python is \\n."

# print(a)


# file =open("./FileHandling.txt",'w') #overwriting

# sow='''Sowmya Sathyanarayana (18 July 1972 – 17 April 2004), better known by her stage name Soundarya, was an Indian actress known for her works primarily in Telugu cinema.\n[1][2] She was regarded as one of the greatest actresses in the history of Telugu cinema.[3] She also acted in a few Kannada, Tamil, Hindi and Malayalam films./n She has received three Nandi Awards, two Karnataka State Film Awards and six Filmfare Awards South.\n In 2002, she received the National Film Award for Best Feature Film as a producer for the Kannada film Dweepa.'''

# ice='''Aishwarya Rai Bachchan (born 1 November 1973) is an Indian actress who is primarily known for her work in Hindi and Tamil films.\n Rai won the Miss World 1994 pageant and later established herself as one of the most-popular and influential celebrities in India. She has received numerous accolades for her acting, including two Filmfare Awards.\n In 2004, Time magazine named her one of the 100 most influential people in the world. In 2009, the Government of India honoured her with the Padma Shri and in 2012, the Government of France awarded her with the Order of Arts and Letters.\n From the late 1990s, she has often been called "the most beautiful woman in the world".'''

# file.write(sow)

# file.close()


file =open("./FileHandling.txt",'a') #adding

sow='''Sowmya Sathyanarayana (18 July 1972 – 17 April 2004), better known by her stage name Soundarya, was an Indian actress known for her works primarily in Telugu cinema.\n[1][2] She was regarded as one of the greatest actresses in the history of Telugu cinema.[3] She also acted in a few Kannada, Tamil, Hindi and Malayalam films./n She has received three Nandi Awards, two Karnataka State Film Awards and six Filmfare Awards South.\n In 2002, she received the National Film Award for Best Feature Film as a producer for the Kannada film Dweepa.'''

ice='''\n\n\n\nAishwarya Rai Bachchan (born 1 November 1973) is an Indian actress who is primarily known for her work in Hindi and Tamil films.\n Rai won the Miss World 1994 pageant and later established herself as one of the most-popular and influential celebrities in India. She has received numerous accolades for her acting, including two Filmfare Awards.\n In 2004, Time magazine named her one of the 100 most influential people in the world. In 2009, the Government of India honoured her with the Padma Shri and in 2012, the Government of France awarded her with the Order of Arts and Letters.\n From the late 1990s, she has often been called "the most beautiful woman in the world".'''

file.write(sow)

file.close()