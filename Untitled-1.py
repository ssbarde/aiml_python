import tabula

print("fdgfd")
df = tabula.read_pdf("C:/Users/Saudagar/Downloads/file_example_XLS_10.pdf", pages = 1)[0]
df.to_csv('C:/Users/Saudagar/Downloads/file_example_XLS_10.csv')
