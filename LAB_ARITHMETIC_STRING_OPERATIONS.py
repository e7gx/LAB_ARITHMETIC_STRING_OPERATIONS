

price = 2.99  # !-1 first part
quantity = 3  #! -2 second part
tax_rate = 7.5 / 100  #! -3 third part

#!  subtotal and tax and total make variables
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# ! print -_- results
print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")


test = f"Price of item: ${price:.2f}\nQuantity: {quantity}\nTax rate: {tax_rate * 100}%\n\nSubtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}"

sentence = "abdullah lovees to code in python all day long."
word = "long"

print("\nthe Length:", len(sentence))#! يعطيك طول الجملة
print("Index of the word:", sentence.index("day")) #! يعطيك موقع الكلمة
print("Number of times the word appears:", sentence.count(word))#! يعد كم مره تكررت الكلمة
print("Sentence in uppercase:", sentence.upper())#! كلها كابتل 
print("Sentence in lowercase:", sentence.lower())#! كلها سمول 
print("Sentence with replaced word:", sentence.replace(word, "long"))
print("Last character of the sentence:", sentence[-1])#! ياخذ من النهاية بسبب -١
print("thanks the lab has been done")