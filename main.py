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


def all_directors(cursor):
    # prints all directors in database
    print('viewing all directors in database...')
    directors = 'SELECT * FROM director'
    try:
        cursor.execute(directors)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (directors, e.args[0], e.args[1]))


def all_writers(cursor):
    # prints all writers in database
    print('Viewing all writers in database...')
    writers = 'SELECT * FROM writer'
    try:
        cursor.execute(writers)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (writers, e.args[0], e.args[1]))


def all_actors(cursor):
    # prints all actors in database
    print('Veiwing all actors in database...')
    actors = 'SELECT * FROM actors'
    try:
        cursor.execute(actors)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (actors, e.args[0], e.args[1]))


def all_awards(cursor):
    # prints all the kdramas in database
    print('viewing all awards in database...')
    awards = 'SELECT * FROM drama_awards'
    try:
        cursor.execute(awards)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (awards, e.args[0], e.args[1]))


def all_reviews(cursor):
    # prints all reviews in database
    print('viewing all reviews in database...')
    reviews = 'call see_all_reviews()'
    try:
        cursor.execute(reviews)
        print(cursor.fetchall())
    except pymysql.Error as e:
        print('SELECT failed %s Error: %d: %s' % (reviews, e.args[0], e.args[1]))


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
      '(13)quit program')
