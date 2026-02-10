#!/usr/bin/env python3
"""
Demo script showing how to use the medical dataset with GraphRAG.
This demonstrates loading and displaying the medical example dataset.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

def display_dataset_info():
    """Display information about the medical example dataset."""
    
    print("=" * 70)
    print("Medical Dataset Demo for GraphRAG")
    print("=" * 70)
    print()
    
    # Path to medical example dataset
    data_dir = Path(__file__).parent / "Data" / "MedicalExample"
    corpus_path = data_dir / "Corpus.json"
    question_path = data_dir / "Question.json"
    
    # Load and display corpus
    print("📚 CORPUS (Medical Documents)")
    print("-" * 70)
    
    with open(corpus_path, 'r', encoding='utf-8') as f:
        corpus_lines = f.readlines()
        
    print(f"Total documents: {len(corpus_lines)}")
    print()
    
    for i, line in enumerate(corpus_lines[:3], 1):  # Show first 3
        entry = json.loads(line)
        print(f"Document {i}:")
        print(f"  Title: {entry['title']}")
        print(f"  Content: {entry['context'][:150]}...")
        print()
    
    print(f"... and {len(corpus_lines) - 3} more documents")
    print()
    
    # Load and display questions
    print("❓ QUESTIONS")
    print("-" * 70)
    
    with open(question_path, 'r', encoding='utf-8') as f:
        question_lines = f.readlines()
        
    print(f"Total questions: {len(question_lines)}")
    print()
    
    for i, line in enumerate(question_lines[:3], 1):  # Show first 3
        entry = json.loads(line)
        print(f"Question {i}:")
        print(f"  Q: {entry['question']}")
        print(f"  A: {entry['answer'][:120]}...")
        print()
    
    print(f"... and {len(question_lines) - 3} more questions")
    print()
    
    # Show how to run with GraphRAG
    print("=" * 70)
    print("🚀 RUNNING WITH GRAPHRAG")
    print("=" * 70)
    print()
    print("To use this dataset with different GraphRAG methods:")
    print()
    
    methods = [
        ("RAPTOR", "Tree-based retrieval"),
        ("LightRAG", "Rich Knowledge Graph"),
        ("HippoRAG", "Knowledge Graph with PPR"),
        ("LGraphRAG", "Local Graph Search"),
        ("GGraphRAG", "Global Graph Search"),
        ("ToG", "Thinking on Graphs")
    ]
    
    for method, description in methods:
        print(f"  {method:12} ({description})")
        print(f"    python main.py -opt Option/Method/{method}.yaml -dataset_name MedicalExample")
        print()
    
    print("=" * 70)
    print("📖 For more information:")
    print("  - Medical Dataset Guide: Data/MEDICAL_DATASET_GUIDE.md")
    print("  - Quick Start: Data/MEDICAL_README.md")
    print("=" * 70)


if __name__ == "__main__":
    try:
        display_dataset_info()
    except FileNotFoundError as e:
        print(f"Error: Could not find medical dataset files.")
        print(f"Make sure you're running from the GraphRAG root directory.")
        print(f"Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
