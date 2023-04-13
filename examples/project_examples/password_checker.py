from string_py import Str, Color
import string


class PasswordManager:
    def __init__(self, password: Str):
        self.password = password

    @staticmethod
    def generate_password() -> str:
        return Str(string.ascii_letters + string.digits + ".,?!$#").generate(min_=20, max_=30)

    def calc_strength(self, points: int):
        if points <= 15:
            print("You password is okay. Maybe use a new password. Example: " + self.generate_password())
        elif points <= 10:
            print("Bad! You should use a new password. Example: " + Color.basic,
                  self.generate_password())
        if points < 5:
            print("Very Bad! You should use a new password. Example: ", Color.basic,
                  self.generate_password())
        else:
            print("Your password is fine!")

    def check_password(self):
        points = 0
        if len(self.password) < 8:
            return self.calc_strength(points)
        else:
            points += 0.5 * len(self.password)
        if self.password.get_numeric(chars=False) == 0:
            points -= 1
        if self.password.get_upper(chars=False) == 0:
            points -= 1
        if self.password.get_lower(chars=False) == 0:
            points -= 1
        if self.password.get_punctuation(chars=False) == 0:
            points -= 1
        else:
            points += 10
        return self.calc_strength(round(points))


if __name__ == "__main__":
    PasswordManager(Str(input("Your password: "))).check_password()
