from app import app
from flask import render_template,flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'pfeng'}
    posts=[
        {
            'author':{'nickname':'xiaoxia'},
            'body':'beautiful day'
        },
        {
            'author':{'nickname':'zhengxiong'},
            'body':'coder day'
        }
    ]
    htmlstr=render_template("child.html", title = "myblog", user = user, posts = posts)
    #print htmlstr
    return htmlstr

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    print('login called')
    if form.validate_on_submit():
        a='login request for OpenId = "' + form.openid.data + '";remember_me='+str(form.remember_me.data)
        print(a)
        flash(a)
        return redirect('/index')
    return render_template('login.html', 
                            title = 'Sign in', 
                            form = form,
                            providers = app.config['OPENID_PROVIDER'])

#创建书库的路由处理函数
@app.route('/bookstore')
def bookstore():
    print("bookstore called") #test
    #打印时间信息 test
    import time
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    return render_template('bookstore.html')