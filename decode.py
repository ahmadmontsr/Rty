import marshal

# استبدل النص الموجود في marshal.loads بالنص الموجود في facebook.py
decoded_code = marshal.loads(b'c\x00\x00\x00\x0>')  # تأكد من استبدال هذه السلسلة بالنص الصحيح
print(decoded_code)

