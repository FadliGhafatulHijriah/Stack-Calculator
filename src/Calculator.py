"""
Stack Calculator - Main Program
================================

Program kalkulator yang menggunakan Stack untuk mengevaluasi ekspresi matematika.

CARA KERJA:
1. User input expression dalam notasi INFIX (normal math)
2. Program convert INFIX → POSTFIX
3. Program evaluate POSTFIX → HASIL
4. Tampilkan hasil

FITUR:
- Support operator: +, -, *, /, ^
- Support tanda kurung: ( )
- Support angka desimal
- Error handling yang baik
- Step-by-step visualization (optional)

Author: Fadli Ghafatul Hijriah
Date: Februari 2026
"""

# Import semua module yang ada
from Stack import Stack
from Infix_to_Postfix import infix_to_postfix
from Postfix_Evaluator import evaluate_postfix


class Calculator:
    """
    Kelas Calculator yang mengintegrasikan semua komponen.
    
    Attributes:
        history (list): Menyimpan riwayat perhitungan
        show_steps (bool): Flag untuk menampilkan langkah-langkah detail
    """
    
    def __init__(self, show_steps=False):
        """
        Initialize calculator.
        
        Args:
            show_steps (bool): Jika True, tampilkan step-by-step process
        """
        # List untuk menyimpan history perhitungan
        self.history = []
        
        # Flag untuk show/hide detailed steps
        self.show_steps = show_steps
    
    
    def calculate(self, infix_expression):
        """
        Menghitung hasil dari ekspresi matematika.
        
        WORKFLOW:
        1. Validate input
        2. Convert infix → postfix
        3. Evaluate postfix → result
        4. Save to history
        5. Return result
        
        Args:
            infix_expression (str): Ekspresi matematika dalam notasi infix
                                   Contoh: "3 + 4 * 2"
        
        Returns:
            float: Hasil perhitungan
        
        Raises:
            ValueError: Jika expression invalid
            ZeroDivisionError: Jika pembagian dengan nol
        
        Example:
            calc = Calculator()
            result = calc.calculate("3 + 4")      # Returns 7.0
            result = calc.calculate("(5+6) * 2")  # Returns 22.0
        """
        
        print("\n" + "="*70)
        print("STACK CALCULATOR - COMPUTATION")
        print("="*70)
        
        # Step 1: Validate input
        if not infix_expression or infix_expression.strip() == "":
            raise ValueError("Error: Expression kosong!")
        
        print(f"Input (Infix):  {infix_expression}")
        
        # Step 2: Convert infix to postfix
        # Jika show_steps=False, suppress output dari infix_to_postfix
        if not self.show_steps:
            # Temporary disable printing
            import sys
            from io import StringIO
            old_stdout = sys.stdout
            sys.stdout = StringIO()
        
        try:
            postfix_expression = infix_to_postfix(infix_expression)
        finally:
            if not self.show_steps:
                # Restore stdout
                sys.stdout = old_stdout
        
        print(f"Postfix:        {postfix_expression}")
        
        # Step 3: Evaluate postfix expression
        if not self.show_steps:
            # Temporary disable printing
            old_stdout = sys.stdout
            sys.stdout = StringIO()
        
        try:
            result = evaluate_postfix(postfix_expression)
        finally:
            if not self.show_steps:
                # Restore stdout
                sys.stdout = old_stdout
        
        print(f"Result:         {result}")
        print("="*70)
        
        # Step 4: Save to history
        self.history.append({
            'infix': infix_expression,
            'postfix': postfix_expression,
            'result': result
        })
        
        # Step 5: Return result
        return result
    
    
    def show_history(self):
        """
        Menampilkan riwayat perhitungan.
        
        Example:
            calc = Calculator()
            calc.calculate("3 + 4")
            calc.calculate("5 * 6")
            calc.show_history()
        """
        print("\n" + "="*70)
        print("CALCULATION HISTORY")
        print("="*70)
        
        if not self.history:
            print("No history yet. Start calculating!")
        else:
            for i, entry in enumerate(self.history, 1):
                print(f"\n{i}. Expression: {entry['infix']}")
                print(f"   Postfix:    {entry['postfix']}")
                print(f"   Result:     {entry['result']}")
        
        print("\n" + "="*70)
    
    
    def clear_history(self):
        """
        Menghapus semua riwayat perhitungan.
        """
        self.history = []
        print("History cleared!")


