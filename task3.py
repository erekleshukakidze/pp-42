Phonebook = {
    "Giorgi": "1 (555) 234-5678",
    "Ana": "1 (555) 891-2345",
    "Nika": "1 (555) 432-1098",
    "Mariami": "1 (555) 678-9012"
}

print("Phonebook contacts")
print(Phonebook)
print("=" *20)

search_name = input("Enter the name you ant to search for: ") 
phone_number = Phonebook.get(search_name, "Not Found")
print(f"Result for {search_name}: {phone_number}")
   