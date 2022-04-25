import pymysql

# helper functions


def all_kdramas(cursor):
    # prints all the kdramas in database
    print('viewing all kdramas in database...')
    dramas = 'SELECT * FROM kdramas'
    try:
        cursor.execute(dramas)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (dramas, e.args[0], e.args[1]))
        exit()


def all_directors(cursor):
    # prints all directors in database
    print('viewing all directors in database...')
    directors = 'SELECT * FROM director'
    try:
        cursor.execute(directors)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (directors, e.args[0], e.args[1]))
        exit()


def all_writers(cursor):
    # prints all writers in database
    print('Viewing all writers in database...')
    writers = 'SELECT * FROM writer'
    try:
        cursor.execute(writers)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (writers, e.args[0], e.args[1]))
        exit()


def all_actors(cursor):
    # prints all actors in database
    print('Veiwing all actors in database...')
    actors = 'SELECT * FROM actors'
    try:
        cursor.execute(actors)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (actors, e.args[0], e.args[1]))
        exit()


def all_reviews(cursor):
    # prints all reviews in database
    print('viewing all reviews in database...')
    reviews = 'SELECT * FROM user_reviews'
    try:
        cursor.execute(reviews)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (reviews, e.args[0], e.args[1]))
        exit()


try:
    user = input('Enter in your username: ')
    password = input('Enter in your password: ')
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
      '(1)add a new kdrama to the database\n' # HELP
      '(2)add a review of a kdrama\n'
      '(3)add an award' # HELP
      '(4)update kdrama information\n' # HELP
      '(5)update a review\n'
      '(6)update awards\n' # HELP
      '(7)delete a kdrama\n' 
      '(8)delete a review\n'  
      '(9)see all kdramas available\n'
      '(10)see all staff\n'
      '(11)see all reviews\n'
      '(12)select kdramas through filters\n'
      '(13)view everything' # HELP
      '(13)quit program')

