import scrape
import random

# create a dictionary from the scraped data for title and defination
terminologies = {}
title = scrape.newTitleList
defination = scrape.newDefList

for TechTerm, TechDefine in zip(title, defination):
    terminologies[TechTerm] = TechDefine

for quizNum in range(5):
    # generating the files for the questions and the answers
    quizFile = open('techQuiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('techQuizAns%s.txt' % (quizNum + 1), 'w')

    # shuffle the order of the questions
    terms = list(terminologies.keys())
    random.shuffle(terms)

    # looping throught the terminologies and creating answers
    for termsNumber in range(67):
        termsTuple = list(terminologies.items())
        # correctAnswer = terminologies[title[termsNumber]]
        correctAnswer = termsTuple[termsNumber][1]
        # creating a list of wrong answers
        wrongAnswer = list(terminologies.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)

        # write the questions to the file created
        quizFile.write('%s. What is the meaning of  %s?\n' %(termsNumber + 1, terms[termsNumber]))
        
        # display the options
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answers to a file
        answerFile.write('%s. %s\n' %(termsNumber + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerFile.close()