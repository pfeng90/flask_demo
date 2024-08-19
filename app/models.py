from app import db

class User(db.Model):
    """docstring for User"""
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    def __repr__(self):
        return '<User %r' % (self.nickname)


#创建一个Book类，用来存储书籍信息,
class Book(db.Model):
    """docstring for Book"""
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique = True)
    author = db.Column(db.String(100), index = True, unique = True)
    def __repr__(self):
        return '<Book %r' % (self.title)
#创建一个章节类，用来存储书籍的章节信息
class Chapter(db.Model):
    """docstring for Chapter"""
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True, unique = True)
    content = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    def __repr__(self):
        return '<Chapter %r' % (self.title)    
#创建一个书库类，用来存储书库信息，同一类型的书籍放在一个书库中
class BookStore(db.Model):
    """docstring for BookStore"""
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), index = True, unique = True)
    books = db.relationship('Book', backref = 'bookstore', lazy = 'dynamic')
    def __repr__(self):
        return '<BookStore %r' % (self.name)