def print_banner():
    """
    Menampilkan banner welcome program.
    """
    print("\n" + "="*70)
    print(" " * 20 + "STACK CALCULATOR")
    print(" " * 15 + "by Fadli Ghafatul Hijriah")
    print("="*70)
    print("\nFeatures:")
    print("  ✓ Support operators: +, -, *, /, ^")
    print("  ✓ Support parentheses: ( )")
    print("  ✓ Support decimal numbers")
    print("  ✓ Step-by-step visualization")
    print("  ✓ Calculation history")
    print("\nNote: Pisahkan angka dan operator dengan SPASI")
    print("      Contoh: '3 + 4 * 2' atau '( 5 + 6 ) * 2'")
    print("="*70 + "\n")


def print_menu():
    """
    Menampilkan menu pilihan.
    """
    print("\nMenu:")
    print("  1. Calculate expression")
    print("  2. Show calculation history")
    print("  3. Clear history")
    print("  4. Toggle step-by-step mode")
    print("  5. Exit")
    print("-" * 70)


def interactive_mode():
    """
    Mode interaktif - user bisa input expression secara berulang.
    """
    # Create calculator instance
    calc = Calculator(show_steps=False)
    
    # Print welcome banner
    print_banner()
    
    # Main loop
    while True:
        print_menu()
        choice = input("Pilih menu (1-5): ").strip()
        
        # Menu 1: Calculate
        if choice == '1':
            print("\nMasukkan ekspresi matematika:")
            print("(Gunakan SPASI antara angka dan operator)")
            print("Contoh: 3 + 4 * 2")
            print("Contoh: ( 5 + 6 ) * ( 7 - 2 )")
            
            expression = input("\nExpression: ").strip()
            
            try:
                result = calc.calculate(expression)
                print(f"\n🎯 Hasil: {result}")
            
            except ValueError as e:
                print(f"\n❌ Error: {e}")
            
            except ZeroDivisionError as e:
                print(f"\n❌ Error: {e}")
            
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
        
        # Menu 2: Show history
        elif choice == '2':
            calc.show_history()
        
        # Menu 3: Clear history
        elif choice == '3':
            calc.clear_history()
        
        # Menu 4: Toggle steps
        elif choice == '4':
            calc.show_steps = not calc.show_steps
            status = "ON" if calc.show_steps else "OFF"
            print(f"\nStep-by-step mode: {status}")
        
        # Menu 5: Exit
        elif choice == '5':
            print("\nTerima kasih telah menggunakan Stack Calculator!")
            print("Made with ❤️ by Fadli Ghafatul Hijriah")
            print("="*70 + "\n")
            break
        
        # Invalid choice
        else:
            print("\n❌ Pilihan tidak valid! Pilih 1-5.")


def quick_test():
    """
    Quick test mode - test beberapa expression langsung.
    """
    print("\n" + "="*70)
    print("QUICK TEST MODE")
    print("="*70 + "\n")
    
    # Create calculator
    calc = Calculator(show_steps=True)
    
    # Test expressions
    test_expressions = [
        "3 + 4",
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "10 / 5 + 3",
        "( 5 + 6 ) * ( 7 - 2 )",
        "2 ^ 3 + 1"
    ]
    
    print("Testing the following expressions:\n")
    for expr in test_expressions:
        print(f"  - {expr}")
    print()
    
    # Calculate each
    for expr in test_expressions:
        try:
            calc.calculate(expr)
            print()
        except Exception as e:
            print(f"Error: {e}\n")
    
    # Show history
    calc.show_history()


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    """
    Entry point program.
    
    User bisa pilih:
    1. Interactive mode - input expression berulang kali
    2. Quick test mode - test beberapa expression otomatis
    """
    
    print("\n" + "="*70)
    print("STACK CALCULATOR - MODE SELECTION")
    print("="*70)
    print("\n1. Interactive Mode - Input your own expressions")
    print("2. Quick Test Mode  - Run automated tests")
    print("3. Exit")
    
    choice = input("\nPilih mode (1-3): ").strip()
    
    if choice == '1':
        interactive_mode()
    elif choice == '2':
        quick_test()
    elif choice == '3':
        print("\nGoodbye! 👋\n")
    else:
        print("\nInvalid choice! Running interactive mode...\n")
        interactive_mode()