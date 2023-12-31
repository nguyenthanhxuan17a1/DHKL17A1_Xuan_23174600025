with open ("HumptyDumpty.txt",'w',encoding='utf-8')as f:
    f.write("HumpyDumpty sat on a wall\n")
    f.write('HumptyDummpty had a great fall\n')
    f.write("All the king's horses and all the king's men\n")
    f.write("Couldn't put Humpty together again.\n")
    f.close()

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Không tìm thấy tập tin {filename}."
    except Exception as e:
        return f"Lỗi: {e}"
    
def main():
    try:
        filename = input("Nhập tên tập tin: ")
        content = read_file(filename)
        print(f"Nội dung tập tin {filename}:")
        print(content)
    except KeyboardInterrupt:
        print("\nChương trình đã bị ngừng bởi người dùng.")

if __name__ == "__main__":
    main()