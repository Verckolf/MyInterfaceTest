
def process(request, **kwargs):
    # print("func process start!!!")
    # print(request)
    # print(kwargs)
    app = kwargs.pop('app', None)
    fun = kwargs.pop('function', None)
    index = kwargs.pop('id', None)

    if app == 'api' or app == 'admin':
        app = 'ApiManager'
    try:
        app = __import__("%s.views" % app)
        view = getattr(app, 'views')
        fun = getattr(view, fun)

        # 执行view.py中的函数，并获取其返回值
        result = fun(request, index) if index else fun(request)
    except (ImportError, AttributeError):
        raise
    return result
