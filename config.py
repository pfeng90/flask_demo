CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDER=[
    {'name':'Baidu', 'url':'http://www.baidu.com'},
    {'name':'Google', 'url':'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo', 'url':'https://me.yahoo.com'},
    {'name':'Myopenid', 'url':'http://www.myopenid.com/<username>'},
    {'name':'Flick', 'url':'http://www.flickr.com/<username>'}
]