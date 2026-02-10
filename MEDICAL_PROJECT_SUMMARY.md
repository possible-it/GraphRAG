# 医学数据集转换项目总结 / Medical Dataset Conversion Project Summary

[English](#english-summary) | [中文](#中文总结)

---

## 中文总结

### 📋 项目目标

根据您的需求："我想要找到医学类的数据集转化为适配代码库里的数据集（语料库和问题集）"，本项目已完成以下工作：

### ✅ 已完成的工作

#### 1. 医学数据集转换工具 (`Data/convert_medical_dataset.py`)

这是一个功能完整的Python工具，支持多种医学数据集格式：

- **PubMedQA** - 基于PubMed生物医学文献的问答数据集
- **MedQA** - 美国医师执照考试(USMLE)风格的医学问题
- **MedMCQA** - 医学多项选择题
- **自定义格式** - 支持任意JSON格式的数据集，可自定义字段映射

**使用方法：**
```bash
# 转换PubMedQA数据集
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

#### 2. 示例医学数据集 (`Data/MedicalExample/`)

提供了一个包含10个医学主题的示例数据集，可以直接使用：

**医学主题包括：**
- 2型糖尿病
- 高血压
- 急性心肌梗死
- 慢性阻塞性肺疾病(COPD)
- 类风湿关节炎
- 甲状腺功能减退症
- 肺炎
- 急性肾损伤
- 胃食管反流病(GERD)
- 阿尔茨海默病

**数据格式：**
- `Corpus.json` - 10个医学文档（语料库）
- `Question.json` - 10个医学问题及答案

**立即使用：**
```bash
# 使用RAPTOR方法
python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample

# 使用LightRAG方法
python main.py -opt Option/Method/LightRAG.yaml -dataset_name MedicalExample
```

#### 3. 完整的文档

创建了三个文档文件，提供中英文双语支持：

1. **`Data/MEDICAL_README.md`** - 快速入门指南
   - 快速开始步骤
   - 数据格式说明
   - 推荐的医学数据集列表

2. **`Data/MEDICAL_DATASET_GUIDE.md`** - 详细转换指南
   - 完整的数据格式要求
   - 支持的数据集详细说明
   - 转换工具使用示例
   - 故障排除指南

3. **主README更新** - 在主README中添加了医学数据集部分

#### 4. 测试和验证

- **`test_medical_converter.py`** - 完整的测试套件
  - 自定义格式转换测试
  - 示例数据集验证
  - PubMedQA格式测试
  - 所有测试通过 (3/3) ✅

- **`demo_medical_dataset.py`** - 演示脚本
  - 显示数据集内容
  - 展示如何使用不同的GraphRAG方法

### 🎯 数据格式

GraphRAG要求的数据格式为JSONL（每行一个JSON对象）：

**Corpus.json (语料库)：**
```json
{"title": "文档标题", "context": "文档内容"}
{"title": "另一个文档", "context": "另一个内容"}
```

**Question.json (问题集)：**
```json
{"question": "问题内容", "answer": "答案内容"}
{"question": "另一个问题", "answer": "另一个答案"}
```

### 🔗 推荐的医学数据集

#### 英文数据集
- **PubMedQA**: https://pubmedqa.github.io/
- **MedQA**: https://github.com/jind11/MedQA
- **MedMCQA**: https://medmcqa.github.io/

#### 中文数据集
- **cMedQA**: https://github.com/zhangsheng93/cMedQA
- **webMedQA**: https://github.com/hejunqing/webMedQA
- **Chinese Medical Dialogue**: https://github.com/Toyhom/Chinese-medical-dialogue-data

### 📁 文件结构

```
GraphRAG/
├── Data/
│   ├── convert_medical_dataset.py    # 转换工具
│   ├── MEDICAL_README.md              # 快速入门
│   ├── MEDICAL_DATASET_GUIDE.md       # 详细指南
│   └── MedicalExample/                # 示例数据集
│       ├── Corpus.json                # 10个医学文档
│       └── Question.json              # 10个问题
├── test_medical_converter.py          # 测试套件
├── demo_medical_dataset.py            # 演示脚本
└── README.md                          # 已更新
```

### 🚀 下一步

1. **使用示例数据集**
   ```bash
   python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample
   ```

2. **转换您自己的医学数据集**
   - 下载医学数据集（如PubMedQA）
   - 使用转换工具转换格式
   - 运行GraphRAG

3. **查看文档**
   - 快速入门：`Data/MEDICAL_README.md`
   - 详细指南：`Data/MEDICAL_DATASET_GUIDE.md`

---

## English Summary

### 📋 Project Objective

Based on your requirement: "I want to find medical datasets and convert them to fit the datasets in the codebase (corpus and question sets)", this project has completed the following:

### ✅ Completed Work

#### 1. Medical Dataset Conversion Tool (`Data/convert_medical_dataset.py`)

A fully-featured Python tool supporting multiple medical dataset formats:

- **PubMedQA** - Biomedical QA from PubMed abstracts
- **MedQA** - USMLE-style medical exam questions
- **MedMCQA** - Medical multiple choice questions
- **Custom Format** - Support for any JSON format with custom field mapping

**Usage:**
```bash
# Convert PubMedQA dataset
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

#### 2. Example Medical Dataset (`Data/MedicalExample/`)

Provides a ready-to-use example dataset with 10 medical topics:

**Medical Topics:**
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

**Data Format:**
- `Corpus.json` - 10 medical documents (corpus)
- `Question.json` - 10 medical questions and answers

**Use Immediately:**
```bash
# With RAPTOR method
python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample

# With LightRAG method
python main.py -opt Option/Method/LightRAG.yaml -dataset_name MedicalExample
```

#### 3. Complete Documentation

Created three documentation files with bilingual support:

1. **`Data/MEDICAL_README.md`** - Quick Start Guide
   - Quick start steps
   - Data format requirements
   - Recommended medical datasets

2. **`Data/MEDICAL_DATASET_GUIDE.md`** - Detailed Conversion Guide
   - Complete data format requirements
   - Detailed supported dataset descriptions
   - Conversion tool usage examples
   - Troubleshooting guide

3. **Main README Update** - Added medical dataset section

#### 4. Testing and Validation

- **`test_medical_converter.py`** - Complete test suite
  - Custom format conversion test
  - Example dataset validation
  - PubMedQA format test
  - All tests passing (3/3) ✅

- **`demo_medical_dataset.py`** - Demo script
  - Display dataset contents
  - Show how to use different GraphRAG methods

### 🎯 Data Format

GraphRAG requires JSONL format (one JSON object per line):

**Corpus.json (Corpus):**
```json
{"title": "Document Title", "context": "Document Content"}
{"title": "Another Document", "context": "Another Content"}
```

**Question.json (Questions):**
```json
{"question": "Question Text", "answer": "Answer Text"}
{"question": "Another Question", "answer": "Another Answer"}
```

### 🔗 Recommended Medical Datasets

#### English Datasets
- **PubMedQA**: https://pubmedqa.github.io/
- **MedQA**: https://github.com/jind11/MedQA
- **MedMCQA**: https://medmcqa.github.io/

#### Chinese Datasets
- **cMedQA**: https://github.com/zhangsheng93/cMedQA
- **webMedQA**: https://github.com/hejunqing/webMedQA
- **Chinese Medical Dialogue**: https://github.com/Toyhom/Chinese-medical-dialogue-data

### 📁 File Structure

```
GraphRAG/
├── Data/
│   ├── convert_medical_dataset.py    # Conversion tool
│   ├── MEDICAL_README.md              # Quick start
│   ├── MEDICAL_DATASET_GUIDE.md       # Detailed guide
│   └── MedicalExample/                # Example dataset
│       ├── Corpus.json                # 10 medical documents
│       └── Question.json              # 10 questions
├── test_medical_converter.py          # Test suite
├── demo_medical_dataset.py            # Demo script
└── README.md                          # Updated
```

### 🚀 Next Steps

1. **Use the Example Dataset**
   ```bash
   python main.py -opt Option/Method/RAPTOR.yaml -dataset_name MedicalExample
   ```

2. **Convert Your Own Medical Dataset**
   - Download a medical dataset (e.g., PubMedQA)
   - Use the conversion tool to convert the format
   - Run GraphRAG

3. **Check Documentation**
   - Quick start: `Data/MEDICAL_README.md`
   - Detailed guide: `Data/MEDICAL_DATASET_GUIDE.md`

---

## 🎉 Success Metrics

- ✅ Conversion tool implemented and tested
- ✅ Example dataset created and validated
- ✅ Bilingual documentation completed
- ✅ All tests passing (3/3)
- ✅ Zero security vulnerabilities
- ✅ Ready for immediate use

## 📞 Support

For questions or issues:
- See documentation: `Data/MEDICAL_README.md` or `Data/MEDICAL_DATASET_GUIDE.md`
- Run demo: `python demo_medical_dataset.py`
- Run tests: `python test_medical_converter.py`
