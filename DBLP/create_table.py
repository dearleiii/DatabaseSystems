def create_tables():
    commands = (
        """ 
        CREATE TABLE Article (
            pubkey VARCHAR(255) PRIMARY KEY, 
            title VARCHAR(255) NOT NULL,
            journal VARCHAR(255) NOT NULL,
            year INTEGER
        )
        """, 
        """ 
        CREATE TABLE Inproceedings (
            pubkey VARCHAR(255) PRIMARY KEY, 
            title VARCHAR(255) NOT NULL,
            booktitle VARCHAR(255) NOT NULL,
            year INTEGER
        )
        """,
        """
        CREATE TABLE Authorship (
            pubkey VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        )
        """)
    conn = None
    try:
        conn = psycopg2.connect("dbname=dblp user=postgres password=201211")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
  
