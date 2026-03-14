from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def get_users(self):
        return self.repo.get_all_users()

    def get_user(self, user_id: int):
        user = self.repo.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found")
        return user

    def create_user(self, user: UserCreate):
        if "@" not in user.email:
            raise Exception("Invalid email")

        existing_user = self.repo.get_user_by_email(user.email)
        if existing_user:
            raise Exception("Email already exists")

        return self.repo.create_user(user.name, user.email)

    def update_user(self, user_id: int, user: UserUpdate):
        db_user = self.repo.get_user_by_id(user_id)
        if not db_user:
            raise Exception("User not found")

        if "@" not in user.email:
            raise Exception("Invalid email")

        existing_user = self.repo.get_user_by_email(user.email)
        if existing_user and existing_user.id != user_id:
            raise Exception("Email already exists")

        return self.repo.update_user(db_user, user.name, user.email)

    def delete_user(self, user_id: int):
        db_user = self.repo.get_user_by_id(user_id)
        if not db_user:
            raise Exception("User not found")

        self.repo.delete_user(db_user)
        return {"message": "User deleted successfully"}