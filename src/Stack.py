"""
Stack Data Structure Implementation
====================================

File ini berisi implementasi Stack (Tumpukan) dari scratch tanpa menggunakan
library bawaan Python. Stack adalah struktur data Linear yang mengikuti
prinsip LIFO (Last In First Out) - elemen terakhir yang masuk adalah
elemen pertama yang keluar.

Author: Fadli Ghafatul Hijriah
Date: Februari 2026
"""


class Stack:
    """
    Kelas Stack untuk implementasi struktur data tumpukan.
    
    Stack bekerja seperti tumpukan piring:
    - Push: Menambah piring di atas (top)
    - Pop: Mengambil piring dari atas (top)
    - Peek: Melihat piring paling atas tanpa mengambilnya
    
    Attributes:
        items (list): List untuk menyimpan elemen-elemen stack
    """
    
    def __init__(self):
        """
        Constructor untuk membuat stack kosong.
        
        Ketika stack dibuat, kita initialize dengan list kosong.
        List ini akan bertindak sebagai container untuk menyimpan data.
        """
        # Inisialisasi list kosong untuk menyimpan elemen stack
        self.items = []
    
    
    def push(self, item):
        """
        Menambahkan item ke bagian atas stack (top).
        
        Operasi push menambahkan elemen baru ke posisi paling atas.
        Time complexity: O(1) - konstan, karena append() di Python adalah O(1)
        
        Args:
            item: Elemen yang akan ditambahkan ke stack (bisa angka, string, dll)
        
        Example:
            stack = Stack()
            stack.push(5)    # Stack: [5]
            stack.push(10)   # Stack: [5, 10]
            stack.push(15)   # Stack: [5, 10, 15]
        """
        # Gunakan append() untuk menambah item di akhir list
        # Akhir list = top of stack
        self.items.append(item)
        
        # Print untuk debugging (optional, bisa di-comment)
        # print(f"Pushed {item} to stack. Current stack: {self.items}")
    
    
    def pop(self):
        """
        Menghapus dan mengembalikan item dari bagian atas stack (top).
        
        Operasi pop mengambil elemen paling atas dan menghapusnya dari stack.
        Time complexity: O(1) - konstan
        
        Returns:
            Item yang diambil dari top of stack
        
        Raises:
            IndexError: Jika stack kosong (tidak ada item untuk di-pop)
        
        Example:
            stack = Stack()
            stack.push(5)
            stack.push(10)
            item = stack.pop()  # Returns 10, Stack sekarang: [5]
        """
        # Cek dulu apakah stack kosong
        if self.is_empty():
            # Jika kosong, raise error dengan pesan yang jelas
            raise IndexError("Pop from empty stack! Stack sudah kosong, tidak ada item untuk diambil.")
        
        # Jika tidak kosong, ambil dan hapus item terakhir
        # pop() tanpa argument mengambil elemen terakhir
        return self.items.pop()
    
    
    def peek(self):
        """
        Melihat item di bagian atas stack tanpa menghapusnya.
        
        Berguna untuk cek item teratas tanpa mengubah stack.
        Time complexity: O(1) - konstan
        
        Returns:
            Item di top of stack (tanpa menghapusnya)
        
        Raises:
            IndexError: Jika stack kosong
        
        Example:
            stack = Stack()
            stack.push(5)
            stack.push(10)
            top = stack.peek()  # Returns 10, Stack tetap: [5, 10]
        """
        # Cek apakah stack kosong
        if self.is_empty():
            raise IndexError("Peek from empty stack! Stack kosong, tidak ada item untuk dilihat.")
        
        # Return item terakhir tanpa menghapusnya
        # Index -1 = elemen terakhir dalam list Python
        return self.items[-1]
    
    
    def is_empty(self):
        """
        Mengecek apakah stack kosong atau tidak.
        
        Time complexity: O(1) - konstan
        
        Returns:
            bool: True jika stack kosong, False jika ada isinya
        
        Example:
            stack = Stack()
            print(stack.is_empty())  # True
            stack.push(5)
            print(stack.is_empty())  # False
        """
        # Cara 1: Cek panjang list
        # return len(self.items) == 0
        
        # Cara 2: Gunakan truthiness Python (lebih Pythonic)
        # Empty list = False, Non-empty list = True
        # Maka kita gunakan 'not' untuk balik hasilnya
        return len(self.items) == 0
    
    
    def size(self):
        """
        Mengembalikan jumlah item dalam stack.
        
        Time complexity: O(1) - konstan
        
        Returns:
            int: Jumlah elemen dalam stack
        
        Example:
            stack = Stack()
            print(stack.size())  # 0
            stack.push(5)
            stack.push(10)
            print(stack.size())  # 2
        """
        # Return panjang list
        return len(self.items)
    
    
    def clear(self):
        """
        Mengosongkan stack (menghapus semua elemen).
        
        Time complexity: O(1) - konstan (assignment baru)
        
        Example:
            stack = Stack()
            stack.push(5)
            stack.push(10)
            stack.clear()
            print(stack.is_empty())  # True
        """
        # Cara mudah: assign list baru yang kosong
        self.items = []
    
    
    def __str__(self):
        """
        String representation dari stack untuk printing.
        
        Method ini dipanggil ketika kita print(stack).
        Berguna untuk debugging dan melihat isi stack.
        
        Returns:
            str: Representasi string dari stack
        
        Example:
            stack = Stack()
            stack.push(5)
            stack.push(10)
            print(stack)  # Output: Stack: [5, 10] (Top: 10)
        """
        # Jika stack kosong
        if self.is_empty():
            return "Stack: [] (Empty)"
        
        # Jika ada isi, tampilkan isi dan top element
        return f"Stack: {self.items} (Top: {self.peek()})"
    
    
    def __repr__(self):
        """
        Official string representation untuk debugging.
        
        Returns:
            str: Representasi teknis dari stack
        """
        return f"Stack({self.items})"


