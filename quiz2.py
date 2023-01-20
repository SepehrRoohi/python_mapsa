user_name = input('what is your name? ')
answers = ['1', '3', '4']
total_points = 0
question_one = print(
    '''What is the diameter of the earth?
1)12,742 km
2)11,742 km
3)10,742 km
4)13,742 km'''
    )
answer_question_one = input('select: ')
if answer_question_one == answers[0]:
    total_points += 10
    print(f'score: {total_points}')
question_two = print(
    '''BMW company for which country?
1)America
2)Poland
3)Germany
4)Portugal'''
    )
answer_question_two = input('select: ')
question_three = print(
    '''How much is Elon Musk's wealth??
1)174 billion USD
2)110 billion USD
3)123 billion USD
4)148 billion USD'''
    )
answer_question_three = input('select: ')
