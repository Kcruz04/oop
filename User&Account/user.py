class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
        # if self.is_rewards_member == True:
        #     print('Already a member')
        #     return False
        # else:
        #     return True
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return amount

user1 = User( 'Kenneth', 'Cruz', 'Kc@email.com', 30)
user2 = User('Shari', 'J', 'SJ@email.com', 21)

user1.display_info().enroll().spend_points(50)
user2.enroll().spend_points(80)
user1.display_info()
user2.display_info()
# user2
# user1.display_info()
# user2.display_info()
