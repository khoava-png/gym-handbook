# 🏋️ Nét Đô - Cẩm Nang Dinh Dưỡng Tập Gym (Avant-Garde Edition)

Kho chứa tài liệu nghiên cứu dinh dưỡng khoa học và chế độ ăn tối ưu cho mục tiêu tăng cơ nạc (Lean Bulk).

---

## 🎨 Giao Diện Thiết Kế (Avant-Garde / Constructivism / Tech-Art)
Cẩm nang đọc trực tuyến được thiết kế theo phong cách nghệ thuật **Constructivism & Bauhaus**:
- **Background**: Màu xám ấm / beige `#E0E0D0` giả lập chất liệu giấy nhám in ấn cổ điển.
- **Accent**: Màu vàng Neon `#DFFF00` phản quang nổi bật.
- **Lines**: Hệ lưới chia ngăn tối giản bằng các đường nét mực đen mảnh `0.5pt`.
- **Typography**: Sự kết hợp tương phản giữa chữ Serif cổ điển (`DM Serif Display`) và chữ máy đánh chữ Monospace (`Courier New`).

---

## 🚀 Cách Đọc Trực Tuyến
Trang web được xuất bản trực tuyến tại:
👉 **[https://khoava-png.github.io/gym-handbook/](https://khoava-png.github.io/gym-handbook/)**

---

## 🛠️ Quản Lý & Tự Động Hóa Đồng Bộ (Watchdog Updater)
Để đơn giản hóa việc cập nhật nội dung từ máy tính lên web, thư mục chứa sẵn một script tự động theo dõi (Watchdog):

1. **`watchdog.py`**: Script Python chạy ngầm, liên tục giám sát sự thay đổi của các file `index.html` và `Nghien_Cuu_Dinh_Duong_Gym.md`.
2. **`run_watchdog.bat`**: File chạy nhanh trên Windows.

### Hướng dẫn sử dụng Watchdog:
- Nhấp đúp chuột vào file **`run_watchdog.bat`** khi bắt đầu làm việc.
- Cửa sổ dòng lệnh sẽ mở ra và giám sát các file.
- Mỗi khi bạn chỉnh sửa và nhấn **Save (Ctrl + S)** file `index.html` hoặc `Nghien_Cuu_Dinh_Duong_Gym.md`, Watchdog sẽ tự động thực thi chuỗi lệnh:
  ```bash
  git add index.html Nghien_Cuu_Dinh_Duong_Gym.md
  git commit -m "Auto-update: [Thời gian]"
  git push origin main
  ```
- Bạn không cần gõ bất kỳ lệnh Terminal nào, trang web online của bạn sẽ tự động cập nhật sau 5 giây!
