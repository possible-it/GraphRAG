# 医学数据集转换指南 / Medical Dataset Conversion Guide

本文档介绍如何将医学领域的数据集转换为适配 GraphRAG 代码库的格式。
This document describes how to convert medical domain datasets to the format compatible with the GraphRAG codebase.

---

## 📋 目录 / Table of Contents

1. [数据格式要求 / Data Format Requirements](#数据格式要求--data-format-requirements)
2. [支持的医学数据集 / Supported Medical Datasets](#支持的医学数据集--supported-medical-datasets)
3. [转换工具使用 / Using the Conversion Tool](#转换工具使用--using-the-conversion-tool)
4. [示例数据集 / Example Dataset](#示例数据集--example-dataset)
5. [运行 GraphRAG / Running GraphRAG](#运行-graphrag--running-graphrag)

---

## 数据格式要求 / Data Format Requirements

GraphRAG 需要两个 JSONL 格式的文件：
GraphRAG requires two files in JSONL (JSON Lines) format:

### 1. Corpus.json (语料库 / Corpus)

每行一个 JSON 对象，包含以下字段：
Each line contains one JSON object with the following fields:

```json
{"title": "文档标题 / Document Title", "context": "文档内容 / Document Content"}
```

**字段说明 / Field Description:**
- `title`: 文档标题（字符串）/ Document title (string)
- `context`: 文档正文内容（字符串）/ Document main content (string)

**示例 / Example:**
```json
{"title": "Diabetes Mellitus Type 2", "context": "Type 2 diabetes mellitus is a metabolic disorder..."}
{"title": "Hypertension Pathophysiology", "context": "Hypertension, or high blood pressure..."}
```

### 2. Question.json (问题集 / Question Set)

每行一个 JSON 对象，包含以下字段：
Each line contains one JSON object with the following fields:

```json
{"question": "问题文本 / Question Text", "answer": "答案文本 / Answer Text"}
```

**字段说明 / Field Description:**
- `question`: 问题内容（字符串）/ Question content (string)
- `answer`: 标准答案（字符串）/ Ground truth answer (string)

**示例 / Example:**
```json
{"question": "What are the main risk factors for Type 2 diabetes?", "answer": "The main risk factors include obesity, sedentary lifestyle..."}
{"question": "What is the blood pressure threshold for hypertension?", "answer": "Hypertension is diagnosed when systolic BP ≥140 mmHg..."}
```

---

## 支持的医学数据集 / Supported Medical Datasets

转换工具支持以下常见医学数据集：
The conversion tool supports the following medical datasets:

### 1. PubMedQA

**简介 / Description:**
- 基于 PubMed 生物医学摘要的问答数据集
- Biomedical question answering dataset from PubMed abstracts

**数据源 / Data Source:**
- GitHub: https://github.com/pubmedqa/pubmedqa
- Paper: https://arxiv.org/abs/1909.06146

**使用方法 / Usage:**
```bash
python Data/convert_medical_dataset.py \
    --source_type pubmedqa \
    --source_path /path/to/pubmedqa.json \
    --output_dir ./Data/PubMedQA
```

### 2. MedQA (USMLE)

**简介 / Description:**
- 美国医师执照考试（USMLE）风格的医学问答
- Medical question answering in USMLE style

**数据源 / Data Source:**
- GitHub: https://github.com/jind11/MedQA
- Paper: https://arxiv.org/abs/2009.13081

**使用方法 / Usage:**
```bash
python Data/convert_medical_dataset.py \
    --source_type medqa \
    --source_path /path/to/medqa.json \
    --output_dir ./Data/MedQA
```

### 3. MedMCQA

**简介 / Description:**
- 印度医学考试的多项选择题
- Multiple choice questions from Indian medical exams

**数据源 / Data Source:**
- GitHub: https://github.com/medmcqa/medmcqa
- Paper: https://arxiv.org/abs/2203.14371

**使用方法 / Usage:**
```bash
python Data/convert_medical_dataset.py \
    --source_type medmcqa \
    --source_path /path/to/medmcqa.jsonl \
    --output_dir ./Data/MedMCQA
```

### 4. 自定义医学数据集 / Custom Medical Datasets

如果您有自定义格式的医学数据集，可以指定字段映射：
If you have a custom format medical dataset, you can specify field mappings:

```bash
python Data/convert_medical_dataset.py \
    --source_type custom \
    --source_path /path/to/your_dataset.json \
    --output_dir ./Data/YourDataset \
    --title_field "doc_title" \
    --context_field "doc_content" \
    --question_field "query" \
    --answer_field "response"
```

---

## 转换工具使用 / Using the Conversion Tool

### 安装依赖 / Install Dependencies

确保已安装必要的 Python 库：
Ensure necessary Python libraries are installed:

```bash
pip install pandas
```

### 命令行参数 / Command Line Arguments

| 参数 / Argument | 必需 / Required | 说明 / Description |
|----------------|----------------|-------------------|
| `--source_type` | ✅ | 数据集类型 / Dataset type: `pubmedqa`, `medqa`, `medmcqa`, `custom` |
| `--source_path` | ✅ | 源数据集文件路径 / Source dataset file path |
| `--output_dir` | ✅ | 输出目录 / Output directory |
| `--title_field` | ❌ | 标题字段名（仅自定义格式）/ Title field name (custom only) |
| `--context_field` | ❌ | 内容字段名（仅自定义格式）/ Context field name (custom only) |
| `--question_field` | ❌ | 问题字段名（仅自定义格式）/ Question field name (custom only) |
| `--answer_field` | ❌ | 答案字段名（仅自定义格式）/ Answer field name (custom only) |

### 完整示例 / Complete Example

```bash
# 1. 转换 PubMedQA 数据集
python Data/convert_medical_dataset.py \
    --source_type pubmedqa \
    --source_path ./raw_data/pubmedqa_ori.json \
    --output_dir ./Data/PubMedQA

# 2. 验证生成的文件
ls -lh ./Data/PubMedQA/
# 应该看到:
# Corpus.json
# Question.json

# 3. 查看前几行
head -2 ./Data/PubMedQA/Corpus.json
head -2 ./Data/PubMedQA/Question.json
```

---

## 示例数据集 / Example Dataset

我们提供了一个包含 10 个医学主题的示例数据集：
We provide an example dataset with 10 medical topics:

**位置 / Location:** `./Data/MedicalExample/`

**内容 / Contents:**
- 糖尿病、高血压、心肌梗死、COPD、类风湿关节炎等
- Diabetes, Hypertension, Myocardial Infarction, COPD, Rheumatoid Arthritis, etc.

**使用示例数据集 / Using the Example Dataset:**

```bash
# 使用 RAPTOR 方法运行
python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample

# 使用 LightRAG 方法运行
python main.py -opt Option/Method/LightRAG.yaml -dataset_name MedicalExample

# 使用 HippoRAG 方法运行
python main.py -opt Option/Method/HippoRAG.yaml -dataset_name MedicalExample
```

---

## 运行 GraphRAG / Running GraphRAG

### 配置文件设置 / Configuration File Setup

在运行前，确保配置文件中的数据路径正确：
Before running, ensure the data path in the configuration file is correct:

**Option/Config2.yaml:**
```yaml
data_root: "./Data"  # 数据根目录 / Data root directory
```

### 运行不同方法 / Running Different Methods

GraphRAG 支持多种图 RAG 方法：
GraphRAG supports multiple Graph RAG methods:

```bash
# 方法 1: RAPTOR (树结构)
python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample

# 方法 2: GraphRAG (本地搜索)
python main.py -opt Option/Method/LGraphRAG.yaml -dataset_name MedicalExample

# 方法 3: GraphRAG (全局搜索)
python main.py -opt Option/Method/GGraphRAG.yaml -dataset_name MedicalExample

# 方法 4: HippoRAG (知识图谱)
python main.py -opt Option/Method/HippoRAG.yaml -dataset_name MedicalExample

# 方法 5: LightRAG (富知识图谱)
python main.py -opt Option/Method/LightRAG.yaml -dataset_name MedicalExample

# 方法 6: ToG (思维图)
python main.py -opt Option/Method/ToG.yaml -dataset_name MedicalExample
```

### 评估结果 / Evaluation Results

运行完成后，结果将保存在相应的输出目录中，包括：
After running, results will be saved in the output directory, including:

- 生成的答案 / Generated answers
- 评估指标（BLEU, ROUGE-L, METEOR, MAUVE）/ Evaluation metrics
- 检索的文档 / Retrieved documents

---

## 🔧 故障排除 / Troubleshooting

### 常见问题 / Common Issues

1. **编码错误 / Encoding Errors**
   ```bash
   # 确保使用 UTF-8 编码
   # Ensure UTF-8 encoding
   file -i your_data.json
   iconv -f gbk -t utf-8 input.json > output.json
   ```

2. **JSON 格式错误 / JSON Format Errors**
   ```bash
   # 验证 JSON 格式
   # Validate JSON format
   python -m json.tool Corpus.json > /dev/null
   python -m json.tool Question.json > /dev/null
   ```

3. **文件路径问题 / File Path Issues**
   ```bash
   # 使用绝对路径
   # Use absolute paths
   realpath ./Data/MedicalExample
   ```

---

## 📚 推荐医学数据集资源 / Recommended Medical Dataset Resources

### 英文数据集 / English Datasets
- **PubMedQA**: https://pubmedqa.github.io/
- **MedQA**: https://github.com/jind11/MedQA
- **MedMCQA**: https://medmcqa.github.io/
- **MIMIC-III**: https://mimic.mit.edu/
- **BioASQ**: http://bioasq.org/

### 中文数据集 / Chinese Datasets
- **cMedQA**: https://github.com/zhangsheng93/cMedQA
- **webMedQA**: https://github.com/hejunqing/webMedQA
- **Chinese Medical Dialogue**: https://github.com/Toyhom/Chinese-medical-dialogue-data

---

## 📖 参考文献 / References

1. GraphRAG Paper: [In-depth Analysis of Graph-based RAG](https://arxiv.org/abs/2503.04338)
2. PubMedQA Paper: [PubMedQA: A Dataset for Biomedical Research Question Answering](https://arxiv.org/abs/1909.06146)
3. MedQA Paper: [What Disease does this Patient Have?](https://arxiv.org/abs/2009.13081)

---

## 💡 贡献 / Contributing

如果您想添加对其他医学数据集的支持，请提交 Pull Request！
If you want to add support for other medical datasets, please submit a Pull Request!

---

## 📞 联系方式 / Contact

如有问题，请在 GitHub Issues 中提出。
For questions, please open a GitHub Issue.
