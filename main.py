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
#print('hi')
print(f'Welcome {user} to our Kdrama database.')
print('Here you can:\n'
      '(1)add a new kdrama to the database\n'  
      '(2)add a review of a kdrama\n'
      '(3)add an award\n'
      '(4)update kdrama information\n'  # HELP
      '(5)update a review\n'
      '(6)update awards\n'  # HELP
      '(7)delete a kdrama\n'
      '(8)delete a review\n'
      '(9)see all kdramas available\n'
      '(10)see all staff\n'
      '(11)see all reviews\n'
      '(12)select kdramas or actor through filters\n'
      '(13)view everything\n'  # HELP
      '(14)quit program')
keepRunning = True
while keepRunning:
    menu = input('Choose a menu option: ')
    if menu == '1':
        print('add a new kdrama to the database')
        title = input('Type in name of kdrama: ')
        print('If you do not know the following information, press enter to continue')
        rating = input('Type in the drama\'s rating from 1 - 10 : ')
        year = input('Type in the year the drama was released: ')
        num_eps = input('Type in the number of episodes the drama had: ')
        synopsis = input('Type in the dramas synopsis: ')
        station = input('Type in the station the drama aired on :')
        genre = input('Type in the drama\'s genre: ')
        tag = input('Type in the drama\'s tag: ')
        know_dir = input('Type YES if you know the director of the drama: ')
        if know_dir == 'YES':
            dir_name = input('Type in the name of the director: ')

        know_wri = input('Type YES if you know the writer of the drama: ')
        if know_wri == 'YES':
            wri_name = input('Type in the writer\'s name: ')

        if know_dir == 'YES' and know_wri == 'YES':

            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', \'{dir_name}\', \'{wri_name}\', \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        if know_dir != 'YES' and know_wri == 'YES':

            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', NULL, \'{wri_name}\', \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        if know_dir == 'YES' and know_wri != 'YES':

            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', \'{dir_name}\', NULL, \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        if know_dir != 'YES' and know_wri != 'YES':

            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', NULL, NULL, \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        know_act = input('Type YES if you know the 2 actors and their characters: ')
        if know_act == 'YES':
            act_1_name = input('Type in the actor\'s name: ')
            act_1_birth = input('Type in the actor\'s birthday in YYYY-MM-DD format: ')
            act_1_desc = input('Type in the actor\'s description: ')
            char_1_name = input(f'Type in the {act_1_name}\'s character\'s name: ')
            char_1_role = input('Type in the character\'s role')
            # PROCEDURE with title, actor name, actor bday, actor description, character name, character role

            create_actor_char = f'CALL create_character_connect_actor(\'{title}\', \'{act_1_name}\',' \
                                f' \'{char_1_name}\', \'{char_1_role}\', \'{act_1_birth}\', \'{act_1_desc}\')'
            try:
                # executes the procedure
                cur.execute(create_actor_char)
            except pymysql.Error as e:
                # while loop continues and we ask user to try again
                print('SELECT failed %s Error: %d: %s' % (create_actor_char, e.args[0], e.args[1]))

            act_2_name = input('Type in the actor\'s name: ')
            act_2_birth = input('Type in the actor\'s birthday in YYYY-MM-DD format: ')
            act_2_desc = input('Type in the actor\'s description: ')
            char_2_name = input(f'Type in the {act_1_name}\'s character\'s name: ')
            char_2_role = input('Type in the character\'s role')
            # PROCEDURE with title, actor name, actor bday, actor description, character name, character role
            create_actor_char = f'CALL create_character_connect_actor(\'{title}\', \'{act_2_name}\',' \
                                f' \'{char_2_name}\', \'{char_2_role}\', \'{act_2_birth}\', \'{act_2_desc}\')'
            try:
                # executes the procedure
                cur.execute(create_actor_char)
            except pymysql.Error as e:
                # while loop continues and we ask user to try again
                print('SELECT failed %s Error: %d: %s' % (create_actor_char, e.args[0], e.args[1]))

        else:
            print('if they do not know actor and characters do we make null?')
        print('adding kdrama to database...')

    if menu == '2':
        print('add a new kdrama review')
        add_review = input('Type in your review here: ')
        add_kid = input('Type in the drama\' title: ')
        add_uid = input('Type in your username: ')
        add_rating = input('Type in your overall rating of the drama: ')

        create_review = f'CALL add_review(\'{add_review}\', \'{add_kid}\', \'{add_uid}\', {add_rating})'
        try:
            # executes the procedure
            cur.execute(create_review)
            # prints all the rows in the command line
            print("creating " + add_kid + '\'s review...')
        except pymysql.Error as e:
            # while loop continues and we ask user to try again
            print('SELECT failed %s Error: %d: %s' % (create_review, e.args[0], e.args[1]))
        print('adding review to database...')

    if menu == '3':
        print('add an award')
        drama = input('Type in the drama that won an award: ')
        title = input('Type in title of the award: ')
        year = input('Type in the year the drama won the award: ')

        create_award = f'CALL create_award(\'{drama}\', \'{title}\', {year})'
        try:
            # executes the procedure
            cur.execute(create_award)
            print("creating " + title + '\'...')
        except pymysql.Error as e:
            # while loop continues and we ask user to try again
            print('SELECT failed %s Error: %d: %s' % (create_award, e.args[0], e.args[1]))
        print('adding award to database...')

    if menu == '4':
        all_kdramas(cur)
        print('update information of kdrama')
        up_did = input('Type in the drama id you with to update')
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

    if menu == '5':
        print('update information of review')
        all_reviews(cur)
        up_rid = input('What is the review id: ')
        select = f'SELECT * FROM user_reviews WHERE rid = {up_rid}'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        # after printing the current version of the review how will we update
        up_review = input('Update the review: ')
        up_rating = input('Update the overall rating (Type in a number 1- 5): ')

        print(f'updating review number\'{up_rid}\'')

    if menu == '6':
        print('update awards')
        # we might have to fix awards db... its only for drama when staff are now getting awards
        # view all awards that also have a drama title attached to it
        up_aid = input('what is the award id you wish to update')
        up_rev_title = input('what is the title of the drama that won an award that you wish to update: ')
        # PROCEDURE that returns all the award info of dramas that pop up with given title

    if menu == '7':
        # prints all dramas first, so that user can choose
        all_kdramas(cur)
        print('Delete a drama')
        del_did = input('Type in the drama id of the drama you wish to delte: ')
        del_drama = input('Type in the title of the drama you wish to delete: ')
        select = f'SELECT * FROM kdrama WHERE drama_id = \'{del_did}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        del_confirm = input('Type YES to confirm that you wish to delete this drama: ')
        if del_confirm == 'YES':
            delete_drama = f'CALL delete_kdrama(\'{del_drama}\', \'{del_did}\')'
            try:
                # executes the procedure
                cur.execute(delete_drama)
                print(f'Deleting {del_drama}...')
            except pymysql.Error as e:
                # while loop continues and we ask user to try again
                print('SELECT failed %s Error: %d: %s' % (delete_drama, e.args[0], e.args[1]))
        else:
            print('Going back to main menu...')

    if menu == '8':
        # print all reviews first, so that user can choose
        all_reviews(cur)
        print('Delete a review')
        del_review = input('Type in the review id of the review you want to delete: ')
        select = f'SELECT * FROM user_reviews WHERE rid = {del_review}'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()
        del_confirm = input('Type YES to confirm that you wish to delete this review: ')
        if del_confirm == 'YES':

            delete_review = f'CALL delete_review({del_review})'
            try:
                # executes the procedure
                cur.execute(delete_review)
                # prints all the rows in the command line
                print("deleting review " + del_review + '...')
            except pymysql.Error as e:
                # while loop continues and we ask user to try again
                print('SELECT failed %s Error: %d: %s' % (delete_review, e.args[0], e.args[1]))
            print('deleting review from database...')
        else:
            print('Going back to main menu...')

    if menu == '9':
        all_kdramas(cur)

    if menu == '10':
        print('viewing all staff in database...')
        all_actors(cur)
        all_directors(cur)
        all_writers(cur)

    if menu == '11':
        all_reviews(cur)

    if menu == '12':
        print('searching through kdrama database')
        print('Do you want to search through:'
              '(1)kdramas'
              '(2)actors'
              '(3)return to menu')
        fil_menu = input('Choose a menu option: ')
        if fil_menu == '1':
            print('Do you want to find kdrama\'s through:'
                  '(1)title'
                  '(2)actor'
                  '(3)year'
                  '(4)station'
                  '(5)rating')
            dra_menu = input('Choose a menu option: ')
            if dra_menu == '1':
                fil_title = input('Type in a title: ')
                # FIND PROCEDURE
                # given title input return dramas with the input in the title,
                # it doesn't even have to be exact
                # when returning the procedures: it must show drama info, actors, and drama awards
            if dra_menu == '2':
                fil_actor = input('Type in an actor: ')
                # FIND PROCEDURE
                # IF ACTOR EXISTS- PRINT THEIR INFO + AWARDS
                # PRINT ALL DRAMAS THAT EXIST with same info as above
            if dra_menu == '3':
                fil_year = input('Type in a year: ')
                # FIND PROCEDURE
                # all dramas that aired that year
            if dra_menu == '4':
                fil_station = input('Type in a station: ')
                # FIND PROCEDURE
                # all dramas with that station
            if dra_menu == '5':
                fil_rating = input('Type in a rating from 1 to 10: ')
                # FIND PROCDURE
                # all dramas with that rating
            print('Returning to previous menu...')
        if fil_menu == '2':
            print('Do you want to find actor\'s through:'
                  '(1)name'
                  '(2)dramas'
                  '(3)year')
            act_menu = input('Choose a menu option: ')
            if act_menu == '1':
                fil_name = input('Type in the name of the actor: ')
                # FIND PROCEDURE RETURN ALL DATA OF ACTOR + AWARDS
                # could even be partial of a name and others can appear
            if act_menu == '2':
                fil_drama = input('Type in a drama: ')
                # FIND PROCEDURE takes in drama title
                # return drama info + actors in + actor awards
                # could  also be a portion of the title that fits
            if act_menu == '3':
                fil_ayear = input('Type in a year: ')
                # FIND PROCEDURE return all actors born in that year + awards
        print('Returning to previous menu...')

    if menu == '13':
        print('View everything in kdrama database')
        select = 'SELECT *'  # DONT KNOW IF THIS WILL WORK
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))
            exit()

    if menu == '14':
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
