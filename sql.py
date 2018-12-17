import sqlite3

list_of_items = ['title',
                 'description',
                 'content',
                 'title_pre',
                 'description_pre',
                 'content_pre',
                 'title_entities',
                 'title_tokens',
                 'title_dependencies',
                 'description_entities',
                 'description_tokens',
                 'description_dependencies',
                 'content_entities',
                 'content_tokens',
                 'content_dependencies',
                 'title_pre_entities',
                 'title_pre_tokens',
                 'title_pre_dependencies',
                 'description_pre_entities',
                 'description_pre_tokens',
                 'description_pre_dependencies',
                 'content_pre_entities',
                 'content_pre_tokens',
                 'content_pre_dependencies']


def create_table():
    list_ = ([ttype + ' text' for ttype in list_of_items])

    string = str()
    for entry in list_:
        string += entry + ', '
    string = string[0: len(string) - 2]
    string = '''CREATE TABLE DATA(''' + string + ''')'''

    # print(string)

    con = sqlite3.connect('storage.db')
    c = con.cursor()
    c.execute(string)
    con.commit()
    con.close()


def dump_data(data):
    """Dumps our data in a database, currently has some issues, but dumps generally okay"""
    print('i just got here')
    con = sqlite3.connect('storage.db')
    c = con.cursor()
    for entry in data:
        string = ''
        for key_value in entry.keys():
            string += '"' + str(entry[key_value]).strip('\"') + '", '

        string = '''INSERT INTO DATA VALUES (''' + string[0:len(string) - 2] + ''')'''
        try:
            c.execute(string)
        except sqlite3.OperationalError:
            print('something went wrong, have the string')
            print(string)

    con.commit()
    con.close()


# create_table()
