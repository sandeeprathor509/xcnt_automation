class Constants(object):

    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.email = None
        self.uuid = None

    @property
    def firstname(self):
        return self.firstname

    @firstname.setter
    def firstname(self, firstname):
        self.firstname = firstname

    @property
    def lastname(self):
        return self.lastname

    @lastname.setter
    def lastname(self, lastname):
        self.lastname = lastname

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def uuid(self):
        return self.uuid

    @uuid.setter
    def uuid(self, uuid):
        self.uuid = uuid
