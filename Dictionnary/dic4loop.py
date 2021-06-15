colors = {"red": "สีแดง", "yellow": "สีเหลือง", "green": "สีเขียว"}
colors.update({"blue": "สีน้ำเงิน", "orange": "สีส้ม", "red": "สีชมพู"})
for item in colors:
    print(item)
for item in colors.values(): #.key() เอา key ||  .values() เอา value  || .items()เอา สองค่า
    print(item)

for k,v in colors.items():
    print("key = ",k,"value =",v )