# 医学数据集快速入门 / Medical Dataset Quick Start

[English](#english-version) | [中文](#中文版本)

---

## 中文版本

### 📚 概述

本指南帮助您快速将医学数据集转换并使用到 GraphRAG 系统中。

### 🚀 快速开始

#### 1. 使用预制的医学示例数据集

我们提供了一个包含 10 个医学主题的示例数据集，可以直接使用：

```bash
# 运行 RAPTOR 方法
python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample

# 运行 LightRAG 方法
python main.py -opt Option/Method/LightRAG.yaml -dataset_name MedicalExample
```

#### 2. 转换您自己的医学数据集

**支持的医学数据集格式：**
- PubMedQA - 生物医学问答
- MedQA - 医学考试问题
- MedMCQA - 医学选择题
- 自定义格式

**转换命令示例：**

```bash
# 转换 PubMedQA
python Data/convert_medical_dataset.py \
    --source_type pubmedqa \
    --source_path /path/to/pubmedqa.json \
    --output_dir ./Data/PubMedQA

# 转换自定义数据集
python Data/convert_medical_dataset.py \
    --source_type custom \
    --source_path /path/to/your_data.json \
    --output_dir ./Data/YourDataset
```

### 📋 数据格式要求

GraphRAG 需要两个 JSONL 文件：

**1. Corpus.json（语料库）**
```json
{"title": "文档标题", "context": "文档内容"}
```

**2. Question.json（问题集）**
```json
{"question": "问题内容", "answer": "答案内容"}
```

### 📖 详细文档

完整的转换指南请查看：[MEDICAL_DATASET_GUIDE.md](./MEDICAL_DATASET_GUIDE.md)

### 🔗 推荐的医学数据集

#### 英文数据集
- **PubMedQA**: https://pubmedqa.github.io/ - 基于 PubMed 的生物医学问答
- **MedQA**: https://github.com/jind11/MedQA - USMLE 风格的医学问题
- **MedMCQA**: https://medmcqa.github.io/ - 医学多选题

#### 中文数据集
- **cMedQA**: https://github.com/zhangsheng93/cMedQA - 中文医学问答
- **webMedQA**: https://github.com/hejunqing/webMedQA - 中文在线医疗问答
- **Chinese Medical Dialogue**: https://github.com/Toyhom/Chinese-medical-dialogue-data - 中文医患对话

### 💡 示例数据集内容

示例数据集（`Data/MedicalExample/`）包含以下医学主题：
- 2型糖尿病
- 高血压
- 急性心肌梗死
- 慢性阻塞性肺疾病（COPD）
- 类风湿关节炎
- 甲状腺功能减退症
- 肺炎
- 急性肾损伤
- 胃食管反流病（GERD）
- 阿尔茨海默病

---

## English Version

### 📚 Overview

This guide helps you quickly convert and use medical datasets with the GraphRAG system.

### 🚀 Quick Start

#### 1. Use the Pre-built Medical Example Dataset

We provide an example dataset with 10 medical topics that you can use directly:

```bash
# Run with RAPTOR method
python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample

# Run with LightRAG method
python main.py -opt Option/Method/LightRAG.yaml -dataset_name MedicalExample
```

#### 2. Convert Your Own Medical Dataset

**Supported medical dataset formats:**
- PubMedQA - Biomedical question answering
- MedQA - Medical exam questions
- MedMCQA - Medical multiple choice questions
- Custom format

**Conversion command examples:**

```bash
# Convert PubMedQA
python Data/convert_medical_dataset.py \
    --source_type pubmedqa \
    --source_path /path/to/pubmedqa.json \
    --output_dir ./Data/PubMedQA

# Convert custom dataset
python Data/convert_medical_dataset.py \
    --source_type custom \
    --source_path /path/to/your_data.json \
    --output_dir ./Data/YourDataset
```

### 📋 Data Format Requirements

GraphRAG requires two JSONL files:

**1. Corpus.json (Corpus)**
```json
{"title": "Document Title", "context": "Document Content"}
```

**2. Question.json (Questions)**
```json
{"question": "Question Text", "answer": "Answer Text"}
```

### 📖 Detailed Documentation

For a complete conversion guide, see: [MEDICAL_DATASET_GUIDE.md](./MEDICAL_DATASET_GUIDE.md)

### 🔗 Recommended Medical Datasets

#### English Datasets
- **PubMedQA**: https://pubmedqa.github.io/ - Biomedical QA from PubMed
- **MedQA**: https://github.com/jind11/MedQA - USMLE-style medical questions
- **MedMCQA**: https://medmcqa.github.io/ - Medical multiple choice questions

#### Chinese Datasets
- **cMedQA**: https://github.com/zhangsheng93/cMedQA - Chinese medical QA
- **webMedQA**: https://github.com/hejunqing/webMedQA - Chinese online medical QA
- **Chinese Medical Dialogue**: https://github.com/Toyhom/Chinese-medical-dialogue-data - Chinese doctor-patient dialogues

### 💡 Example Dataset Contents

The example dataset (`Data/MedicalExample/`) includes the following medical topics:
- Type 2 Diabetes Mellitus
- Hypertension
- Acute Myocardial Infarction
- Chronic Obstructive Pulmonary Disease (COPD)
- Rheumatoid Arthritis
- Hypothyroidism
- Pneumonia
- Acute Kidney Injury
- Gastroesophageal Reflux Disease (GERD)
- Alzheimer's Disease

---

## 🛠️ Tools Provided / 提供的工具

### convert_medical_dataset.py

A comprehensive conversion tool for transforming medical datasets into GraphRAG format.

**Features / 功能：**
- ✅ Supports multiple medical dataset formats / 支持多种医学数据集格式
- ✅ Automatic field mapping / 自动字段映射
- ✅ Custom dataset support / 支持自定义数据集
- ✅ UTF-8 encoding support / UTF-8 编码支持
- ✅ Validation and error checking / 验证和错误检查

**Usage / 使用方法：**
```bash
python Data/convert_medical_dataset.py --help
```

---

## 📞 Support / 支持

For questions or issues, please:
- 查看详细文档 / Check detailed documentation: [MEDICAL_DATASET_GUIDE.md](./MEDICAL_DATASET_GUIDE.md)
- 提交 Issue / Open an issue on GitHub
- 查阅主 README / See main README: [README.md](../README.md)
