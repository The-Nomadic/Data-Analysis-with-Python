a,b=10,0
min=a if a<b else b
print(min)

print(dir("string"))

try:
    print("open")
    print(a/b)
except Exception as e:
    print("error",e)
finally:
    print("close")
print("success")