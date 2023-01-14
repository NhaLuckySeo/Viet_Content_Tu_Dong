# import sqlite3
#
# def register(email, password):
#   # Kết nối tới database
#   conn = sqlite3.connect('users.db')
#   c = conn.cursor()
#
#   # Kiểm tra xem email đã được đăng ký hay chưa
#   c.execute("SELECT * FROM users WHERE email=?", (email,))
#   result = c.fetchone()
#
#   if result:
#     # Nếu email đã được đăng ký, trả về một thông báo lỗi
#     return "Địa chỉ email này đã được đăng ký!"
#   else:
#     # Nếu email chưa được đăng ký, thêm email và mật khẩu vào database
#     c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
#     conn.commit()
#     return "Đăng ký thành công!"
#
# def update(email, password):
#   # Kết nối tới database
#   conn = sqlite3.connect('users.db')
#   c = conn.cursor()
#
#   # Cập nhật email và mật khẩu của người dùng
#   c.execute("UPDATE users SET email=?, password=?", (email, password))
#   conn.commit()
#   return "Cập nhật thành công!"
#
# def login(email, password):
#   # Kết nối tới database
#   conn = sqlite3.connect('users.db')
#   c = conn.cursor()
#
#   # Kiểm tra xem email và mật khẩu có khớp với bản ghi trong database không
#   c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#   result = c.fetchone()
#
#   if result:
#     # Nếu khớp, trả về một thông báo đăng nhập thành công
