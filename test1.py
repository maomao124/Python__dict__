"""
 * Project name(项目名称)：Python__dict__
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:09
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    a = 1
    b = 2
    c = 3

    def __init__(self, a1, a2, a3) -> None:
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


if __name__ == '__main__':
    print(C.__dict__)
    c = C(4, 5, 6)
    print(c.__dict__)
    print(c.__dict__["a1"])
    c.__dict__["a2"] = 11
    print(c.__dict__)
