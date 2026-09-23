cart_total = float(input("Enter your cart total: "))
is_vip_input = input("Are you a VIP member? (yes/no): "). strip(). lower()
is_vip = is_vip_input == "yes"
is_guest_input = input("Are you a guest user? (yes/no): "). strip(). lower()
is_guest = is_guest_input == "yes"
promo_code = input("Enter promo code (or press Enter to skip): ").strip()


has_free_shipping = cart_total >= 50 or is_vip
has_discount = bool(promo_code) and not is_guest

if has_discount:
    final_total = cart_total * 0.9
else: 
    final_total = cart_total

print("order summury")

if has_free_shipping:
    print("Shipping: free shipping")
else:
    print("shipping: Paid shipping")

if has_discount:
    print(f"Discount: 10% discount applied! final discount: ${final_total: .2f}")
else:
    print(f"Discount: No discount applied. Final total: ${ final_total: .2f}")