menu = input('Choose a menu option: ')
keepRunning = True
while keepRunning:
    if menu == 1:
        # WHAT ABOUT TAGS + MUST GET A PROCEDURE ??!?!?!?
        print('add a new kdrama to the database')
        title = input('Type in name of kdrama: ')
        print('If you do not know the following information, type in NULL')  # change to ""
        airDate = input('Type in the date drama first aired in YYYY-MM-DD format: ')
        rating = input('Type in the drama\'s rating from 1 - 10 : ')
        year = input('Type in the year the drama was released: ')
        num_eps = input('Type in the number of episodes the drama had: ')
        synop = input('Type in the dramas synopsis: ')
        station = input('Type in the station the drama aired on :')
        know_dir = input('Type YES if you know the director of the drama: ')
        if know_dir == 'YES':
            dir_name = input('Type in the name of the director: ')
            dir_birth = input('Type in the director\'s birthday or press enter: ')
            # CREATE DIRECTOR PROCEDURE
            # USING DIR ID MAKE THE DRAMA PROCEDURE
        else:
            print('hi')
            # DRAMA PROCEDURE IS MADE AND HAS THE DIRECTOR ID BE NULL
        know_wri = input('Type YES if you know the writer of the drama: ')
        if know_wri == 'YES':
            wri_name = input('Type in the writer\'s name: ')
            wri_birth = input('Type in the writer\'s birthday in YYYY-MM-DD format or press enter: ')
            # CREATE WRITER PROCEDURE
            # THEN CREATE WRITER-DRAMA TABLE PROCEDURE W/ DRAMA_ID
        know_act = input('Type YES if you know the 2 actors and their characters')
        if know_act == 'YES':
            act_1_name = input('Type in the actor\'s name: ')
            act_1_birth = input('Type in the actor\'s birthday in YYYY-MM-DD format or press enter: ')
            act_1_desc = input('Type in the decription of the actor: ')
            # CREATE ACTOR PROCEDURE AND GET ACTOR ID
            char_1_name = input(f'Type in the {act_1_name}\'s character\'s name: ')
            char_1_role = input('Type in the character\'s role')
            # GET THE DRAMA ID
            # CREATE CHARACTER PROCEDURE
            act_2_name = input('Type in the actor\'s name: ')
            act_2_birth = input('Type in the actor\'s birthday in YYYY-MM-DD format or press enter: ')
            act_2_desc = input('Type in the decription of the actor: ')
            # CREATE ACTOR PROCEDURE AND GET ACTOR ID
            char_2_name = input(f'Type in the {act_1_name}\'s character\'s name: ')
            char_2_role = input('Type in the character\'s role')
            # GET THE DRAMA ID
            # CREATE CHARACTER PROCEDURE
        else:
            # make the new kdrama
            # need to make sure that for NULLS we dont actually type in string null but actual null
            print('hi')
        print('adding kdrama to database...')

    if menu == 2:
        print('add a new kdrama review')
        add_review = input('Type in your review here: ')
        add_num_users = input('Type in the number of users it helped: ')
        add_kid = input('Type in the drama\' title: ')
        add_uid = input('Type in your user id: ')
        add_overall = input('Type in your overall rating of the drama: ')
        add_story = input('Type in your story rating of the drama: ')
        add_acting = input('Type in your acting rating of the drama: ')
        add_music = input('Type in your music rating of the drama: ')
        add_rewatch = input('Type in your rewatch rating of the drama: ')
        # USING ALL OF THIS DATA ADD_REVIEW_PROCEDURE
        # must have converted drama title to id
        # if id does not exist, then cancel procedure
        print('adding review to database...')

    if menu == 3:
        print('add an award')

    if menu == 4:
        print('update information of kdrama')
        up_drama = input('Type in the drama you wish to update: ')
        # select drama and show its information
        # ask to rewrite the entire data again?
        select = f'SELECT * FROM kdrama WHERE drama_title = \'{up_drama}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        up_title = input('Update the title of the drama: ')
        up_rating = input('Update the rating of the drama: ')
        up_num_eps = input('Update the number of episodes: ')
        up_synop = input('Update the drama\'s synopsis: ')
        up_station = input('Update the station the drama airs on: ')
        # SHOULD WE ALLOW THEM TO UPDATE THE STAFF??!?!?!

    if menu == 5:
        print('update information of review')
        # how do we figure out what review they want to update?
        # combine the user id and drama title
        up_rid = input('What is the review id: ')
        select = f'SELECT * FROM user_reviews WHERE rid = \"{up_rid}\"'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        # after printing the current version of the review how will we update
        up_review = input('Update the review: ')
        up_helper = input('Update how many users review has helped: ')
        up_choice = input('Do you want to update the rating as well? (Type in YES or NO): ')
        if up_choice == 'YES':
            up_overall = input('Update the overall rating: (Type in number 1 - 5): ')
            up_story = input('Update the story rating: (Type in number 1 - 5): ')
            up_acting = input('Update the actors rating: (Type in number 1 - 5): ')
            up_music = input('Update the music rating: (Type in number 1 - 5): ')
            up_rewatch = input('Update the rewatch value: (Type in number 1 - 5): ')

            # INSERT PROCEDURE HERE
            # takes in rid, review, num_helped, 5 ratings
        else:
            # INSERT PROCEDURE HERE
            # takes in rid, review, num_helped
            print(f'updating review number\'{up_rid}\'')

    if menu == 6:
        print('update awards')
        # we might have to fix awards db... its only for drama when staff are now getting awards

    if menu == 7:
        # prints all dramas first, so that user can choose
        all_kdramas(cur)
        print('Delete a drama')
        del_drama = input('Type in the title of the drama you wish to delete: ')
        select = f'SELECT * FROM kdrama WHERE drama_title = \'{del_drama}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        del_confirm = input('Type YES to confirm that you wish to delete this drama: ')
        if del_confirm == 'YES':
            # DELETE DRAMA PROCEDURE
            print(f'Deleting {del_drama}...')
        else:
            print('Going back to main menu...')

    if menu == 8:
        # print all reviews first, so that user can choose
        all_reviews(cur)
        print('Delete a review')
        del_review = input('Type in the review id of the review you want to delete: ')
        select = f'SELECT * FROM user_reviews WHERE rid = \'{del_review}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        del_confirm = input('Type YES to confirm that you wish to delete this review: ')
        if del_confirm == 'YES':
            # DELETE REVIEW PROCEDURE
            print(f'Deleting review {del_review}...')
        else:
            print('Going back to main menu...')

    if menu == 9:
        all_kdramas(cur)

    if menu == 10:
        print('viewing all staff in database...')
        all_actors(cur)
        all_directors(cur)
        all_writers(cur)

    if menu == 11:
        all_reviews(cur)

    if menu == 12:
        print('searching through kdrama database')
        print('Do you want to search through:'
              '(1)kdramas'
              '(2)actors'
              '(3)return to menu')
        fil_menu = input('Choose a menu option: ')
        if fil_menu == 1:
            print('Do you want to find kdrama\'s through:'
                  '(1)title'
                  '(2)actor'
                  '(3)year'
                  '(4)station'
                  '(5)rating')
            dra_menu = input('Choose a menu option: ')
            if dra_menu == 1:
                fil_title = input('Type in a title: ')
                # FIND PROCEDURE
                # given title input return dramas with the input in the title,
                # it doesn't even have to be exact
                # when returning the procedures: it must show drama info, actors, and drama awards
            if dra_menu == 2:
                fil_actor = input('Type in an actor: ')
                # FIND PROCEDURE
                # IF ACTOR EXISTS- PRINT THEIR INFO + AWARDS
                # PRINT ALL DRAMAS THAT EXIST with same info as above
            if dra_menu == 3:
                fil_year = input('Type in a year: ')
                # FIND PROCEDURE
                # all dramas that aired that year
            if dra_menu == 4:
                fil_station = input('Type in a station: ')
                # FIND PROCEDURE
                # all dramas with that station
            if dra_menu == 5:
                fil_rating = input('Type in a rating from 1 to 10: ')
                # FIND PROCDURE
                # all dramas with that rating
            print('Returning to previous menu...')
        if fil_menu == 2:
            print('Do you want to find actor\'s through:'
                  '(1)name'
                  '(2)dramas'
                  '(3)year')
            act_menu = input('Choose a menu option: ')
            if act_menu == 1:
                fil_name = input('Type in the name of the actor: ')
                # FIND PROCEDURE RETURN ALL DATA OF ACTOR + AWARDS
                # could even be partial of a name and others can appear
            if act_menu == 2:
                fil_drama = input('Type in a drama: ')
                # FIND PROCEDURE takes in drama title
                # return drama info + actors in + actor awards
                # could  also be a portion of the title that fits
            if act_menu == 3:
                fil_ayear = input('Type in a year: ')
                # FIND PROCEDURE return all actors born in that year + awards
        print('Returning to previous menu...')

    if menu == 13:
        print('View everything in kdrama database')
        select = 'SELECT *' # DONT KNOW IF THIS WILL WORK
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()

    if menu == 14:
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
