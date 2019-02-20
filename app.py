import web

# urls 变量：
# 1: url 正则模式
# 2: 接受请求的类名称，如index, view, welcomes.hello(welcomes模块的hello类)，或者get_\1。
#   \1 会被正则表达式捕捉到的内容替换，剩下来捕捉的的内容将被传递到你的函数中去。
urls = (
    '/', 'index'
)
app = web.application(urls, globals())


class index:
    def GET(self):
        return "Hello, web.py!"


if __name__ == '__main__':
    try:
        app.run()
    except StopIteration as e:
        print(e)

