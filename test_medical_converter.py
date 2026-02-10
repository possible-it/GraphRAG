#!/usr/bin/env python3
"""
Test script for medical dataset conversion tool.
This script validates that the conversion tool works correctly.
"""

import json
import os
import tempfile
import shutil
from pathlib import Path

def test_custom_format():
    """Test custom format conversion."""
    print("=" * 60)
    print("Test 1: Custom Format Conversion")
    print("=" * 60)
    
    # Create temporary test data
    temp_dir = tempfile.mkdtemp()
    try:
        # Create test input file
        test_data = [
            {
                "title": "Test Document 1",
                "context": "This is a test medical document about hypertension.",
                "question": "What is hypertension?",
                "answer": "Hypertension is high blood pressure."
            },
            {
                "title": "Test Document 2", 
                "context": "This is a test medical document about diabetes.",
                "question": "What is diabetes?",
                "answer": "Diabetes is a metabolic disorder."
            }
        ]
        
        input_file = os.path.join(temp_dir, "test_input.json")
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        # Run conversion
        output_dir = os.path.join(temp_dir, "output")
        
        from Data.convert_medical_dataset import MedicalDatasetConverter
        converter = MedicalDatasetConverter(output_dir)
        converter.convert_custom(input_file)
        
        # Verify output
        corpus_path = os.path.join(output_dir, "Corpus.json")
        question_path = os.path.join(output_dir, "Question.json")
        
        assert os.path.exists(corpus_path), "Corpus.json not created"
        assert os.path.exists(question_path), "Question.json not created"
        
        # Check corpus format
        with open(corpus_path, 'r', encoding='utf-8') as f:
            corpus_lines = f.readlines()
            assert len(corpus_lines) == 2, f"Expected 2 corpus entries, got {len(corpus_lines)}"
            
            for line in corpus_lines:
                entry = json.loads(line)
                assert 'title' in entry, "Missing 'title' field"
                assert 'context' in entry, "Missing 'context' field"
        
        # Check question format
        with open(question_path, 'r', encoding='utf-8') as f:
            question_lines = f.readlines()
            assert len(question_lines) == 2, f"Expected 2 question entries, got {len(question_lines)}"
            
            for line in question_lines:
                entry = json.loads(line)
                assert 'question' in entry, "Missing 'question' field"
                assert 'answer' in entry, "Missing 'answer' field"
        
        print("✓ Custom format conversion test PASSED")
        return True
        
    except Exception as e:
        print(f"✗ Custom format conversion test FAILED: {e}")
        return False
    finally:
        shutil.rmtree(temp_dir)


def test_example_dataset():
    """Test that the example dataset is valid."""
    print("\n" + "=" * 60)
    print("Test 2: Example Dataset Validation")
    print("=" * 60)
    
    try:
        base_dir = Path(__file__).parent / "Data" / "MedicalExample"
        corpus_path = base_dir / "Corpus.json"
        question_path = base_dir / "Question.json"
        
        assert corpus_path.exists(), f"Corpus.json not found at {corpus_path}"
        assert question_path.exists(), f"Question.json not found at {question_path}"
        
        # Validate corpus
        with open(corpus_path, 'r', encoding='utf-8') as f:
            corpus_lines = f.readlines()
            assert len(corpus_lines) > 0, "Corpus.json is empty"
            
            for i, line in enumerate(corpus_lines):
                try:
                    entry = json.loads(line)
                    assert 'title' in entry, f"Line {i+1}: Missing 'title' field"
                    assert 'context' in entry, f"Line {i+1}: Missing 'context' field"
                    assert isinstance(entry['title'], str), f"Line {i+1}: 'title' must be string"
                    assert isinstance(entry['context'], str), f"Line {i+1}: 'context' must be string"
                    assert len(entry['context']) > 0, f"Line {i+1}: 'context' is empty"
                except json.JSONDecodeError as e:
                    raise AssertionError(f"Line {i+1}: Invalid JSON: {e}")
        
        # Validate questions
        with open(question_path, 'r', encoding='utf-8') as f:
            question_lines = f.readlines()
            assert len(question_lines) > 0, "Question.json is empty"
            
            for i, line in enumerate(question_lines):
                try:
                    entry = json.loads(line)
                    assert 'question' in entry, f"Line {i+1}: Missing 'question' field"
                    assert 'answer' in entry, f"Line {i+1}: Missing 'answer' field"
                    assert isinstance(entry['question'], str), f"Line {i+1}: 'question' must be string"
                    assert isinstance(entry['answer'], str), f"Line {i+1}: 'answer' must be string"
                    assert len(entry['question']) > 0, f"Line {i+1}: 'question' is empty"
                    assert len(entry['answer']) > 0, f"Line {i+1}: 'answer' is empty"
                except json.JSONDecodeError as e:
                    raise AssertionError(f"Line {i+1}: Invalid JSON: {e}")
        
        print(f"✓ Validated {len(corpus_lines)} corpus entries")
        print(f"✓ Validated {len(question_lines)} question entries")
        print("✓ Example dataset validation test PASSED")
        return True
        
    except Exception as e:
        print(f"✗ Example dataset validation test FAILED: {e}")
        return False


