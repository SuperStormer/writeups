# security_question

Source: [index.html](index.html)

The site displays what appears to be a Stack Overflow question, with this code:

```python
@app.route('/getpoem')
def get_poem():
    poemname = request.args.get('name')

    if not poemname:
        return 'Please send a name query:\n' + str(os.listdir('poems')), 404

    poemdir     = os.path.join(os.getcwd(), 'poems')
    poempath    = os.path.join(poemdir, poemname)

    if '..' in poemname:
        return 'Illegal substring detected.', 403

    if not os.path.exists(poempath):
        return 'File not found.', 404

    return send_file(poempath)
```

It also mentions a `hidden_poem.txt` in the root directory that is presumably the flag. The code listing has one flaw. Quoting from the python docs, "If a component is an absolute path, all previous components are thrown away and joining continues from the absolute path component.". This means that `https://security.chal.uiuc.tf/getpoem?name=/hidden_poem.txt` gets us the flag.

Flag: uiuctf{str_join_is_weird_in_python_3}
