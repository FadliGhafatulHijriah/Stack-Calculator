"""
Postfix Expression Evaluator
=============================

File ini berisi algoritma untuk mengevaluasi (menghitung hasil) dari
ekspresi matematika dalam notasi POSTFIX menggunakan Stack.

CARA KERJA EVALUASI POSTFIX:
1. Scan expression dari kiri ke kanan
2. Jika ketemu ANGKA: push ke stack
3. Jika ketemu OPERATOR:
   - Pop 2 angka dari stack (operand2, operand1)
   - Hitung: operand1 OPERATOR operand2
   - Push hasil ke stack
4. Di akhir: angka terakhir di stack = hasil akhir

CONTOH:
Postfix: 3 4 +
1. Push 3 → Stack: [3]
2. Push 4 → Stack: [3, 4]
3. Ketemu '+' → Pop 4, Pop 3 → Hitung 3+4=7 → Push 7 → Stack: [7]
4. Hasil: 7

Author: Fadli Ghafatul Hijriah
Date: January 2025
"""

# Import Stack class
from Stack import Stack


def is_number(string):
    """
    Mengecek apakah string adalah angka (termasuk float/desimal).
    
    Args:
        string (str): String yang akan dicek
    
    Returns:
        bool: True jika string adalah angka, False jika bukan
    
    Example:
        is_number("123")    # True
        is_number("45.6")   # True
        is_number("+")      # False
        is_number("abc")    # False
    """
    try:
        # Coba convert ke float
        # Jika berhasil, berarti string adalah angka
        float(string)
        return True
    except ValueError:
        # Jika gagal (ValueError), berarti bukan angka
        return False


def apply_operator(operand1, operand2, operator):
    """
    Melakukan operasi matematika antara dua operand dengan operator tertentu.
    
    URUTAN PENTING:
    Karena kita pop dari stack, urutan operand terbalik!
    - operand2 = yang di-pop PERTAMA (top of stack)
    - operand1 = yang di-pop KEDUA
    
    Untuk operasi seperti pembagian dan pengurangan, urutan sangat penting!
    Contoh: 10 - 5 ≠ 5 - 10
    
    Args:
        operand1 (float): Operand pertama (yang di-pop kedua)
        operand2 (float): Operand kedua (yang di-pop pertama)
        operator (str): Operator matematika (+, -, *, /, ^)
    
    Returns:
        float: Hasil operasi
    
    Raises:
        ValueError: Jika operator tidak dikenal
        ZeroDivisionError: Jika terjadi pembagian dengan nol
    
    Example:
        apply_operator(10, 5, '+')  # Returns 15.0
        apply_operator(10, 5, '-')  # Returns 5.0  (10 - 5)
        apply_operator(10, 5, '*')  # Returns 50.0
        apply_operator(10, 5, '/')  # Returns 2.0  (10 / 5)
    """
    
    # Penjumlahan
    if operator == '+':
        result = operand1 + operand2
        print(f"     Operasi: {operand1} + {operand2} = {result}")
        return result
    
    # Pengurangan (URUTAN PENTING!)
    elif operator == '-':
        result = operand1 - operand2
        print(f"     Operasi: {operand1} - {operand2} = {result}")
        return result
    
    # Perkalian
    elif operator == '*':
        result = operand1 * operand2
        print(f"     Operasi: {operand1} * {operand2} = {result}")
        return result
    
    # Pembagian (URUTAN PENTING + CEK ZERO!)
    elif operator == '/':
        # Cek pembagian dengan nol
        if operand2 == 0:
            raise ZeroDivisionError("Error: Pembagian dengan nol tidak diperbolehkan!")
        
        result = operand1 / operand2
        print(f"     Operasi: {operand1} / {operand2} = {result}")
        return result
    
    # Pangkat (Power)
    elif operator == '^':
        result = operand1 ** operand2
        print(f"     Operasi: {operand1} ^ {operand2} = {result}")
        return result
    
    # Operator tidak dikenal
    else:
        raise ValueError(f"Error: Operator '{operator}' tidak dikenal!")


