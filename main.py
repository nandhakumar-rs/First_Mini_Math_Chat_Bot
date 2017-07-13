from wit import Wit

access_token="QWMZWOWJFZHRGOE64VXIDHZ7GJNAII5K"
cli = Wit(access_token=access_token)
text_msg = "formula for addition"
def response(text):
     res = cli.message(text)
     entity = None
     value = None
     try:
         entity = list(res['entities'])[0]
         value = res['entities'][entity][0]['value']
     except:
         pass
     return entity,value


while True:
          entity,value = response(input("Enter your message : "))
          if entity == 'formula':
              if value == 'addition':
                  print("Here is the formula for " + value + " a + b")
              elif value == 'subtraction':
                  print("Here is the formula for " + value + " a - b")
              elif value == 'multiplication':
                  print("Here is the formula for " + value + " a * b")
              elif value == 'division':
                  print("Here is the formula for " + value + " a / b")
              else:
                  print("I can't find this")

          elif entity == 'greeting':
              if value == "thank":
                  print("you are welcome")
              elif value == 'bye':
                  print("bye!Have a nice day")
                  break
              else:
                  print("hi! how can i help you,Please enter a keyword like 'addition' to get its formula...")
          else:
              print("I can't find this")


