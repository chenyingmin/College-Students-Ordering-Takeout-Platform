class UserCenterService:
    def __init__(self):
        self.user = {
            "user_id": "student001",
            "name": "张三同学",
            "student_verified": False,
            "order_count": 3,
            "message_count": 2
        }

    # 获取用户信息
    def get_user_info(self):
        return {
            "name": self.user["name"],
            "student_verified": self.user["student_verified"],
            "order_count": self.user["order_count"],
            "message_count": self.user["message_count"]
        }

    # 学生认证
    def verify_student(self, student_id):
        if len(student_id) < 6:
            return {"success": False, "msg": "学号格式不正确"}
        self.user["student_verified"] = True
        return {"success": True, "msg": "学生认证成功"}

    # 获取订单列表
    def get_orders(self):
        return [
            {"id": "ORD001", "status": "已完成", "time": "2026-05-05"},
            {"id": "ORD002", "status": "配送中", "time": "2026-05-06"},
            {"id": "ORD003", "status": "待支付", "time": "2026-05-06"}
        ]

    # 获取消息
    def get_messages(self):
        return [
            {"id": 1, "content": "您的订单已送达", "read": False},
            {"id": 2, "content": "平台新功能上线", "read": False}
        ]

    # 退出登录
    def logout(self):
        self.user = {
            "user_id": None,
            "name": "未登录",
            "student_verified": False,
            "order_count": 0,
            "message_count": 0
        }
        return True


# 直接运行测试
if __name__ == "__main__":
    service = UserCenterService()

    print("=== 用户信息 ===")
    print(service.get_user_info())

    print("\n=== 学生认证 ===")
    print(service.verify_student("2023001"))

    print("\n=== 订单列表 ===")
    print(service.get_orders())

    print("\n=== 消息列表 ===")
    print(service.get_messages())