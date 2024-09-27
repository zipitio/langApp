import sqlite3

def dbsetup():
    conn = sqlite3.connect('Databases/french_vocab.db')
    c = conn.cursor()

    #c.execute('''CREATE TABLE frenchvocab(word TEXT, topic TEXT, level INT)''')

    word1 = 'bonjour'
    topic1 = "Greetings"
    level = 1

    word2 = 'salut'

    #c.execute('''INSERT INTO frenchvocab VALUES(?,?,?)''', (word1, topic1, level))
    #c.execute('''INSERT INTO frenchvocab VALUES(?,?,?)''', (word2, topic1, level))

    c.execute('''SELECT * FROM frenchvocab''')
    results = c.fetchall()
    print(results)

    conn.commit()




