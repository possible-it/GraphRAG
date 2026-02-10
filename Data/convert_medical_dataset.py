"""
Medical Dataset Converter for GraphRAG

This script converts medical datasets into the format required by GraphRAG:
- Corpus.json: JSONL format with {title, context} fields
- Question.json: JSONL format with {question, answer} fields

Supported medical datasets:
1. PubMedQA - Biomedical question answering from PubMed abstracts
2. MedQA (USMLE) - Medical exam questions from USMLE
3. MedMCQA - Medical multiple choice questions
4. Custom medical datasets

Usage:
    python convert_medical_dataset.py --source_type pubmedqa --source_path /path/to/pubmedqa.json --output_dir ./Data/MedicalDataset
"""

import json
import argparse
import os
from pathlib import Path
from typing import Dict, List, Any


class MedicalDatasetConverter:
    """Converter for various medical datasets to GraphRAG format."""
    
    def __init__(self, output_dir: str):
        """
        Initialize converter.
        
        Args:
            output_dir: Output directory for converted dataset
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.corpus_path = self.output_dir / "Corpus.json"
        self.question_path = self.output_dir / "Question.json"
        
    def convert_pubmedqa(self, source_path: str):
        """
        Convert PubMedQA dataset.
        
        PubMedQA format:
        {
            "PMID": {
                "question": "...",
                "context": {"contexts": [...], "labels": [...], "meshes": [...]},
                "long_answer": "...",
                "final_decision": "yes/no/maybe"
            }
        }
        """
        print(f"Converting PubMedQA dataset from {source_path}")
        
        with open(source_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        corpus_data = []
        question_data = []
        
        for pmid, item in data.items():
            # Create corpus entry from context
            if 'context' in item and 'contexts' in item['context']:
                contexts = item['context']['contexts']
                context_text = ' '.join(contexts)
                
                corpus_entry = {
                    "title": f"PubMed Article {pmid}",
                    "context": context_text
                }
                corpus_data.append(corpus_entry)
            
            # Create question entry
            question_entry = {
                "question": item.get('question', ''),
                "answer": item.get('long_answer', item.get('final_decision', ''))
            }
            question_data.append(question_entry)
        
        self._write_jsonl(self.corpus_path, corpus_data)
        self._write_jsonl(self.question_path, question_data)
        
        print(f"✓ Converted {len(corpus_data)} corpus entries")
        print(f"✓ Converted {len(question_data)} questions")
        
    def convert_medqa(self, source_path: str):
        """
        Convert MedQA (USMLE) dataset.
        
        MedQA format:
        {
            "question": "...",
            "answer": "...",
            "options": {"A": "...", "B": "...", ...},
            "meta_info": "..."
        }
        """
        print(f"Converting MedQA dataset from {source_path}")
        
        with open(source_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        corpus_data = []
        question_data = []
        
        for idx, item in enumerate(data):
            # Create corpus from question context
            context = item.get('question', '')
            if 'meta_info' in item:
                context += f"\n\nContext: {item['meta_info']}"
            
            corpus_entry = {
                "title": f"Medical Question {idx + 1}",
                "context": context
            }
            corpus_data.append(corpus_entry)
            
            # Create question entry with options
            options_text = ""
            if 'options' in item:
                options_text = "\nOptions:\n" + "\n".join(
                    f"{k}: {v}" for k, v in item['options'].items()
                )
            
            question_entry = {
                "question": item.get('question', '') + options_text,
                "answer": item.get('answer', '')
            }
            question_data.append(question_entry)
        
        self._write_jsonl(self.corpus_path, corpus_data)
        self._write_jsonl(self.question_path, question_data)
        
        print(f"✓ Converted {len(corpus_data)} corpus entries")
        print(f"✓ Converted {len(question_data)} questions")
        
    def convert_medmcqa(self, source_path: str):
        """
        Convert MedMCQA dataset.
        
        MedMCQA format:
        {
            "question": "...",
            "opa": "option A",
            "opb": "option B",
            "opc": "option C",
            "opd": "option D",
            "cop": correct_option_index,
            "exp": "explanation",
            "subject_name": "...",
            "topic_name": "..."
        }
        """
        print(f"Converting MedMCQA dataset from {source_path}")
        
        with open(source_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        corpus_data = []
        question_data = []
        
        for idx, line in enumerate(lines):
            item = json.loads(line.strip())
            
            # Create corpus entry
            context = item.get('question', '')
            if 'subject_name' in item:
                context = f"Subject: {item['subject_name']}\n" + context
            if 'topic_name' in item:
                context += f"\nTopic: {item['topic_name']}"
            
            corpus_entry = {
                "title": f"Medical MCQ {idx + 1}",
                "context": context
            }
            corpus_data.append(corpus_entry)
            
            # Create question entry
            options = [
                f"A: {item.get('opa', '')}",
                f"B: {item.get('opb', '')}",
                f"C: {item.get('opc', '')}",
                f"D: {item.get('opd', '')}"
            ]
            options_text = "\nOptions:\n" + "\n".join(options)
            
            # Get correct answer
            cop = item.get('cop', 0)
            answer_map = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
            answer = answer_map.get(cop, 'A')
            if 'exp' in item and item['exp']:
                answer += f"\nExplanation: {item['exp']}"
            
            question_entry = {
                "question": item.get('question', '') + options_text,
                "answer": answer
            }
            question_data.append(question_entry)
        
        self._write_jsonl(self.corpus_path, corpus_data)
        self._write_jsonl(self.question_path, question_data)
        
        print(f"✓ Converted {len(corpus_data)} corpus entries")
        print(f"✓ Converted {len(question_data)} questions")
    
    def convert_custom(self, source_path: str, 
                      title_field: str = "title",
                      context_field: str = "context",
                      question_field: str = "question", 
                      answer_field: str = "answer"):
        """
        Convert custom medical dataset.
        
        Args:
            source_path: Path to source JSON file
            title_field: Field name for document title
            context_field: Field name for document context
            question_field: Field name for question
            answer_field: Field name for answer
        """
        print(f"Converting custom dataset from {source_path}")
        
        with open(source_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle both list and dict formats
        if isinstance(data, dict):
            data = list(data.values())
        
        corpus_data = []
        question_data = []
        
        for idx, item in enumerate(data):
            # Create corpus entry
            corpus_entry = {
                "title": item.get(title_field, f"Document {idx + 1}"),
                "context": item.get(context_field, "")
            }
            corpus_data.append(corpus_entry)
            
            # Create question entry
            question_entry = {
                "question": item.get(question_field, ""),
                "answer": item.get(answer_field, "")
            }
            question_data.append(question_entry)
        
        self._write_jsonl(self.corpus_path, corpus_data)
        self._write_jsonl(self.question_path, question_data)
        
        print(f"✓ Converted {len(corpus_data)} corpus entries")
        print(f"✓ Converted {len(question_data)} questions")
    
    def _write_jsonl(self, path: Path, data: List[Dict[str, Any]]):
        """Write data in JSONL format."""
        with open(path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        print(f"  → Saved to {path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert medical datasets to GraphRAG format"
    )
    parser.add_argument(
        "--source_type",
        type=str,
        required=True,
        choices=["pubmedqa", "medqa", "medmcqa", "custom"],
        help="Type of source medical dataset"
    )
    parser.add_argument(
        "--source_path",
        type=str,
        required=True,
        help="Path to source dataset file"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Output directory for converted dataset"
    )
    parser.add_argument(
        "--title_field",
        type=str,
        default="title",
        help="Field name for title (custom format only)"
    )
    parser.add_argument(
        "--context_field",
        type=str,
        default="context",
        help="Field name for context (custom format only)"
    )
    parser.add_argument(
        "--question_field",
        type=str,
        default="question",
        help="Field name for question (custom format only)"
    )
    parser.add_argument(
        "--answer_field",
        type=str,
        default="answer",
        help="Field name for answer (custom format only)"
    )
    
    args = parser.parse_args()
    
    converter = MedicalDatasetConverter(args.output_dir)
    
    if args.source_type == "pubmedqa":
        converter.convert_pubmedqa(args.source_path)
    elif args.source_type == "medqa":
        converter.convert_medqa(args.source_path)
    elif args.source_type == "medmcqa":
        converter.convert_medmcqa(args.source_path)
    elif args.source_type == "custom":
        converter.convert_custom(
            args.source_path,
            args.title_field,
            args.context_field,
            args.question_field,
            args.answer_field
        )
    
    print(f"\n✓ Conversion completed! Dataset saved to: {args.output_dir}")
    print(f"  - Corpus: {args.output_dir}/Corpus.json")
    print(f"  - Questions: {args.output_dir}/Question.json")
    print(f"\nTo use with GraphRAG, run:")
    print(f"  python main.py -opt Option/Method/<METHOD>.yaml -dataset_name {Path(args.output_dir).name}")


if __name__ == "__main__":
    main()
