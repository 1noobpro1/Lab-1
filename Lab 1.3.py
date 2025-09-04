my_list = ['Python', 15442, 32, 'QweRty', 34, 19, 'love']
gl = "aeiouAEIOU"
sogl = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
gl_count = 0
sogl_count = 0

for item in my_list:
    if isinstance(item, str):
        for char in item:
            if char in gl:
                gl_count += 1
            elif char in sogl:
                sogl_count += 1
        print("Слово",item,": гласных -",gl_count," согласных -", sogl_count)
        gl_count = 0
        sogl_count = 0
    else:
        print("Элемент", item, "не является словом")