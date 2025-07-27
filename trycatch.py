def safe_diver_1(x, y):
    if y == 0:
        print("Cannot divide by zero")
        return None
    else:
        return x / y


def safe_diver_2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None


safe_diver_2(10, 0)
safe_diver_1(10, 0)


def read_file(filename):
    try:
        # 尝试打开并读取文件
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
    except FileNotFoundError as e:
        # 如果文件未找到，捕获异常，并命名为e
        print("文件未找到：", e)
    except Exception as e:
        # 捕获其他所有异常
        print("发生其他错误：", e)
    else:
        # 没有发生异常时执行
        print("文件读取成功，内容如下：")
        print(content)
    finally:
        # 无论是否发生异常都会执行
        try:
            file.close()
            print("文件已关闭。")
        except:
            print("文件未打开，无需关闭。")


# 测试
read_file("example.txt")
