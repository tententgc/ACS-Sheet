market={
    "ร้านป้าพร":{
        "name":"porn",
        "menu":["paokai",'noodle'],
        "zone": "north"
    },
    "ร้านลุงป้อม":{
        "name":"job",
        "menu": ["mango", 'kiwi'],
        "zone": "putmarket"
    },
    "ร้านน้าใจ":
    {
        "name":"jai",
        "menu": ["milk", 'tea'],
        "zone": "7-11"
    }
}
print(market["ร้านป้าพร"]["menu"])
print("noodle" in market["ร้านป้าพร"]["menu"])
if "noodle" in market["ร้านป้าพร"]["menu"]:
    print("เป็น")
else:
    print("ไม่เป็น")
