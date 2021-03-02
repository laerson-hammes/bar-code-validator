# Código de Barras
# 7898275010656
# 1 Passo:
   # (Soma todos os números dos indices pares), exceto o de número 12, último dígito do código
   # (7 + 9 + 2 + 5 + 1 + 6) = 30
# 2 Passo:
   # (Soma todos os números dos indices impares) * 3 
   # (8 + 8 + 7 + 0 + 0 + 5) * 3 = 84
# 3 Passo:
   # Soma os resultados do passo 1 e 2
   # (30 + 84) = 114
# 4 Passo:
   # Encontre o próximo númnero divisível por 10 (resto 0) que seja igual ou > que o resultado do passo 3
   # 120
# 5 Passo:
   # Passo 4 - Passo 3
   # (120 - 114) = 6
   
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
