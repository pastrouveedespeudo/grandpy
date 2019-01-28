class Post():

    POSTS = [

        {"id":1, "titre":"premier post", "body":"premier post biatch"},
        {"id":2, "titre":"deuxieme post", "body":"deuxieme post biatch"},
        {"id":3, "titre":"troisieme post", "body":"troisieme post biatch"}


        ]

    @classmethod
    def all(cls):
        return cls.POSTS


    @classmethod
    def find(cls, id):
        cls.id = id
        return cls.POSTS[int(cls.id) - 1]
