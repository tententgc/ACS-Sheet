colors = {"red": "สีแดง", "yellow": "สีเหลือง", "green": "สีเขียว"}
colors.update({"blue": "สีน้ำเงิน", "orange": "สีส้ม", "red": "สีชมพู"})
print (colors)
colors.pop("red")
colors.popitem() #อันสุดท้าย 
print(colors)
colors.clear()
print(colors)
del colors