def evaluate_postfix(expression):
    """
    Mengevaluasi ekspresi postfix dan mengembalikan hasilnya.
    
    ALGORITMA:
    1. Buat stack kosong
    2. Scan setiap token (angka/operator) dari kiri ke kanan
    3. Jika token adalah ANGKA:
       - Convert ke float
       - Push ke stack
    4. Jika token adalah OPERATOR:
       - Pop dua angka dari stack (operand2 dulu, lalu operand1)
       - Hitung: operand1 OPERATOR operand2
       - Push hasil ke stack
    5. Di akhir: angka terakhir di stack adalah hasil akhir
    
    Args:
        expression (str): Ekspresi dalam notasi postfix
                         Contoh: "3 4 +"
    
    Returns:
        float: Hasil evaluasi
    
    Raises:
        ValueError: Jika expression invalid (tidak cukup operand, dll)
        ZeroDivisionError: Jika terjadi pembagian dengan nol
    
    Example:
        evaluate_postfix("3 4 +")           # Returns 7.0
        evaluate_postfix("3 4 2 * +")       # Returns 11.0
        evaluate_postfix("10 5 /")          # Returns 2.0
        evaluate_postfix("5 6 + 2 *")       # Returns 22.0
    """
    
    # Stack untuk menyimpan operand (angka-angka)
    stack = Stack()
    
    # Split expression menjadi tokens (dipisah spasi)
    # Contoh: "3 4 +" → ["3", "4", "+"]
    tokens = expression.split()
    
    print(f"\n{'='*60}")
    print(f"EVALUASI POSTFIX EXPRESSION")
    print(f"{'='*60}")
    print(f"Postfix: {expression}")
    print(f"Tokens: {tokens}")
    print(f"{'='*60}\n")
    
    # Scan setiap token
    for i, token in enumerate(tokens):
        
        print(f"Step {i+1}: Membaca token '{token}'")
        
        # CASE 1: Token adalah ANGKA
        if is_number(token):
            # Convert string ke float dan push ke stack
            number = float(token)
            stack.push(number)
            print(f"  → Angka ditemukan: {number}")
            print(f"  → Push {number} ke stack")
            print(f"  → Stack sekarang: {stack}")
        
        # CASE 2: Token adalah OPERATOR
        else:
            print(f"  → Operator ditemukan: '{token}'")
            
            # Cek apakah ada cukup operand di stack
            # Operator membutuhkan minimal 2 operand
            if stack.size() < 2:
                raise ValueError(f"Error: Tidak cukup operand untuk operator '{token}'!")
            
            # Pop dua operand dari stack
            # PENTING: Yang di-pop pertama = operand2 (kanan)
            #          Yang di-pop kedua = operand1 (kiri)
            operand2 = stack.pop()  # Top of stack (operand kanan)
            operand1 = stack.pop()  # Second from top (operand kiri)
            
            print(f"  → Pop operand2 (kanan): {operand2}")
            print(f"  → Pop operand1 (kiri): {operand1}")
            
            # Lakukan operasi
            result = apply_operator(operand1, operand2, token)
            
            # Push hasil ke stack
            stack.push(result)
            print(f"  → Push hasil {result} ke stack")
            print(f"  → Stack sekarang: {stack}")
        
        print()
    
    # Setelah semua token di-scan, stack harus berisi tepat 1 angka
    # Angka tersebut adalah hasil akhir
    
    if stack.is_empty():
        raise ValueError("Error: Expression kosong atau invalid!")
    
    if stack.size() > 1:
        raise ValueError(f"Error: Expression invalid! Stack masih berisi {stack.size()} angka.")
    
    # Pop hasil akhir
    final_result = stack.pop()
    
    print(f"{'='*60}")
    print(f"HASIL EVALUASI:")
    print(f"Postfix: {expression}")
    print(f"Result:  {final_result}")
    print(f"{'='*60}\n")
    
    return final_result


# ============================================================================
# TESTING SECTION
# ============================================================================

if __name__ == "__main__":
    """
    Testing Postfix Evaluator dengan berbagai kasus.
    """
    
    print("\n" + "="*60)
    print("TESTING POSTFIX EVALUATOR")
    print("="*60)
    
    # Test cases: (postfix_expression, expected_result)
    test_cases = [
        ("3 4 +", 7.0),                    # 3 + 4 = 7
        ("3 4 2 * +", 11.0),               # 3 + (4 * 2) = 11
        ("3 4 + 2 *", 14.0),               # (3 + 4) * 2 = 14
        ("10 5 /", 2.0),                   # 10 / 5 = 2
        ("10 5 -", 5.0),                   # 10 - 5 = 5
        ("5 6 + 7 8 + *", 165.0),          # (5+6) * (7+8) = 11 * 15 = 165
        ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5.0),  # Complex expression
        ("2 3 ^", 8.0),                    # 2^3 = 8
    ]
    
    print("\nMenjalankan test cases...\n")
    
    passed = 0
    failed = 0
    
    for postfix, expected in test_cases:
        try:
            result = evaluate_postfix(postfix)
            
            # Cek apakah hasil sesuai expected (dengan toleransi untuk float)
            if abs(result - expected) < 0.0001:  # Toleransi 0.0001 untuk floating point
                print(f"✅ PASS")
                passed += 1
            else:
                print(f"❌ FAIL")
                print(f"   Expected: {expected}")
                print(f"   Got:      {result}")
                failed += 1
        
        except Exception as e:
            print(f"❌ FAIL - Exception occurred")
            print(f"   Error: {e}")
            failed += 1
        
        print()
    
    # Test error cases
    print("\n" + "="*60)
    print("TESTING ERROR HANDLING")
    print("="*60 + "\n")
    
    # Test 1: Division by zero
    print("Test: Pembagian dengan nol")
    try:
        evaluate_postfix("10 0 /")
        print("❌ FAIL - Should have raised ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"✅ PASS - Error tertangkap: {e}\n")
    
    # Test 2: Invalid expression (not enough operands)
    print("Test: Expression invalid (kurang operand)")
    try:
        evaluate_postfix("3 +")
        print("❌ FAIL - Should have raised ValueError")
    except ValueError as e:
        print(f"✅ PASS - Error tertangkap: {e}\n")
    
    print("="*60)
    print(f"SUMMARY: {passed} passed, {failed} failed")
    print("="*60)