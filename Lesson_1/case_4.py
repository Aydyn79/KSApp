'''4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).'''

enc_seq = ['разработка', 'администрирование', 'protocol', 'standard']

dec_seq = [word.encode('utf8') for word in enc_seq]
print(*dec_seq, sep='\n')

back_enc_seq = [word.decode('utf8') for word in dec_seq]
print(*back_enc_seq, sep=', ')