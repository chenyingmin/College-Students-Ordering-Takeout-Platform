# user_center_service.py
from datetime import datetime

class UserCenterService:
    def __init__(self):
        # 模拟用户数据
        self.users = {
            "student001": {
                "user_id": "student001",
                "name": "张三同学",
                "phone": "138****1234",
                "is_student_verified": False,
                "orders": [
                    {"order_id": "ORD001", "status": "已送达", "create_time": "2026-05-05 12:30"},
                    {"order_id": "ORD002", "status": "配送中", "create_time": "2026-05-06 11:20"},
                    {"order_id": "ORD003", "status": "待支付", "create_time": "2026-05-06 15:40"}
                ],
                "notifications": [
                    {"id": 1, "content": "您的订单已送达，请尽快取餐", "read": False},
                    {"id": 2, "content": "平台新功能上线：拼单点餐", "read": False}
                ]
            }
        }

    def get_user_info(self, user_id):
        """获取用户中心的基本信息"""
        user = self.users.get(user_id)
        if not user:
            return {"success": False, "message": "用户不存在"}
        
        return {
            "success": True,
            "user_info": {
                "name": user["name"],
                "is_student_verified": user["is_student_verified"],
                "order_count": len(user["orders"]),
                "unread_notification_count": sum(1 for n in user["notifications"] if not n["read"])
            }
        }

    def student_verification(self, user_id, student_id, school_name):
        """模拟校园身份认证"""
        user = self.users.get(user_id)
        if not user:
            return {"success": False, "message": "用户不存在"}
        
        if user["is_student_verified"]:
            return {"success": False, "message": "您的校园身份已认证"}
        
        # 这里可以加一些简单的校验逻辑
        if len(student_id) < 6:
            return {"success": False, "message": "学号格式不正确"}
        
        user["is_student_verified"] = True
        return {"success": True, "message": "校园身份认证成功！您已解锁学生专属优惠"}

    def get_user_orders(self, user_id):
        """获取用户所有订单"""
        user = self.users.get(user_id)
        if not user:
            return {"success": False, "message": "用户不存在"}
        
        return {"success": True, "orders": user["orders"]}

    def mark_notification_read(self, user_id, notification_id):
        """标记消息为已读"""
        user = self.users.get(user_id)
        if not user:
            return {"success": False, "message": "用户不存在"}
        
        for notification in user["notifications"]:
            if notification["id"] == notification_id:
                notification["read"] = True
                return {"success": True, "message": "消息已标记为已读"}
        
        return {"success": False, "message": "消息不存在"}


# 测试代码
if __name__ == "__main__":
    service = UserCenterService()
    user_id = "student001"

    # 1. 获取用户中心信息
    print("用户中心信息：")
    print(service.get_user_info(user_id))

    # 2. 模拟校园认证
    print("\n模拟校园认证：")
    print(service.student_verification(user_id, "2023001", "佛山大学"))

    # 3. 获取用户订单
    print("\n用户订单列表：")
    print(service.get_user_orders(user_id))