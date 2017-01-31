livro1 = {'Titulo': 'Livro1',
		 'Paginas': 220,
         'Editora':'Abril'}

livro2 = {'Titulo': 'Livro2',
		 'Paginas': 520,
         'Editora':'Sony'}

livro3 = {'Titulo': 'Livro3',
		 'Paginas': 370,
         'Editora':'SeiLA'}

array_livros = [livro1, livro2, livro3]

for i in array_livros:
	print (i['Titulo'])


for i in [range(15)]:
	print (i)

l = [1,3,5,7,11]
list_ret = []
for i in l:
	list_ret.append(i * 2)
print (list_ret)

# Isso é o equivalente do de cima
l = [1,3,5,7,11]
print ([i * 2 for i in l])

# Possivel aplicação
f = lambda x: [x * i for i in [1,3,5,7,11]]
print (f(10))