# Sử dụng Python image nhẹ
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file requirements trước để tận dụng Docker cache
COPY requirements.txt .

# Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào
COPY . .

# Tạo thư mục data để tránh lỗi permission (nếu cần)
RUN mkdir -p data

# Lệnh chạy mặc định
CMD ["python", "main.py"]