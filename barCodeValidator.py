def getDivisionOfTen(result):
   for number in range(0, 10, +1):
      result += number
      if result % 10 == 0:
         return result

def validate(digit, code):
   if int(digit) == int(code.pop()):
      print(f"[+] {True}")
   else:  
      print(f"[-] {False}")
     
def validation(code):
   first = 0
   seccond = 0
   for index, element in enumerate(code):
      if index != 12:
         if index % 2 == 0:
            first += int(element)
         else:
            seccond = seccond + (int(element) * 3)
   result = first + seccond
   divisionOfTen = getDivisionOfTen(result)
   validate(divisionOfTen - result, code)
   
def verifyInput(code):
   if len(code) == 13:
      validation(code)
   else:
      for element in code:
         if not element.isnumeric():
            code.remove(element)
      if len(code) != 13:
         print("[-] ERROR")
      else:
         verifyInput(code)
            
   
code = str(input("[+] BAR CODE: "))
verifyInput(list(code))
