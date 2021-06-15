#list ,tuple

lis =["red","blue","green"]
tup = ("red", "blue", "green")

#dictionnary => key(การเข้าถึงข้อมูล    เป็นค่าอะไรก็ได้),value(ค่าขอวข้อมูล)
#list , tuple => index    เป็น int, value

#การสร้าง dict
# ชื่อตัวแปร = {key:value,key:value,key:value,key:value}
colors ={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า"}
colors1 =dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า"})

print(colors1["red"])
#constructor
pets =dict(cat="แมว",dog="หมา",duck ="เป็ด")
print(pets["cat"])
