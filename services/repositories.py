from abc import ABC

from jobs_app.models import Job
from nft_shop_app.models import Nft
from users_app.models import AdvancedUser


class BaseRepository(ABC):
    def __init__(self, model):
        self.model = model

    def get(self, id_):
        return self.model.objects.get(pk=id_)


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(AdvancedUser)

    def get(self, user):
        return self.model.objects.get(user=user)

    def update_balance(self, user, balance):
        user_ = self.model.objects.get(user=user)
        user_.balance += balance
        user_.save()
        return user_


class NftRepository(BaseRepository):
    def __init__(self):
        super().__init__(Nft)


class JobRepository(BaseRepository):
    def __init__(self):
        super().__init__(Job)
