#variable global
nama='python'
versi= ' 1.0.8'

def help():
    #Var lokal
    nama='c++'
    versi= '1.2.1'
    #akses Var lokal
    print('nama : %s' % nama)
    print('versi : %s:' % versi)

#akses Variable global
print('nama : %s % nama')
print('versi : %s' % versi)

#memanggil fungsi help
help()