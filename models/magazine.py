from database.connection import get_db_connection
conn = get_db_connection()
cursor = conn.cursor()

class Magazine:
    def __init__(self, id, name, category):
        self.name = name
        self.category = category
        self.id = self.save()
    
    def save(self):
        sql = """
            INSERT INTO magazines(name, category)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.category))
        conn.commit()
        return cursor.lastrowid
    
    def __repr__(self):
        return f'<Magazine {self.name}>'
    
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
        # sql = """
        #     SELECT name
        #     FROM magazines
        #     WHERE name = ?
        # """
        
        # name = cursor.execute(sql, (value,)).fetchone()
        
        # if not name:
        #     raise Exception("Name must be in the table")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        elif 16 < len(value) < 2:
            raise ValueError("Name must be between 2 and 16 characters")
        else:
            self._name = value
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        ### Cannot be implemented because the data cannot be initially in the table before it is initialized ###
        # sql = """
        #     SELECT category
        #     FROM magazines
        #     WHERE category = ?
        # """
        # category = cursor.execute(sql, (value,)).fetchone()
        
        # if not category:
        #     raise Exception("Category must be in the table")
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        elif not value:
            raise ValueError("Category must not be empty")
        else:
            self._category = value
        
    def articles(self):
        sql = """
            SELECT name
            FROM articles
            INNER JOIN magazine
            ON articles.magazine_id = ?
        """
        articles = cursor.execute(sql, (self._id,)).fetchall()
        return articles
    
