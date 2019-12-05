# binary1.py

with open("binary1", 'bw') as bin_file:
    for i in range(7,35):
        # bytes converts i into a byte object
        bin_file.write(bytes([i]))

with open("binary1", 'br') as b_file:
    for b in b_file:
        print(b)
print("end")
""" Output:  note: 09 = tab char, 10 = new line char
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
b'\x0b\x0c\r\x0e\x0f\x10'
"""

