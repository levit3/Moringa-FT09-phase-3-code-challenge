from database.connection import get_db_connection
conn = get_db_connection()
cursor = conn.cursor()

class Author:
    def __init__(self, id, name):
        self.name = name
        self.id = self.save()
        
    def save(self):
        sql = """
            INSERT INTO authors(name)
            VALUES (?)
        """
        cursor.execute(sql, (self.name,))
        conn.commit()
        return cursor.lastrowid

    def __repr__(self):
        return f'<Author {self.name}>'
    
    @property
    def id(self):
        return self._id 
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("Id must be an integer")
        self._id = value
            
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        ### Cannot be implemented because the data cannot be initially in the table before it is initialized ###
        # conn = get_db_connection()
        # cursor = conn.cursor()
        # sql = """
        #     SELECT name
        #     FROM authors
        #     WHERE name = ?
        # """
        
        # name = cursor.execute(sql, (value,)).fetchone()
        
        # if not name:
        #     raise Exception("Name must be in the table")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        elif not value:
            raise ValueError("Name must not be blank")
        elif hasattr(self, '_name'):
            raise Exception("Name cannot be changed")
        else:
            self._name = value
            
    def articles(self):
        sql = """
            SELECT title
            FROM articles
            INNER JOIN author
            WHERE articles.author_id = ?
        """
        articles = cursor.execute(sql, self._name).fetchall()
        return articles
    
    def magazines(self):
        sql = """
            SELECT name
            FROM magazine
            INNER JOIN author
            WHERE magazine.author_id = ?
        """
        magazines = cursor.execute(sql, self._name).fetchall()
        return magazines
    
