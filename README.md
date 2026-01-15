**Set up the environment**
**Prerequisites**
Python 3.8+
VS Code (or any IDE)
Internet connection
**Steps**
# Install Playwright
pip install playwright
# Install browser binaries
playwright install
**Verify installation**
playwright --version

**Challenges faced**
Cart icon opens mini cart popup instead of full cart page
Some elements had changing text and spacing
Needed to handle waits properly

**test design decisions**
Chose Playwright for fast execution & auto-wait
Used XPath locators for accuracy