# ============================================================================
# TESTING SECTION - Untuk memastikan Stack bekerja dengan benar
# ============================================================================

if __name__ == "__main__":
    """
    Main function untuk testing Stack implementation.
    
    Bagian ini hanya akan dijalankan jika file ini dijalankan langsung
    (bukan di-import sebagai module).
    """
    
    print("=" * 60)
    print("TESTING STACK IMPLEMENTATION")
    print("=" * 60)
    print()
    
    # Test 1: Membuat stack dan cek apakah kosong
    print("Test 1: Membuat stack baru")
    stack = Stack()
    print(f"Stack kosong? {stack.is_empty()}")  # Should be True
    print(f"Ukuran stack: {stack.size()}")      # Should be 0
    print(stack)
    print()
    
    # Test 2: Push beberapa elemen
    print("Test 2: Push elemen 5, 10, 15, 20")
    stack.push(5)
    print(f"Setelah push 5: {stack}")
    
    stack.push(10)
    print(f"Setelah push 10: {stack}")
    
    stack.push(15)
    print(f"Setelah push 15: {stack}")
    
    stack.push(20)
    print(f"Setelah push 20: {stack}")
    print()
    
    # Test 3: Peek (lihat top tanpa hapus)
    print("Test 3: Peek (lihat elemen teratas)")
    top_item = stack.peek()
    print(f"Elemen teratas: {top_item}")
    print(f"Stack setelah peek: {stack}")  # Stack tidak berubah
    print()
    
    # Test 4: Pop (ambil dan hapus elemen teratas)
    print("Test 4: Pop (ambil elemen teratas)")
    popped = stack.pop()
    print(f"Item yang di-pop: {popped}")
    print(f"Stack setelah pop: {stack}")
    print()
    
    # Test 5: Pop beberapa kali
    print("Test 5: Pop beberapa kali")
    print(f"Pop: {stack.pop()}")
    print(f"Stack sekarang: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack sekarang: {stack}")
    print()
    
    # Test 6: Size
    print("Test 6: Cek ukuran stack")
    print(f"Ukuran stack: {stack.size()}")
    print()
    
    # Test 7: Clear stack
    print("Test 7: Clear stack")
    stack.clear()
    print(f"Stack setelah clear: {stack}")
    print(f"Stack kosong? {stack.is_empty()}")
    print()
    
    # Test 8: Error handling - Pop dari stack kosong
    print("Test 8: Error handling - Pop dari stack kosong")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error tertangkap: {e}")
    print()
    
    # Test 9: Push dengan tipe data berbeda
    print("Test 9: Stack dengan tipe data berbeda")
    stack.push(5)          # Integer
    stack.push("Hello")    # String
    stack.push(3.14)       # Float
    stack.push([1, 2, 3])  # List
    print(f"Stack dengan berbagai tipe: {stack}")
    print()
    
    print("=" * 60)
    print("SEMUA TEST SELESAI! ✅")
    print("=" * 60)