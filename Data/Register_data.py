from faker import Faker
faker = Faker(locale="FR_fr")


class RegisterData:


    @staticmethod
    def formulaire_register():
        return {
            "firstName" : faker.first_name(),
            "lastName" : faker.last_name(),
            "email" : faker.email(),
            "pwd" : "password",
            "pwdConfirm" : "password"
        }