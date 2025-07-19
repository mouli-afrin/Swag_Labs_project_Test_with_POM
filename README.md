<h1> Playwright Automation for swag labgs project</h1>

<h2> Project Overview</h2>
<p>
This is a scalable, modular test automation framework built with <strong>Playwright</strong> and <strong>Pytest</strong>, following the <strong>Page Object Model (POM)</strong>. It automates login flows, product validation, cart functionality, and error handling on <a href="https://www.saucedemo.com" target="_blank">SauceDemo</a>.
</p>

<h2> Folder Structure</h2>
<pre>
project-root/
│
├── config/           # Global constants and logger
├── pages/            # POM classes (LoginPage, CartPage, ProductPage)
├── tests/            # Modular test cases
├── screenshots/      # Captured on failure
├── reports/          # Optional: HTML report outputs
├── conftest.py       # Pytest fixtures for browser/page
├── pytest.ini        # Pytest config
└── README.md         # Project documentation
</pre>

<h2>Setup Instructions</h2>
<ol>
  <li>Clone the repo:
    <pre>git clone https://github.com/your-username/your-repo-name.git</pre>
  </li>
  <li>Install dependencies:
    <pre>pip install -r requirements.txt<br>playwright install</pre>
  </li>
  <li>Run all tests:
    <pre>pytest -v -s -n auto</pre>
  </li>
  <li>Run a specific test:
    <pre>pytest -v -s tests/test_login.py</pre>
  </li>
   <li>Run for html report:
    <pre>pytest -v -s --html .\reports\report.html -n 7</pre>
  </li>
   <li>Run for specific browser:
    <pre>pytest -v -s --browser browserName</pre>
  </li>
</ol>

<h2> Environments</h2>
<ul>
  <li>Python ≥ 3.9</li>
  <li>Playwright ≥ 1.44</li>
  <li>Pytest + pytest-xdist + pytest-html</li>
</ul>

<h2> Features</h2>
<ul>
  <li>Modular Page Object structure</li>
  <li>Centralized configuration via <code>settings.py</code></li>
  <li>Explicit waits using <code>expect()</code> and <code>wait_for_selector()</code></li>
  <li>Failure screenshot capture with timestamps</li>
  <li>Parallel test execution with <code>pytest-xdist</code></li>
  <li>Structured logging with <code>logger.py</code></li>
</ul>

<h2> Test Scenarios Covered</h2>
<ol>
  <li>Valid login → asserts dashboard title</li>
  <li>Invalid login → asserts error message</li>
  <li>Product page → validates total product count and title presence</li>
  <li>Add to cart → validates badge and cart item</li>
</ol>

<h2>Screenshot Sample</h2>
<p><code>/screenshots/login_failed_1689024321.png</code></p>

<h2>Author</h2>
<p><strong>Mouli Afrin Proma</strong> – QA Intern | Samsung R&D Institute Bangladesh</p>

