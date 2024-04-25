

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/login1')
def login():
    # 处理登录逻辑
    return '登录成功'


@auth_bp.route('/logout1')
def logout():
    # 处理注销逻辑
    return '注销成功'