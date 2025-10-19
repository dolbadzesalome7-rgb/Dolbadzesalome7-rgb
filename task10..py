#  ამოცანა #1 — inputs.txt ფაილიდან სახელის წაკითხვა და უკუღმა ჩაწერა output.txt-ში

def main():
    input_file = "inputs.txt"
    output_file = "output.txt"
    
    try:
        # 1️⃣ წავიკითხოთ სახელი
        with open(input_file, "r", encoding="utf-8") as f:
            name = f.readline().strip()
            
        if not name:
            print(" inputs.txt ფაილი ცარიელია. გთხოვთ, ჩაწეროთ თქვენი სახელი.")
            return
        
        # 2️⃣ შემოვაბრუნოთ სახელი (უკუღმა)
        reversed_name = "".join(reversed(name))
        
        # 3️⃣ შევქმნათ გამოსატანი ტექსტი
        message = f"გამარჯობა, {reversed_name}"
        
        # 4️⃣ ჩავწეროთ შედეგი ახალ ფაილში
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(message)
        
        print(f"შესრულებულია! შედეგი ჩაწერილია '{output_file}' ფაილში.")
        print(f" ტექსტი: {message}")
    
    except FileNotFoundError:
        print(" ვერ მოიძებნა inputs.txt. გთხოვთ, შექმნათ ფაილი და ჩაწეროთ თქვენი სახელი.")
    except Exception as e:
        print(f" გაუთვალისწინებელი შეცდომა: {e}")

if __name__ == "__main__":
    main()