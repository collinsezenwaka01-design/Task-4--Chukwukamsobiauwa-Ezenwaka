# Task-4--Chukwukamsobiauwa-Ezenwaka
# My Project 4: Azure Serverless Cost Calculator API

This project implements the serverless cost calculator backend API using Python and Azure Functions. The logic extracts two integer variables, calculates their sum, and returns a structured response without needing a traditional database or virtual machine running 24/7.

## 📊 The "Frustration & Confusion" Counter
Deploying serverless architecture under a tight deadline comes with its fair share of hurdles! Here is the honest tally of the roadblocks hit and overcome during this deployment:

* **Azure screaming that "Free Trial doesn't support Premium plans":** 1 time ❌
* **Azure complaining about missing subscription provider registrations:** 1 time 🛑
* **Typing the resource group name wrong in the CLI terminal:** 1 time ⌨️
* **NPM blocking global installation due to `allow-scripts` security flags:** 1 time 🛡️
* **Windows path environment completely refusing to recognize the global `func` command:** 1 time ❌
* **UCRT64 environment throwing `archive cannot contain itself` tar format loops:** 2 times 🌀
* **Bash terminal missing the native `zip` tool command binary entirely:** 1 time 🔍
* **Bypassing local environment tool bugs by bundling via PowerShell and streaming directly:** 1 time ⚡
* **Total Times Frustrated & Confused:** **9 times** 🤯
* **Beating the ticking clock and hitting that glorious 100% upload mark:** **Priceless!** 🏁🎉

---

## 🛠️ Infrastructure Details
* **Cloud Platform:** Microsoft Azure
* **Service Type:** Azure Function Apps (Serverless)
* **Hosting Plan:** Consumption (Linux)
* **Runtime Stack:** Python 3.11
* **Deployment Method:** Direct Zip Deployment via Azure CLI (`az functionapp deployment source config-zip`)

-
