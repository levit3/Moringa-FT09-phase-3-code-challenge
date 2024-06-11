from database.connection import get_db_connection
conn = get_db_connection()
cursor = conn.cursor()

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.id = self.save()
        
    def save(self):
        sql = """
            INSERT INTO articles(title, content, author_id, magazine_id)
            VALUES (?,?,?,?)
        """
        cursor.execute(sql, (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        return cursor.lastrowid

    def __repr__(self):
        return f'<Article {self.title}>'
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        ### Cannot be implemented because the data cannot be initially in the table before it is initialized ###
        # sql = """
        #     SELECT title
        #     FROM articles
        #     WHERE title = ?
        # """
        # title = cursor.execute(sql, (value,)).fetchone()
        
        # if not title:
        #     raise Exception("Title must be in the table")
        if not isinstance(value, str):
            raise ValueError("Title must be a sting")
        elif not 5 <= len(value) <= 50:
            raise Exception("Title must have between 5 and 50 characters")
        elif hasattr(self, '_title'):
            raise Exception("Title cannot be changed")
        else:
            self._title = value
        
        
    def authors(self):
        sql = """
            SELECT name
            FROM author
            INNER JOIN article
            ON author.id = ?
        """
        authors = cursor.execute(sql, self.author_id,).fetchall()
        return authors
    
    def magazines(self):
        sql = """
            SELECT name
            FROM magazine
            INNER JOIN article
            ON magazine.id = ?
        """
        magazines = cursor.execute(sql, (self._magazine_id,)).fetchall()
        return magazines