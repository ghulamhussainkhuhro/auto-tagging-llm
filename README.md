# 🧠 Auto-Tagging Support Tickets Using LLMs

Automatically classify and tag support tickets into meaningful categories using zero-shot and few-shot techniques with Azure OpenAI.

---

## 📌 Objective

To develop an intelligent support system that uses Large Language Models (LLMs) to **automatically tag incoming customer support tickets** into relevant categories — improving efficiency for support agents and reducing manual effort.

---

## 🧰 Tech Stack

- **Python**
- **Azure OpenAI (GPT-4 / GPT-3.5 via Langchain)**
- **Langchain**
- **FAISS (Vector store)**
- **Jupyter Notebook** for experimentation
- **VS Code** for development

---

## 🗂️ Dataset

- `support_tickets.json`: Free-text customer support messages.
- Each ticket contains an `id` and a `message`.

---

## 🎯 Methodology

| Phase                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 🧹 **Preprocessing**      | Cleaned and loaded JSON support tickets                                     |
| 🧠 **Zero-Shot Inference**| Used Azure GPT to predict top 3 categories without prior training            |
| 🧪 **Few-Shot Prompting** | Enhanced accuracy by adding labeled examples directly into the prompt        |
| 📈 **Evaluation**         | Compared tags, checked invalid predictions, and exported labeled output     |

---

## 🏷️ Support Tag Categories

```text
1. Billing Issue
2. Technical Problem
3. Account Access
4. Feature Request
5. General Inquiry
6. Bug Report
7. Refund Request
8. Subscription Management


````markdown
## 📂 Project Structure, Evaluation, and How to Run

```bash
auto-tagging-llm/
│
├── data/                      # Input raw tickets
│   └── support_tickets.json
│
├── results/                   # Tagged output
│   └── tagged_tickets.json
│
├── src/                       
│   └── tagging_pipeline.py    # Main tagging logic
│
├── notebooks/                 
│   └── exploration.ipynb      # Zero-shot vs few-shot, Evaluation, Summary
│
├── run.py                     # Main runner script
├── requirements.txt           
└── README.md                  # You're here!
````

### 🧪 Evaluation

* Applied basic string checks and tag validations
* Filtered for unexpected or out-of-category predictions
* Exported final results in `results/tagged_tickets.json`
* 📝 For detailed insights and results comparison, see `notebooks/exploration.ipynb`

### 🚀 Key Learnings

✅ Prompt Engineering
✅ Zero-shot Classification
✅ Few-shot Prompt Tuning
✅ Azure OpenAI Integration
✅ Real-world NLP Application

### 💡 Future Enhancements

* Add vector search using FAISS for semantic similarity matching
* Integrate feedback loop from human-labeled corrections
* Fine-tune a small open-source model on custom ticket dataset

### 📎 How to Run

```bash
# 1. Clone repo & install requirements
git clone https://github.com/ghulamhussainkhuhro/auto-tagging-llm.git
cd auto-tagging-llm
pip install -r requirements.txt

# 2. Configure Azure OpenAI API in .env
# Example:
# AZURE_OPENAI_API_KEY=...
# AZURE_OPENAI_ENDPOINT=...

# 3. Run the pipeline
python run.py
```

---

### 🔗 Connect with Me

Made with ❤️ by **\[Your Name]**
📧 [your.email@example.com](mailto:ghulamhussain.developer@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/ghulamhussainkhuhro) | [GitHub](https://github.com/ghulamhussainkhuhro)

```


