#แบบปกติ
fruit = {"มะม่วง", "มะขาม", "มะยม"}

#เพิ่มข้อมูลสมาชิก
fruit.add("ทุเรียน")
print(fruit)

fruit.add("สัปปะรด")
print(fruit)
fruit.add(999)

print(fruit)
#เพิ่มสมาชิกหลายตัว
fruit.update(["ตะไคร้", "โหระพา", "ชะอม"])

#Loop
print(fruit)

#แสดงจำนวนสมาชิกใน set
# print(len(fruit))

fruit.discard("ทุเรียน")  # remove ถ้าไม่มีจะerror  / discard ถ้ามีหรือไม่มี ก็ไม่ error
fruit.clear()
#del fruit
print(fruit)
