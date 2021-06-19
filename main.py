import wolframalpha

client = wolframalpha.Client('JPY49W-5R97J6XYAX')


while True:
  query = str(input("Your Question: "))
  res = client.query(query)
  output = next(res.results).text
  print(output)