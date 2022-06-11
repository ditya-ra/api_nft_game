from .repositories import JobRepository, NftRepository, UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_user(self, user):
        return self.repository.get(user)

    def get_user_balance(self, user):
        return self.repository.get(user).balance

    def update_balance(self, user, balance):
        return self.repository.update_balance(user, balance)


class NftService:
    def __init__(self):
        self.repository = NftRepository()

    def get_nft_by_id(self, nft_id):
        return self.repository.get(nft_id)

    def get_price_by_id(self, nft_id):
        return self.repository.get(nft_id).price


class JobService:
    def __init__(self):
        self.repository = JobRepository()

    def get_text_by_id(self, job_id):
        return self.repository.get(job_id).text

    def get_price_by_id(self, job_id):
        return self.repository.get(job_id).price


class NftServiceUtils:
    @classmethod
    def is_buy_nft(cls, user, validate_data):
        nft_id = validate_data['nft_id']
        nft_price = NftService().get_price_by_id(nft_id)
        user_balance = UserService().get_user_balance(user)

        return user_balance > nft_price

    @classmethod
    def buy_nft(cls, user, validate_data):
        nft_id = validate_data['nft_id']
        nft = NftService().get_nft_by_id(nft_id)
        nft_price = NftService().get_price_by_id(nft_id)
        user = UserService().get_user(user)
        user.nft = nft
        user.level = 1
        user.productivity = nft.productivity
        user.balance -= nft_price
        user.save()


class JobServiceUtils:
    @classmethod
    def is_true_text(cls, validate_data):
        job_id = validate_data['job_id']
        input_text = validate_data['text']
        job_text = JobService().get_text_by_id(job_id)
        return input_text == job_text


class UserServiceUtils:
    @classmethod
    def update_balance_user(cls, validate_data, user):
        job_id = validate_data['job_id']
        job_price = JobService().get_price_by_id(job_id)
        UserService().update_balance(user, job_price)

    @classmethod
    def update_level(cls, user):
        price_for_one_level = 4
        user_ = UserService().get_user(user)
        user_balance = user_.balance
        curr_level = user_.level
        price_for_next_level = price_for_one_level * (curr_level + 1)

        if user_balance > price_for_next_level:
            user_.balance -= price_for_next_level
            user_.level += 1
            user_.productivity += 5
            user_.save()