def test_pubmedqa_format():
    """Test PubMedQA format handling."""
    print("\n" + "=" * 60)
    print("Test 3: PubMedQA Format")
    print("=" * 60)
    
    temp_dir = tempfile.mkdtemp()
    try:
        # Create test PubMedQA data
        test_data = {
            "12345": {
                "question": "Does vitamin D deficiency cause depression?",
                "context": {
                    "contexts": [
                        "Vitamin D deficiency is common in many populations.",
                        "Depression is a major mental health condition.",
                        "Some studies suggest a link between vitamin D and depression."
                    ],
                    "labels": ["BACKGROUND", "BACKGROUND", "RESULTS"],
                    "meshes": ["Vitamin D", "Depression"]
                },
                "long_answer": "There is evidence suggesting that vitamin D deficiency may be associated with depression, but more research is needed.",
                "final_decision": "maybe"
            }
        }
        
        input_file = os.path.join(temp_dir, "pubmedqa.json")
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        # Run conversion
        output_dir = os.path.join(temp_dir, "output")
        
        from Data.convert_medical_dataset import MedicalDatasetConverter
        converter = MedicalDatasetConverter(output_dir)
        converter.convert_pubmedqa(input_file)
        
        # Verify output
        corpus_path = os.path.join(output_dir, "Corpus.json")
        question_path = os.path.join(output_dir, "Question.json")
        
        assert os.path.exists(corpus_path), "Corpus.json not created"
        assert os.path.exists(question_path), "Question.json not created"
        
        # Verify content
        with open(corpus_path, 'r', encoding='utf-8') as f:
            corpus_entry = json.loads(f.readline())
            assert '12345' in corpus_entry['title'], f"Title mismatch: {corpus_entry['title']}"
            assert 'Vitamin D' in corpus_entry['context'], "Context missing expected content"
        
        with open(question_path, 'r', encoding='utf-8') as f:
            question_entry = json.loads(f.readline())
            q_lower = question_entry['question'].lower()
            assert 'vitamin' in q_lower, f"Question missing 'vitamin': {question_entry['question']}"
            assert len(question_entry['answer']) > 0, "Answer is empty"
        
        print("✓ PubMedQA format test PASSED")
        return True
        
    except Exception as e:
        print(f"✗ PubMedQA format test FAILED: {e}")
        return False
    finally:
        shutil.rmtree(temp_dir)


def main():
    """Run all tests."""
    print("\n" + "🧪 " * 20)
    print("Medical Dataset Converter Test Suite")
    print("🧪 " * 20 + "\n")
    
    results = []
    
    # Run tests
    results.append(("Custom Format", test_custom_format()))
    results.append(("Example Dataset", test_example_dataset()))
    results.append(("PubMedQA Format", test_pubmedqa_format()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    print("\n" + "-" * 60)
    print(f"Total: {passed}/{total} tests passed")
    print("-" * 60)
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
