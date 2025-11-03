import sys

class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new_node):
        if new_node is not None:
            new_node.link = self.link
            self.link = new_node

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[번호: {self.book_id}] 제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}"
    
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def find_by_title(self, title):
        curr = self.head
        while curr is not None:
            if curr.data.title == title:
                return curr.data
            curr = curr.link
        return None

    def find_pos_by_title(self, title):
        if self.isEmpty():
            return None

        if self.head.data.title == title:
            return

        prev = self.head
        curr = self.head.link
        while curr is not None:
            if curr.data.title == title:
                return prev
            prev = curr
            curr = curr.link
        
        return None

    def find_by_id(self, book_id):
        curr = self.head
        while curr is not None:
            if curr.data.book_id == book_id:
                return curr.data
            curr = curr.link
        return None

    def get_last_node(self):
        if self.isEmpty():
            return None
        curr = self.head
        while curr.link is not None:
            curr = curr.link
        return curr

    def display_all(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        
        print("\n--- [ 전체 도서 목록 ] ---")
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.link
        print("--------------------------\n")

class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()

    def add_book(self):
        try:
            book_id = int(input("  > 책 번호 (숫자): ").strip())
            title = input("  > 책 제목: ").strip()
            author = input("  > 저자: ").strip()
            year = int(input("  > 출판 연도 (숫자): ").strip())
            
            if not title or not author:
                print("오류: 책 제목과 저자는 공백일 수 없습니다.")
                return

            if self.book_list.find_by_id(book_id) is not None:
                print(f"오류: 이미 존재하는 책 번호({book_id})입니다. 추가에 실패했습니다.")
                return

            new_book = Book(book_id, title, author, year)
            new_node = Node(new_book)

            if self.book_list.isEmpty():
                self.book_list.head = new_node
            else:
                last_node = self.book_list.get_last_node()
                last_node.append(new_node)

            print(f"성공: '{title}' 도서가 성공적으로 추가되었습니다.")

        except ValueError:
            print("오류: 책 번호와 출판 연도는 숫자로만 입력해야 합니다.")
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}")

    def remove_book(self):
        title = input("  > 삭제할 책 제목: ").strip()
        if not title:
            print("오류: 책 제목을 입력해주세요.")
            return
        
        pos = self.book_list.find_pos_by_title(title)

        if pos is None:
            print(f"오류: '{title}' 제목의 도서를 찾을 수 없습니다. 삭제에 실패했습니다.")
        elif pos == 'head':
            self.book_list.head = self.book_list.head.link
            print(f"성공: '{title}' 도서를 삭제했습니다.")
        else:
            pos.popNext()
            print(f"성공: '{title}' 도서를 삭제했습니다.")

    def search_book(self):
        title = input("  > 조회할 책 제목: ").strip()
        if not title:
            print("오류: 책 제목을 입력해주세요.")
            return

        book_data = self.book_list.find_by_title(title)

        if book_data:
            print("\n--- [ 도서 조회 결과 ] ---")
            print(book_data)
            print("--------------------------\n")
        else:
            print(f"오류: '{title}' 제목의 도서를 찾을 수 없습니다.")

    def display_books(self):
        self.book_list.display_all()

    def run(self):
        print("========================================")
        print("  단순 연결 리스트 활용 - 도서 관리 프로그램  ")
        print("========================================")

        while True:
            print("\n[ 메인 메뉴 ]")
            print("  1. 도서 추가")
            print("  2. 도서 삭제 (책 제목으로)")
            print("  3. 도서 조회 (책 제목으로)")
            print("  4. 전체 도서 목록 출력")
            print("  5. 프로그램 종료")
            
            choice = input("  > 메뉴 선택: ").strip()

            if choice == '1':
                print("\n[ 1. 도서 추가 ]")
                self.add_book()
            elif choice == '2':
                print("\n[ 2. 도서 삭제 ]")
                self.remove_book()
            elif choice == '3':
                print("\n[ 3. 도서 조회 ]")
                self.search_book()
            elif choice == '4':
                print("\n[ 4. 전체 도서 목록 ]")
                self.display_books()
            elif choice == '5':
                print("\n프로그램을 종료합니다.")
                sys.exit()
            else:
                print("오류: 1~5 사이의 번호를 입력해주세요.")

if __name__ == "__main__":
    app = BookManagement()
    app.run()