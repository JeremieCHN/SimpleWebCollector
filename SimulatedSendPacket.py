#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
写于 2019-8-15 后续如果API有更新可能就不能用了
原网页
https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3
通过模拟发包的方式，让他执行代码并获取返回
"""

from urllib import request, parse
import json


def run_py3_code(code):
    data = parse.urlencode([
        ('code', code),
        ('language', 15),
        ('fileext', 'py3')])
    req = request.Request('https://tool.runoob.com/compile.php')
    with request.urlopen(req, data=data.encode('utf-8')) as f:
        status = f.status
        if status == 200:
            response_data = f.read().decode('utf-8')
            return json.loads(response_data)
        else:
            return None


if __name__ == '__main__':
    code = '#!/usr/bin/python3\nprint("Hello, World!")'
    res = run_py3_code(code)
    if res is not None:
        print('output:\n'+res['output'])
        print('errors:\n'+res['errors'])
