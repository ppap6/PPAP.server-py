def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'user': {
            "uid": user.id,
            "uname": user.user_name,
            "avatar": user.avatar,
            "bg": user.bg,
            "sex": user.gender,
            "email": user.email,
            "identity": 1,
            "create_time": user.create_time,
            "token": token,
            "count": {
                    "posts": 10,
                    "comments": 4,
                    "answers": 14,
                    "fans": 1,
                    "follows": 1,
                    "likes": 0,
                    "collects": 0,
                    "topics": 1
                }
        },
        "message": "登录成功",
        "status": 200,
    }

