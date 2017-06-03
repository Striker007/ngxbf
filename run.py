# -*- coding: utf-8 -*-

# from pyparsing import Word, alphas
import etcd3  # or consul
# from var_dump import var_dump


if __name__ == "__main__":
    etcd = etcd3.client()
    result = etcd.get('mykey')
    # var_dump(result)
    print(result[0])

    # greet = Word(alphas) + "," + Word(alphas) + "!"  # <-- grammar defined here
    # hello = "Hello, World!"
    # print (greet.parseString(hello))
