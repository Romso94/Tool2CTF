
<h1 align="center" id="title">OnePoint Detection Scanner</h1>

<p align="center"><img src="" alt="project-image" width="200"></p>

<p align='center' id="description">Python script to test an Endpoint on multiple url</p>

---

<h2>Why ❓</h2>

<p>Facilitate the detection and analysis of an endpoint misconfigurations. This tool allows for easy retrieval of responses from  an endpoint chosen, helping in identifying potential vulnerabilities or issues by scanning a list of url to identifie your endpoint misconfiguration.</p>

---

<h2>What 📝</h2>

<p>The script will generate a table like this:</p>

| URL | C0D3 | 
| --- | ---- | 
| http://example.com/xmlrpc.php | 200 | 
| http://example.com/xmlrpc.php | 404 |

---

<h2>🛠️ Installation Steps : </h2>

<p>First, you need Python installed (Python 3).</p>

<p>Then run these commands:</p>

```bash
>> git clone https://github.com/Romso94/Tool2CTF.git 
>> cd Tool2CTF/web/OnePointDetection/
>> pip install -r requirements.txt
```

<p>That's it! </p>

--- 

<h2>🪛 To Run the Script</h2>

<p>Specify the URL or a file with all URL:</p>

```python
>>> python OnePointDetection.py -f url.txt -o results -v -p test.php -or 200
```

<h4>Options:</h4>

```
    -h, --help, h, help      Affiche ce message d'aide et quitte
    -u URL, -U URL           Spécifie une URL unique à scanner
    -f FILE, -F FILE         Spécifie un fichier TXT contenant des URLs à scanner
    -o NAME, -O NAME         Spécifie le nom du fichier de sortie en HTML
    -v, -V                   Affiche des informations sur toutes les réponses
    -p OnePoint, -P OnePoint Spécifie le endpoint  à vérifier
    -or Code, -OR Code       Affiche uniquement les résultats avec le code de statut réponse HTTP/HTTPS spécifié
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