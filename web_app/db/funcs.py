from datetime import datetime
from typing import Tuple, List

from .models import User, Profile, Application, Meet


def get_user_by_tg_id(tg_id: int) -> User | None:
    """Получение юзера по id телеграма"""

    user_instance = User.query().filter_by(telegram_id=tg_id).first()
    return user_instance


def create_user(phone: str, telegram_id: int) -> User | None:
    """Добавление нового юзера"""

    try:
        new_user_instance = User.create(phone=phone, telegram_id=telegram_id)
        return new_user_instance
    except Exception as error:
        print(error)
        return None


def delete_user(user_id: int) -> bool:
    """Удаление юзера"""
    try:
        User.delete(pk=user_id)
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


def create_profile(user_id: int, last_name: str, first_name: str, job_title: str, born_date: datetime) -> Profile | None:
    """Добавление нового профиля"""

    try:
        new_profile_instance = Profile.create(
            user_id=user_id,
            last_name=last_name,
            first_name=first_name,
            job_title=job_title,
            born_date=born_date
        )
        return new_profile_instance
    except Exception as error:
        print(error)
        return None


def create_application(user_id: int, duration: str, appl_format: str) -> Application | None:
    """Добавление новой заявки"""

    try:
        new_application_instance = Application.create(
            user_id=user_id,
            duration=duration,
            format=appl_format
        )
        return new_application_instance
    except Exception as error:
        print(error)
        return None


def delete_application(user_id: int) -> bool:
    """Удаление заявки"""
    try:
        Application.delete(pk=user_id)
        return True
    except Exception as error:
        print(error)
        return False


def get_all_applications() -> List[Application]:
    applications = Application.query().all()
    return applications


def create_meet(first_appl_id: int, second_appl_id: int) -> Meet:
    """Создание встречи из двух заявок"""

    first_appl = Application.query().filter_by(user_id=first_appl_id).first()
    second_appl = Application.query().filter_by(user_id=second_appl_id).first()

    avg_duration = max(first_appl.duration, second_appl.duration)

    new_meet_instance = Meet.create(
        first_user_id=first_appl_id,
        second_user_id=second_appl_id,
        duration=avg_duration,
        format=first_appl.format
    )

    Application.delete(pk=first_appl_id)
    Application.delete(pk=second_appl_id)

    return new_meet_instance


def confirm_meet(meet_id: int, user_id: int) -> bool:
    """Подтверждение встречи от одного из участников"""

    meet = Meet.query().filter_by(id=meet_id).first()

    if user_id == meet.first_user_id:
        Meet.update(instance_id=meet_id, first_user_confirm=True)
    elif user_id == meet.second_user_id:
        Meet.update(instance_id=meet_id, second_user_confirm=True)
    else:
        return False
    return True


def set_rating_meet(meet_id: int, user_id: int, rating: str) -> bool:
    """Оценка встречи от одного из участников"""

    meet = Meet.query().filter_by(id=meet_id).first()

    if user_id == meet.first_user_id:
        Meet.update(instance_id=meet_id, first_user_rating=rating)
    elif user_id == meet.second_user_id:
        Meet.update(instance_id=meet_id, second_user_rating=rating)
    else:
        return False
    return True


def user_info(user_id: int) -> Tuple[Profile, bool]:
    """Получение профиля юзера и информации, подана ли у него заявка"""

    user_profile_instance = Profile.query().filter_by(user_id=user_id).first()
    in_queue = True if Application.query().filter_by(user_id=user_id).first() else False

    return user_profile_instance, in_queue


def get_full_name_by_user_id(user_id: int) -> str:
    """Получение полного имени юзера"""

    user_profile_instance = Profile.query().filter_by(user_id=user_id).first()
    full_name = user_profile_instance.first_name + " " + user_profile_instance.last_name

    return full_name


def get_all_meets() -> List[Meet]:
    """Получение всех встреч"""

    meets = Meet.query().all()
    return meets
