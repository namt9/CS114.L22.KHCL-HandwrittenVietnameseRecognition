# BÀI TẬP QUÁ TRÌNH
# LỚP CS114.L22.KHCL
## YÊU CẦU:
- Mỗi nhóm tìm vài ví dụ về bài toán regression trong thực tế
- Ghi rõ input, output và cách thu thập + xử lý data, commit vào github repository và dẫn link lên Topic trên Classroom.
## Thành viên:
- Trịnh Tuấn Nam 19521874
- Nguyễn Dương Hải 19521464
## Các bài toán:
**1. Dự đoán số lượng phân bón cho một miếng đất**
- Input: Diện tích (m2), Thời gian mua phân bón (dd/mm/yy) , Loại đất trồng trọt (đất cát, đất sét, đất thịt), Loại cây trồng (cây ăn quả dài hạn, cây ăn quả ngắn hạn, cây trồng lấy lá, cây trồng lấy hạt,...)
- Output: Số lượng phân bón ứng với từng loại cây (kg)
- Thu thập data:
  + Dùng thước đo kích thước và tính diện tích của miếng đất
  + Các yếu tố còn lại có thể tự quan sát và tổng hợp/ ghi nhận lại
- Xử lí data:
  + Loại bỏ data bị lỗi, thiếu thông tin 
  + Lưu tất cả data trong một file .csv


**2. Dự đoán số nam giới ế vợ ở Việt Nam**
- Input: Năm dự đoán, Số lượng nam giới của năm vừa nhập vào, tỉ lệ nam-nữ của năm vừa nhập vào, tỉ lệ nam giới thất nghiệp (so với tổng số nam giới) của năm vừa nhập vào.
- Output: Số lượng nam giới ế vợ ở năm dự đoán
- Thu thập data:
  + Thông qua thống kê của Tổng cục dân số Việt Nam: https://www.gso.gov.vn và các nguồn có liên quan (thời sự, bài báo)
- Xử lí data:
  + Loại bỏ data bị lỗi, trống thông tin
  + Chọn lọc một cách cẩn thận (xem thông tin từ những bài viết chính thống, có nhiều lượt xem, bình luận tích cực,....) để có được thông tin chính xác nhất
  + Lưu tất cả trong một file .csv
