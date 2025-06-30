def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

# รับข้อมูลจากผู้ใช้
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

# คำนวณ BMI
bmi = calculate_bmi(weight, height)

# แสดงผลลัพธ์
print(f"BMI is {bmi:.1f}")
print(classify_bmi(bmi))
