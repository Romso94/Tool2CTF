
<h1 align="center" id="title">XML-RPC Detection Scanner</h1>

<p align="center"><img src="" alt="project-image" width="200"></p>

<p align='center' id="description">Python script to test for XML-RPC Vulnerability</p>

---

<h2>Why ❓</h2>

<p>Facilitate the detection and analysis of XML-RPC  misconfigurations. This tool allows for easy retrieval of responses from  XML-RPC, helping in identifying potential vulnerabilities or issues.</p>

---

<h2>What 📝</h2>

<p>The script will generate a table like this:</p>

| URL | C0D3 | R3SP0NS3 |
| --- | ---- | -------- |
| http://example.com/xmlrpc.php | 200 | <pre>Formatted XML Response</pre> |
| http://example.com/xmlrpc.php | 404 | <pre>Not Found</pre> |

---

<h2>🛠️ Installation Steps : </h2>

<p>First, you need Python installed (Python 3).</p>

<p>Then run these commands:</p>

```bash
>> git clone https://github.com/Romso94/Tool2CTF.git 
>> cd Tool2CTF/web/WordPress/XMLRPC/
>> pip install -r requirements.txt
```

<p>That's it! </p>

--- 

<h2>🪛 To Run the Script</h2>

<p>Specify the URL or  a file with all URL:</p>

```python
>>> python xmlrpc_scanner.py -f urls.txt -o results -v
```

<h4>Options:</h4>

```
    -u URL: Specify an URL to scan
    -f FILE: Specify a TXT file containing  all urls to scan (example.txt for example)
    -o N4m3: Generate an output file in HTML with the specified name
    -v: Print detailed information about all responses
```
---

<h2>💻 Built with</h2>

Technologies used in the project:

Python
Requests
Tabulate

---


<h2>🛡️ License :</h2>
This project is licensed under the MIT License. 