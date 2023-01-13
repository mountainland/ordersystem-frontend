class product():
    def __init__(self, response):
        self.price = response["price"]
        self.name = response["name"]
