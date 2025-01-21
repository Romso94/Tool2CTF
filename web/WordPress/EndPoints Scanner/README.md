---

<h1 align="center" id="title">WP Ju1cy Sc4nn3r</h1>

<p align="center"><img src="" alt="project-image" width="200"></p>

<p align='center' id="description">Python script to scan and test various WordPress endpoints for responses.</p>

---

<h2>Why ❓</h2>

<p>Facilitate the detection and analysis of WordPress endpoints misconfiguration. This tool allows for easy retrieval of responses from various WordPress endpoints, helping in identifying potential vulnerabilities or issues.</p>

---

<h2>What 📝</h2>

<p>The script will generate a table like this:</p>

| URL | R3SP0NS3 |
| --- | -------- |
| http://example.com/wp-admin.php | 200 |
| http://example.com/wp-login.php | 404 |
| http://example.com/wp-json/wp/v2/posts | 200 |

---

<h2>🛠️ Installation Steps : </h2>

<p>First, you need Python installed (Python 3).</p>

<p>Then run those commands : </p>

```bash
>> git clone https://github.com/Romso94/Tool2CTF.git 
>> cd 'Tool2CTF/web/WordPress/EndPoints Scanner/' 
>> pip install -r requirements.txt
```

<p>That's it!</p>

---

<h2>🪛 To Run the Script</h2>
<p>
Specify the base URL and optionally a file with additional endpoints:
</p>

```bash
>> python WP_JU1CY_SC4NN3R.py -u http://example.com -f endpoints.txt -o -v
```

Options:

    -u URL: Specify the base URL to scan
    -f FILE: Specify a TXT file containing additional endpoints to scan
    -o: Generate an output file in HTML
    -v: Print detailed information about all responses

---

<h2>💡 Stay Up-to Date</h2>

To update the list of endpoints locally, just follow these steps:

1. Edit the WP_Ju1cy_3ndp01nts list in the script to add or remove endpoints.
2. Save the changes and rerun the script.

---

<h2>💻 Built with</h2>

Technologies used in the project:

    Python
    Requests
    Tabulate

---

<h2>Future : </h2>

Future improvements could include:

    Adding more WordPress endpoints
    Improving error handling and logging
    Integrating with other security tools

---

<h2>🛡️ License : </h2>
This project is licensed under the MIT License. 