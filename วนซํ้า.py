# ฟังก์ชันช่วยนับจำนวนรอบและแสดงค่าของ i หลังจบลูป
def loop_info(range_obj):
    count = 0
    last_i = None
    for i in range_obj:
        count += 1
        last_i = i

    print(f"จำนวนรอบที่ทำงาน: {count}")
    if count > 0:
        print(f"ค่าของ i หลังจบลูป: {last_i}")
    else:
        print("ลูปไม่ถูกทำงานเลย (จำนวนรอบ = 0)")
    print('-' * 30)

# เรียกใช้ฟังก์ชันกับลูปต่าง ๆ
print("1. for i in range(1, 101):")
loop_info(range(1, 101))

print("2. for i in range(7, 77, 7):")
loop_info(range(7, 77, 7))

print("3. for i in range(20, 1, -2):")
loop_info(range(20, 1, -2))

print("4. for i in range(2, 18, 3):")
loop_info(range(2, 18, 3))

print("5. for i in range(55, 0, -11):")
loop_info(range(55, 0, -11))

print("6. for i in range(1, 0):")
loop_info(range(1, 0))
