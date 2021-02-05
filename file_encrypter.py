import pyAesCrypt

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile('C:\\Users\\przem\\Desktop\\Music\\6IX9INE - PUNANI.flac', "C:\\Users\\przem\\Desktop\\6IX9INE - PUNANI.flac.aes", password, bufferSize)
# decrypt
# pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)
