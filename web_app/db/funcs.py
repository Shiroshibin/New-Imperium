from datetime import datetime

from models import User, Profile, Application, Meet


def get_user_by_tg_id(tg_id: int) -> list | None:
    """Получение юзера по id телеграма"""

    user = User.query(telegram_id=tg_id)
    return user


def create_user(phone: str, telegram_id: int) -> bool:
    """Добавление нового юзера"""

    try:
        User.create(phone=phone, telegram_id=telegram_id)
        return True
    except Exception as error:
        print(error)
        return False


def set_active_user(user_id: int) -> bool:
    """Активация аккаунта юзера"""

    try:
        User.update(instance_id=user_id, is_active=True)
        return True
    except Exception as error:
        print(error)
        return False


def create_profile(user_id: int, last_name: str, first_name: str, job_title: str, born_date: datetime) -> bool:
    """Добавление нового юзера"""

    try:
        Profile.create(
            user_id=user_id,
            last_name=last_name,
            first_name=first_name,
            job_title=job_title,
            born_date=born_date
        )
        return True
    except Exception as error:
        print(error)
        return False


def create_application(user_id: int, duration: str, appl_format: str) -> bool:
    """Добавление нового юзера"""

    try:
        Application.create(
            user_id=user_id,
            duration=duration,
            format=appl_format
        )
        return True
    except Exception as error:
        print(error)
        return False


def delete_application(user_id: int) -> bool:
    """Добавление нового юзера"""

    try:
        Application.delete(pk=user_id)
        return True
    except Exception as error:
        print(error)
        return False


def get_all_applications() -> list:
    applications = Application.query()
    return applications


def create_meet(first_appl_id: int, second_appl_id: int) -> list:
    """Создание встречи из двух заявок"""

    first_appl = Application.query(id=first_appl_id)
    second_appl = Application.query(id=second_appl_id)

    avg_duration = max(first_appl, second_appl)

    new_meet = Meet.create(
        first_user_id=first_appl_id,
        second_user_id=second_appl_id,
        duration=avg_duration,
        format=first_appl.format
    )

    Application.delete(pk=first_appl_id)
    Application.delete(pk=second_appl_id)

    return new_meet


def confirm_meet(meet_id: int, user_id: int) -> bool:
    """Подтверждение встречи от одного из участников"""

    meet = Meet.query(id=meet_id)

    if user_id == meet.first_user_id:
        Meet.update(instance_id=meet_id, first_user_confirm=True)
    elif user_id == meet.second_user_id:
        Meet.update(instance_id=meet_id, second_user_confirm=True)
    else:
        return False


def set_rating_meet(meet_id: int, user_id: int) -> bool:
    """Оценка встречи от одного из участников"""

    meet = Meet.query(id=meet_id)

    if user_id == meet.first_user_id:
        Meet.update(instance_id=meet_id, first_user_rating=True)
    elif user_id == meet.second_user_id:
        Meet.update(instance_id=meet_id, second_user_rating=True)
    else:
        return False


def user_info(user_id: int) -> tuple:
    user_profile = Profile.query(id=user_id)
    in_queue = True if Application.query(id=user_id) else False

    return user_profile, in_queue
