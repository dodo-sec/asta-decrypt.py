from ctypes import c_uint8, c_uint32
 
i = 0
intermediate_array = bytearray()
final_array = bytearray()
 
with open("db.temp", "rb") as obf, open("asta-decrypted.exe", "wb") as out:
    encrypted_array = bytearray(obf.read())
    while i < len(encrypted_array):
        intermediate_array.append(encrypted_array[i] ^ c_uint8((c_uint32(0x03E7 >> i%32)).value).value)
        i += 1
    i = 0
    while i < len(intermediate_array):
        final_array.append(intermediate_array[i] ^ c_uint8((c_uint32(0xA2C99 >> i%32)).value).value)
        i += 1
    out.write(final_array)