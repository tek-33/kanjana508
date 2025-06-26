# รายการสินค้าและราคาต่อหน่วย
products = {
    "หมูสับกิโล": 150.00,
    "เนื้ออกไก่": 105.00,
    "ไก่บ้าน(ตัว)": 120.00,
    "มาม่าต้มยำ": 6.50,
    "ข้าวสาร": 150.00,
    "น้ำตาล": 20.00,
    "ปลากระป๋องสามแม่ครัว": 10.00,
    "ซอสหอยนางรม": 18.00,
    "ผงชูรส": 10.25,
    "ไข่แยกละเบอร์": 120.25,
    "เท็นเท็น": 21.50,
    "Pepsi": 29.50,
    "กาแฟ": 15.75,
    "ขนมปังอบเนย": 19.00,
    "ชาไทย": 11.50,
    "น้ำเปล่า": 15.15,
    "น้ำแข็ง": 10.00
}

# งบประมาณ
budget = 1000.00

# สุ่มเลือกสินค้าอย่างน้อย 15 รายการ โดยไม่ให้เกินงบ
import random

selected_items = []
total_cost = 0.0

# สุ่มรายการแบบสุ่มไม่ซ้ำ
available_items = list(products.items())
random.shuffle(available_items)

for name, price in available_items:
    if len(selected_items) >= 15:
        break
    if total_cost + price <= budget:
        selected_items.append((name, price))
        total_cost += price

# แสดงผล
print("รายการสินค้าที่ซื้อ:")
for i, (name, price) in enumerate(selected_items, 1):
    print(f"{i}. {name} - {price:.2f} บาท")

print(f"\nรวมเป็นเงิน: {total_cost:.2f} บาท")
print(f"เงินทอน: {budget - total_cost:.2f} บาท")