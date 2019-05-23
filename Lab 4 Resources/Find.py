from Crypto.Cipher import AES

#Function for padding the plaintext if it does not consist of 
#an integral number of 16-byte blocks
bs = AES.block_size
pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def KeyGen(keystring):
	#Write a code to generate the key to be 128 bits (16 bytes)
	#Your code goes here
	return key

def do_crypt(outfile, keystring):
	intext = "This is a top secret."
	#Generate key
	key = KeyGen(keystring)

	#Initialize the iv here
	iv = 16 * '\x00'
	#Initialize the encryption aes_128_cbc
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	
	#Pad the plaintext
	text = pad(intext)

	ciphertext = encryptor.encrypt(text)
	
	#Fill out the expected cipher text
	result = []
	
	#Flag for exact match
	rightFlag = 1

	#Write a test to check whether the ciphertext matches with the result
	#Hint: compare individual bytes using for-loop
	#Your code goes here

	
	if rightFlag == 1:
		return 100		
	out = open(outfile, "w")
	out.write(ciphertext)
	out.close()
	return 1

if __name__ == '__main__':
	#Open the English word file
	#For each word, check whether if the word contains less than 16-byte characters
	#and use it as a key to see if the ciphertext matches
	#Once you find a word that matches the ciphertext, print it
	#Your code goes here

