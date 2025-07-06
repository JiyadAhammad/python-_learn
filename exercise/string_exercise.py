# Extract a product name from a url
# eg -> https://www.amazon.in/s?k=iphone+16+pro&adgrpid=66140603460&ext_vrnc
# output = iphone 16 pro

input_string = "https://www.amazon.in/s?k=iphone+16+pro&adgrpid=66140603460&ext_vrnc"

format_string_start = input_string.find("?k=")
format_string_end = input_string.find("&")

print(input_string[format_string_start + 3 : format_string_end].replace("+", " "))
