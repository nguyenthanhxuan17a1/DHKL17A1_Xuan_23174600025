with open ("HumptyDumpty.txt",'w',encoding='utf-8')as f:
    f.write("HumpyDumpty sat on a wall,\n")
    f.write('HumptyDummpty had a great fall.\n')
    f.write("All the king's horses and all the king's men\n")
    f.write("Couldn't put Humpty together again.")
    
# mo_doc_thong_ke_tap_tin.py

def read_report_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            chars = len(content)

            report = f"Content of file: {content} -----\nReport: Lines/ Words/ Chars--- Lines: {len(lines)}, Words: {len(words)}, Chars: {chars}"

            return report
    except FileNotFoundError:
        return "File not found."
# xu_ly_tap_tin.py



def main():
    filename = input("Nhập tên tập tin: ")
    result = read_report_file(filename)
    print(result)

if __name__ == "__main__":
    main()