
<p align="center"><h1 align="center">PAPERSCRAPER</h1></p>

<p align="center">
	<img src="https://img.shields.io/github/license/Zanadukhan/PaperScraper?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Zanadukhan/PaperScraper?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Zanadukhan/PaperScraper?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Zanadukhan/PaperScraper?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

This script uses selenium to scrape a given article, transform the text into speech using different TTS packages, and uploads them to your google drive for convenient retrieval for mobile device use.

---

##  Features

* Able to scrape text from different articles (New Yorker & Foreign Policy)
* Use Coqui-TTS or Piper-TTS based on different requirements (Speed vs Quality)
* Automatic upload of audio file to your google drive account

---

##  Project Structure

```sh
└── PaperScraper/
    ├── LICENSE.txt
    ├── README.MD
    ├── Scripts
    │   ├── __pycache__
    │   ├── article_scraper.py
    │   ├── audio_generation.py
    │   ├── drive_uploader.py
    │   └── main.py
    └── requirements.txt
```


###  Project Index
<details open>
	<summary><b><code>PAPERSCRAPER/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/LICENSE.txt'>LICENSE.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/README.MD'>README.MD</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Scripts Submodule -->
		<summary><b>Scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/Scripts/drive_uploader.py'>drive_uploader.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/Scripts/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/Scripts/audio_generation.py'>audio_generation.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/PaperScraper/blob/master/Scripts/article_scraper.py'>article_scraper.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with PaperScraper, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install PaperScraper using one of the following methods:

**Build from source:**

1. Clone the PaperScraper repository:
```sh
❯ git clone https://github.com/Zanadukhan/PaperScraper
```

2. Navigate to the project directory:
```sh
❯ cd PaperScraper
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run PaperScraper using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [ ] **`Implement unit tests`**: Test code and achieve coverage of 80%+
- [ ] **`Scrape multiple links`**: Allow user to provide multiple
- [ ] **`Add more supported sites`**: Expand the number of supported sites that the webscraper can handle
---

##  Contributing

- **💬 [Join the Discussions](https://github.com/Zanadukhan/PaperScraper/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Zanadukhan/PaperScraper/issues)**: Submit bugs found or log feature requests for the `PaperScraper` project.
- **💡 [Submit Pull Requests](https://github.com/Zanadukhan/PaperScraper/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Zanadukhan/PaperScraper
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Zanadukhan/PaperScraper/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Zanadukhan/PaperScraper">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT](https://choosealicense.com/licenses/mit/) License. For more details, refer to the LICENSE file.

---

##  Acknowledgments

- New Yorker
- Foreign Policy
- Pydrive2
- Selenium
- Torch
- Yapper-TTS
- Coqui-TTS
- webdriver-manager

---
