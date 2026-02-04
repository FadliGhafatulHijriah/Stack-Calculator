"""
Infix to Postfix Converter
===========================

File ini berisi algoritma untuk mengkonversi ekspresi matematika dari
notasi INFIX ke notasi POSTFIX menggunakan Stack.

NOTASI MATEMATIKA:
1. INFIX: Operator di antara operand (normal math)
   Contoh: 3 + 4, (5 + 6) * 2
   
2. POSTFIX (Reverse Polish Notation): Operator setelah operand
   Contoh: 3 4 +, 5 6 + 2 *
   
3. PREFIX: Operator sebelum operand
   Contoh: + 3 4, * + 5 6 2

KENAPA KONVERSI KE POSTFIX?
- Tidak perlu tanda kurung
- Tidak perlu aturan precedence saat evaluasi
- Mudah dievaluasi dengan stack
- Komputer lebih efisien menghitung postfix

ALGORITMA SHUNTING YARD (Dijkstra):
Menggunakan stack untuk menyimpan operator sementara.

Author: Fadli Ghafatul Hijriah
Date: Februari 2026
"""

# Import Stack class yang sudah kita buat
from Stack import Stack


def get_precedence(operator):
    """
    Mendapatkan tingkat precedence (urutan operasi) dari operator.
    
    Precedence menentukan operator mana yang harus dikerjakan duluan.
    Precedence lebih tinggi = dikerjakan lebih dulu.
    
    ATURAN MATEMATIKA:
    - Perkalian dan Pembagian (*, /) = precedence tinggi (2)
    - Penjumlahan dan Pengurangan (+, -) = precedence rendah (1)
    - Pangkat (^) = precedence paling tinggi (3)
    
    Args:
        operator (str): Operator matematika (+, -, *, /, ^)
    
    Returns:
        int: Tingkat precedence (1, 2, atau 3)
    
    Example:
        get_precedence('+')  # Returns 1
        get_precedence('*')  # Returns 2
        get_precedence('^')  # Returns 3
    """
    # Dictionary untuk mapping operator ke precedence
    # Lebih mudah dibaca dan di-maintain daripada if-else
    precedence = {
        '+': 1,  # Penjumlahan: precedence terendah
        '-': 1,  # Pengurangan: precedence terendah
        '*': 2,  # Perkalian: precedence menengah
        '/': 2,  # Pembagian: precedence menengah
        '^': 3   # Pangkat: precedence tertinggi
    }
    
    # Return precedence, default 0 jika operator tidak dikenal
    return precedence.get(operator, 0)


def is_operator(char):
    """
    Mengecek apakah karakter adalah operator matematika.
    
    Args:
        char (str): Karakter yang akan dicek
    
    Returns:
        bool: True jika karakter adalah operator, False jika bukan
    
    Example:
        is_operator('+')  # True
        is_operator('5')  # False
        is_operator('(')  # False
    """
    # List semua operator yang didukung
    operators = ['+', '-', '*', '/', '^']
    
    # Cek apakah char ada dalam list operators
    return char in operators


