#檔案放置python file同一目錄下
'''
file = open("hello.txt", "r") #open r參數:檔案唯讀
print(file.read()) #讀全部內容的
print(file.read(10)) #讀幾個字
'''
file = open("demo.txt", "w") #a 不管檔案存在與否，原本內容+write文字
file.write("Now the file has one more line!\n")
file.write("line 2\n")

# a 以外也可以用 x 或 w ，
# x 是file“必須不存在”，加入x這個參數就會幫你建立這個檔案
# w 不管檔案存不存在，就會把原本的內容全部重洗掉然後加入