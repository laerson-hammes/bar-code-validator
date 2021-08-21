def get_division_of_ten(result):
   for number in range(0, 10, +1):
      aux = result + number
      if aux % 10 == 0:
         return aux


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
            seccond += (int(element) * 3)
   result = first + seccond
   division_of_ten = get_division_of_ten(result)
   validate(division_of_ten - result, code)
   
   
def verify_input(code):
   if len(code) == 13:
      validation(code)
   else:
      for element in code:
         if not element.isnumeric():
            code.remove(element)
      if len(code) != 13:
         print("[-] ERROR")
      else:
         verify_input(code)
            
   
code = str(input("[+] BAR CODE: "))
verify_input(list(code))