def infix_to_postfix(expression):
    """
    Mengkonversi ekspresi infix menjadi postfix menggunakan Shunting Yard Algorithm.
    
    ALGORITMA SHUNTING YARD:
    1. Scan expression dari kiri ke kanan
    2. Jika operand (angka): langsung ke output
    3. Jika '(': push ke stack
    4. Jika ')': pop sampai ketemu '('
    5. Jika operator:
       - Pop operator dari stack yang precedence-nya >= operator sekarang
       - Push operator sekarang ke stack
    6. Di akhir: pop semua operator dari stack ke output
    
    Args:
        expression (str): Ekspresi matematika dalam notasi infix
                         Contoh: "3 + 4 * 2"
    
    Returns:
        str: Ekspresi dalam notasi postfix
             Contoh: "3 4 2 * +"
    
    Example:
        infix_to_postfix("3 + 4")           # Returns "3 4 +"
        infix_to_postfix("3 + 4 * 2")       # Returns "3 4 2 * +"
        infix_to_postfix("(5 + 6) * 2")     # Returns "5 6 + 2 *"
    """
    
    # Stack untuk menyimpan operator sementara
    stack = Stack()
    
    # String untuk menyimpan hasil postfix
    postfix = []
    
    # Variabel untuk menyimpan angka multi-digit (misal: 123, 45.6)
    current_number = ""
    
    print(f"\n{'='*60}")
    print(f"KONVERSI INFIX KE POSTFIX")
    print(f"{'='*60}")
    print(f"Infix expression: {expression}")
    print(f"{'='*60}\n")
    
    # Scan setiap karakter dalam expression
    for i, char in enumerate(expression):
        
        print(f"Step {i+1}: Membaca karakter '{char}'")
        
        # CASE 1: Karakter adalah DIGIT atau TITIK (bagian dari angka)
        if char.isdigit() or char == '.':
            # Tambahkan ke current_number untuk handle multi-digit
            current_number += char
            print(f"  → Digit/Decimal point, tambah ke number buffer: '{current_number}'")
        
        # CASE 2: Karakter adalah SPASI (separator)
        elif char == ' ':
            # Jika ada current_number, selesaikan dan tambah ke output
            if current_number:
                postfix.append(current_number)
                print(f"  → Spasi ditemukan, finalisasi number: {current_number}")
                print(f"  → Tambah '{current_number}' ke postfix")
                print(f"  → Postfix sekarang: {' '.join(postfix)}")
                current_number = ""  # Reset number buffer
        
        # CASE 3: Karakter adalah KURUNG BUKA '('
        elif char == '(':
            # Kurung buka langsung di-push ke stack
            stack.push(char)
            print(f"  → Kurung buka '(', push ke stack")
            print(f"  → Stack sekarang: {stack}")
        
        # CASE 4: Karakter adalah KURUNG TUTUP ')'
        elif char == ')':
            # Finalisasi current_number jika ada
            if current_number:
                postfix.append(current_number)
                print(f"  → Finalisasi number sebelum ')': {current_number}")
                current_number = ""
            
            # Pop semua operator sampai ketemu '('
            print(f"  → Kurung tutup ')', pop operator sampai ketemu '('")
            while not stack.is_empty() and stack.peek() != '(':
                popped = stack.pop()
                postfix.append(popped)
                print(f"     - Pop operator '{popped}' dari stack ke postfix")
            
            # Pop '(' dari stack (tapi tidak masuk ke postfix)
            if not stack.is_empty():
                stack.pop()  # Buang '('
                print(f"  → Buang '(' dari stack")
            
            print(f"  → Postfix sekarang: {' '.join(postfix)}")
        
        # CASE 5: Karakter adalah OPERATOR (+, -, *, /, ^)
        elif is_operator(char):
            # Finalisasi current_number jika ada
            if current_number:
                postfix.append(current_number)
                print(f"  → Finalisasi number sebelum operator: {current_number}")
                current_number = ""
            
            # Pop operator dari stack yang precedence-nya >= operator sekarang
            print(f"  → Operator '{char}' (precedence: {get_precedence(char)})")
            
            while (not stack.is_empty() and 
                   stack.peek() != '(' and 
                   get_precedence(stack.peek()) >= get_precedence(char)):
                
                popped = stack.pop()
                postfix.append(popped)
                print(f"     - Pop '{popped}' (precedence: {get_precedence(popped)}) dari stack ke postfix")
            
            # Push operator sekarang ke stack
            stack.push(char)
            print(f"  → Push operator '{char}' ke stack")
            print(f"  → Stack sekarang: {stack}")
            print(f"  → Postfix sekarang: {' '.join(postfix)}")
    
    # Jangan lupa: finalisasi current_number terakhir jika ada
    if current_number:
        postfix.append(current_number)
        print(f"\nFinalisasi number terakhir: {current_number}")
    
    # Pop semua operator yang tersisa di stack
    print(f"\nPop semua operator tersisa di stack:")
    while not stack.is_empty():
        popped = stack.pop()
        postfix.append(popped)
        print(f"  - Pop '{popped}' dari stack ke postfix")
    
    # Gabungkan list postfix menjadi string dengan spasi sebagai separator
    result = ' '.join(postfix)
    
    print(f"\n{'='*60}")
    print(f"HASIL KONVERSI:")
    print(f"Infix:   {expression}")
    print(f"Postfix: {result}")
    print(f"{'='*60}\n")
    
    return result


# ============================================================================
# TESTING SECTION
# ============================================================================

if __name__ == "__main__":
    """
    Testing Infix to Postfix Converter dengan berbagai kasus.
    """
    
    print("\n" + "="*60)
    print("TESTING INFIX TO POSTFIX CONVERTER")
    print("="*60)
    
    # Test cases: (infix, expected_postfix)
    test_cases = [
        ("3 + 4", "3 4 +"),
        ("3 + 4 * 2", "3 4 2 * +"),
        ("( 3 + 4 ) * 2", "3 4 + 2 *"),
        ("3 * 4 + 5", "3 4 * 5 +"),
        ("3 + 4 * 5 - 6", "3 4 5 * + 6 -"),
        ("( 3 + 4 ) * ( 5 - 6 )", "3 4 + 5 6 - *"),
        ("10 + 20 * 30", "10 20 30 * +"),
        ("( 5 + 6 ) * ( 7 + 8 )", "5 6 + 7 8 + *"),
    ]
    
    print("\nMenjalankan test cases...\n")
    
    passed = 0
    failed = 0
    
    for infix, expected in test_cases:
        result = infix_to_postfix(infix)
        
        # Cek apakah hasil sesuai expected
        if result == expected:
            print(f"✅ PASS")
            passed += 1
        else:
            print(f"❌ FAIL")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            failed += 1
        
        print()
    
    print("="*60)
    print(f"SUMMARY: {passed} passed, {failed} failed")
    print("="*60)