import camelot

# Extract tables from PDF
tables = camelot.read_pdf('foo.pdf', pages='1-end', flavor='stream')
#Show tables
print(tables)
# Export tables to CSV
tables.export('foo.csv', f='csv', compress=True)
#Export table in position 0 to CSV
tables[0].to_csv('foo.csv')