keepRunning = True
while keepRunning:
    menu = input('Choose a menu option: ')
    if menu == '1': # adds a kdrama
        print('--------add a new kdrama to the database--------')
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

        if know_dir == 'YES' and know_wri == 'YES': # if user knows both then no NULL
            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', \'{dir_name}\', \'{wri_name}\', \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        if know_dir != 'YES' and know_wri == 'YES': # director is NULL
            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', NULL, \'{wri_name}\', \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        if know_dir == 'YES' and know_wri != 'YES': # writer is NULL
            create_drama = f'CALL add_kdrama(\'{title}\', {rating}, {year}, {num_eps}, ' \
                           f'\'{synopsis}\', \'{dir_name}\', NULL, \'{station}\', \'{genre}\', \'{tag}\')'
            try:
                cur.execute(create_drama)
                print("creating " + title + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_drama, e.args[0], e.args[1]))

        if know_dir != 'YES' and know_wri != 'YES': # both NULL
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

            create_actor_char = f'CALL create_character_connect_actor(\'{title}\', \'{act_1_name}\',' \
                                f' \'{char_1_name}\', \'{char_1_role}\', {act_1_birth}, \'{act_1_desc}\')'
            try:
                cur.execute(create_actor_char)
                print(f'creating {act_1_name}\'s character...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_actor_char, e.args[0], e.args[1]))

            act_2_name = input('Type in the actor\'s name: ')
            act_2_birth = input('Type in the actor\'s birthday in YYYY-MM-DD format: ')
            act_2_desc = input('Type in the actor\'s description: ')
            char_2_name = input(f'Type in the {act_1_name}\'s character\'s name: ')
            char_2_role = input('Type in the character\'s role')

            create_actor_char = f'CALL create_character_connect_actor(\'{title}\', \'{act_2_name}\',' \
                                f' \'{char_2_name}\', \'{char_2_role}\', {act_2_birth}, \'{act_2_desc}\')'
            try:
                cur.execute(create_actor_char)
                print(f'creating {act_2_name}\'s character...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (create_actor_char, e.args[0], e.args[1]))

    if menu == '2':
        print('--------add a new kdrama review--------')
        add_review = input('Type in your review here: ')
        add_kid = input('Type in the drama\' title: ')
        add_uid = input('Type in your username: ')
        add_rating = input('Type in your overall rating of the drama: ')

        create_review = f'CALL add_review(\'{add_review}\', \'{add_kid}\', \'{add_uid}\', {add_rating})'
        try:
            cur.execute(create_review)
            print("creating " + add_uid + '\'s review...')
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (create_review, e.args[0], e.args[1]))

    if menu == '3':
        print('---------add an award--------')
        drama = input('Type in the drama that won an award: ')
        title = input('Type in title of the award: ')
        year = input('Type in the year the drama won the award: ')

        create_award = f'CALL create_award(\'{drama}\', \'{title}\', {year})'
        try:
            cur.execute(create_award)
            print("creating " + title + '\'s award...')
        except pymysql.Error as e:
            # while loop continues and we ask user to try again
            print('SELECT failed %s Error: %d: %s' % (create_award, e.args[0], e.args[1]))

    if menu == '4':
        all_kdramas(cur)
        print('--------update information of kdrama--------')
        up_did = input('Type in the id of the drama you wish to update: ')
        up_drama = input('Type in the drama title you wish to update: ')

        select = f'SELECT * FROM kdrama WHERE drama_ID = \'{up_did}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))

        # using the inputs below we can make an update
        up_title = input('Update the title of the drama: ')
        up_rating = input('Update the rating of the drama: ')
        up_num_eps = input('Update the number of episodes: ')
        up_synop = input('Update the drama\'s synopsis: ')

        update_kdrama = f'CALL update_kdrama({up_did}, \'{up_title}\', {up_rating}, ' \
                        f'{up_num_eps}, \'{up_synop}\')'
        try:
            cur.execute(update_kdrama)
            print(f'Updating {up_title}...')
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (update_kdrama, e.args[0], e.args[1]))

    if menu == '5':
        # print all reviews so the awards can see
        all_reviews(cur)
        print('---------update information of review--------')
        up_rid = input('What is the review id of the review you want to update: ')

        select = f'SELECT * FROM user_reviews WHERE rid = {up_rid}'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))

        # given the inputs below make an update
        up_review = input('Update the review: ')
        up_rating = input('Update the overall rating (Type in a number 1- 10): ')

        update_review = f'CALL update_rating({up_rid}, \'{up_review}\', {up_rating})'
        try:
            cur.execute(update_review)
            print(f'Updating review number\'{up_rid}\'...')
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (update_review, e.args[0], e.args[1]))

    if menu == '6':
        # print all awards so the user can see
        all_awards(cur)
        print('--------update awards--------')
        up_aid = input('what is the award id you wish to update')

        select = f'SELECT * FROM drama_awards WHERE award_ID = {up_aid}'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))

        # use inputs to update awards
        up_dtitle = input('Update the title of the drama that won an award: ')
        up_atitle = input('Update the name of the award the drama won: ')
        up_ayear = input('Update: the year the award was won: ')

        update_award = f'CALL update_award({up_aid}, \'{up_dtitle}\', \'{up_atitle}\', {up_ayear})'
        try:
            cur.execute(update_award)
            print(f'updating {up_dtitle}\'s award...')
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (update_award, e.args[0], e.args[1]))

    if menu == '7':
        # prints all dramas first, so that user can choose
        all_kdramas(cur)
        print('--------Delete a drama--------')
        del_did = input('Type in the drama id of the drama you wish to delte: ')
        del_drama = input('Type in the title of the drama you wish to delete: ')

        select = f'SELECT * FROM kdrama WHERE drama_id = \'{del_did}\''
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))

        del_confirm = input('Type YES to confirm that you wish to delete this drama: ')
        if del_confirm == 'YES':

            delete_drama = f'CALL delete_kdrama(\'{del_drama}\', \'{del_did}\')'
            try:
                cur.execute(delete_drama)
                print(f'Deleting {del_drama}...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (delete_drama, e.args[0], e.args[1]))

        else:
            print('Going back to main menu...')

    if menu == '8':
        # print all reviews first, so that user can choose
        all_reviews(cur)
        print('--------Delete a review--------')
        del_review = input('Type in the review id of the review you want to delete: ')

        select = f'SELECT * FROM user_reviews WHERE rid = {del_review}'
        try:
            cur.execute(select)
            print(cur.fetchall())
        except pymysql.Error as e:
            print('SELECT failed %s Error: %d: %s' % (select, e.args[0], e.args[1]))

        del_confirm = input('Type YES to confirm that you wish to delete this review: ')
        if del_confirm == 'YES':

            delete_review = f'CALL delete_review({del_review})'
            try:
                cur.execute(delete_review)
                print("deleting review " + del_review + '...')
            except pymysql.Error as e:
                print('SELECT failed %s Error: %d: %s' % (delete_review, e.args[0], e.args[1]))

        else:
            print('Going back to main menu...')

    if menu == '9': # view all dramas
        all_kdramas(cur)

    if menu == '10': # view all dramas
        print('viewing all staff in database...')
        all_actors(cur)
        all_directors(cur)
        all_writers(cur)

    if menu == '11': # view all reviews
        all_reviews(cur)

    if menu == '12':
        print('--------Search through kdrama database--------')
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
                  '(5)rating'
                  '(6)go back')
            dra_menu = input('Choose a menu option: ')
            if dra_menu == '1':
                fil_title = input('Type in a title of kdrama you want to search for: ')

                read_dtitle = f'CALL find_drama_title(\'{fil_title}\')'
                try:
                    cur.execute(read_dtitle)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_dtitle, e.args[0], e.args[1]))

            if dra_menu == '2':
                fil_actor = input('Type in an actor that appeared in the drama you want to find: ')

                read_dactor = f'CALL find_drama_actor(\'{fil_actor}\')'
                try:
                    cur.execute(read_dactor)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_dactor, e.args[0], e.args[1]))

            if dra_menu == '3':
                fil_year = input('Type in a year that the drama was aired in: ')

                read_dyear = f'CALL find_drama_year({fil_year})'
                try:
                    cur.execute(read_dyear)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_dyear, e.args[0], e.args[1]))

            if dra_menu == '4':
                fil_station = input('Type in a station a drama aired on: ')

                read_dstation = f'CALL find_drama_station(\'{fil_station}\')'
                try:
                    cur.execute(read_dstation)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_dstation, e.args[0], e.args[1]))

            if dra_menu == '5':
                fil_rating = input('Type in a rating from 1 to 10 a drama has: ')

                read_drating = f'CALL find_drama_rating(\'{fil_rating}\')'
                try:
                    cur.execute(read_drating)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_drating, e.args[0], e.args[1]))

            else:
                print('Returning to previous menu...')

        if fil_menu == '2':
            print('Do you want to find actor\'s through:'
                  '(1)name'
                  '(2)dramas'
                  '(3)year'
                  '(4)go back')
            act_menu = input('Choose a menu option: ')
            if act_menu == '1':
                fil_name = input('Type in the name of the actor you want to find: ')

                read_aname = f'CALL find_actor_name(\'{fil_name}\')'
                try:
                    cur.execute(read_aname)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_aname, e.args[0], e.args[1]))

            if act_menu == '2':
                fil_drama = input('Type in a drama to find actors who have appeared in the drama: ')

                read_adrama = f'CALL find_actor_drama(\'{fil_drama}\')'
                try:
                    cur.execute(read_adrama)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_adrama, e.args[0], e.args[1]))

            if act_menu == '3':
                fil_ayear = input('Type in a year the actor was born in (YYYY format): ')

                read_ayear = f'CALL find_actor_name({fil_ayear})'
                try:
                    cur.execute(read_ayear)
                    print('results are...')
                    print(cur.fetchall())
                except pymysql.Error as e:
                    print('no results!')
                    print('SELECT failed %s Error: %d: %s' % (read_ayear, e.args[0], e.args[1]))
            else:
                print('Returning to previous menu...')

        else:
            print('Returning to previous menu...')

    if menu == '13':
        print('Closing out of program...')
        cnx.close()
        keepRunning = False

    else:
        print('Unexpected input. Try again.')

    # runs after every option (except 13)
    print('Here is the menu of commands:\n'
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
          '(13)quit program')
