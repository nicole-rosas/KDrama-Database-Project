import pymysql

try:
    user = input('Enter in your username: ')
    password =  input('Enter in your password: ')
    cnx = pymysql.connect(host='localhost',
                          user=user,
                          password=password,
                          db='kdrama',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
except pymysql.Error as e:
    print("Error with logging in... try again")
    print('Error: %d: %s' % (e.args[0], e.args[1]))

cur = cnx.cursor()

print(f'Welcome {user} to our Kdrama database.')
print('Here you can:\n'
      '(1)add a new kdrama to the database\n'
      '(2)add a review of a kdrama\n'
      '(3)update kdrama information\n'
      '(4)update a review\n'
      '(5)update a rating\n'
      '(6)update awards\n'
      '(7)delete a kdrama\n'
      '(8)delete a review\n'
      '(9)see all kdramas available\n'
      '(10)see all staff\n'
      '(11)see all reviews\n'
      '(12)select kdramas through filters\n'
      '(13)quit program')

menu = input('Choose a menu option: ')
keepRunning = True
while keepRunning:
    if menu == 1:
        print('add a new kdrama to the database')
        # prompt if they know actors + character names
        #   if yes : add the 2 actors + characters
        #   if no  : dont
        # if they do not know smth then NULL
        # kdrama title, air_date, rating, year, num episodes, synopsis, station
        # WHY DIRECTOR ID
        title = input('Type in name of kdrama: ')
        print('If you do not know the following information, type in NULL')
        airDate = input('Type in the date drama first aired in YYYY-MM-DD format: ')
        rating = input('Type in the drama\'s rating from 1 - 10 : ')
        year = input('Type in the year the drama was released: ')
        num_eps = input('Type in the number of episodes the drama had: ')
        synop = input('Type in the dramas synopsis: ')
        station = input('Type in the station the drama aired on :')
        know_act = input('Type YES if you know the 2 actors and their characters')
        if know_act == 'YES':
            act_1 = input('Type in the actors name: ')
            char_1 = input('Type in their characters name: ')

            act_2 = input('Type in the actors name: ')
            char_2 = input('Type in their characters name: ')

            # make the new kdrama and actors here
            # what do we do about writers and directors?

        else:
            # make the new kdrama
            # need to make sure that for NULLS we dont actually type in string null but actual null
            print('adding kdrama to database...')

    if menu == 2:
        print('add a new kdrama review')
        review = input('Type in your review here: ')
        num_users = input('Type in the number of users it helped: ')
        kid = input('Type in the dramas id: ')
        # how are we getting user id or rating id?
        # now we use procedure to add review
        print('adding review to database')

    if menu == 3:
        print('update information of kdrama')
        up_drama = input('Which drama are you updating: ')
        # select drama and show its information
        # ask to rewrite the entire data again?
        select = f'SELECT * FROM kdrama WHERE drama_title = \'{up_drama}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        # how would we go about updating? they update everything or only specifics?

    if menu == 4:
        print('update information of review')
        # how do we figure out what review they want to update?
        # combine the user id and drama title
        up_drama = input('Review of which drama: ')
        up_user = user
        select = f'SELECT * FROM user_reviews WHERE drama_id = {up_drama}= AND user_id = {up_drama}'
        # incorrect because we need to get ids not names
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        # after printing the current version of the review how will we update

    if menu == 5:
        print('update rating of drama')

    if menu == 6:
        print('update awards')
        # we might have to fix awards db... its only for drama when staff are now getting awards

    if menu == 7:
        print('delete a drama')
        # verify using select then ask them to confirm

    if menu == 8:
        print('delete a review')

    if menu == 9:
        print('viewing all kdramas in database...')
        select = 'SELECT * FROM kdramas'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
    if menu == 10:
        print('viewing all staff in database...')
        select = 'SELECT * FROM staff'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
    if menu == 11:
        print('viewing all reviews in database...')
        select = 'SELECT * FROM user_reviews'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()

    if menu == 12:
        print('filter through kdramas')
        # another menu inside where we ask for what they want to look for?

    if menu == 13:
        print('Closing out of program...')
        cnx.close()
        keepRunning = False

    else:
        print('Unexpected input. Try again.')

    # runs after every option (except 13)
    print('Here is the menu of commands:\n'
          '(1)add a new kdrama to the database\n'
          '(2)add a review of a kdrama\n'
          '(3)update kdrama information\n'
          '(4)update a review\n'
          '(5)update a rating\n'
          '(6)update awards\n'
          '(7)delete a kdrama\n'
          '(8)delete a review\n'
          '(9)see all kdramas available\n'
          '(10)see all staff\n'
          '(11)see all reviews\n'
          '(12)select kdramas through filters\n'
          '(13)quit program')


