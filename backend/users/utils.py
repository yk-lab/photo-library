from guardian import management


def get_anonymous_user_instance(User):
    user = management.get_init_anonymous_user(User)
    user.display_name = "ゲスト"
    return user
