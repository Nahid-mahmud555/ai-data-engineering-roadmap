import os
import json
from pathlib import Path
from docling.document_converter import DocumentConverter

def parse_quality_gate(text, min_chars_per_page=100, max_symbol_ratio=0.3):
    """
    Automated check to quarantine badly parsed documents.
    """
    if not text or len(text.strip()) == 0:
        return False, "Empty Document / No Text Extracted"
    
    total_chars = len(text)
    symbol_count = sum(1 for c in text if not c.isalnum() and not c.isspace())
    symbol_ratio = symbol_count / total_chars if total_chars > 0 else 1
    
    if symbol_ratio > max_symbol_ratio:
        return False, f"High gibberish/symbol ratio: {symbol_ratio:.2f}"
    
    if total_chars < min_chars_per_page:
        return False, f"Low character yield: {total_chars} chars"
        
    return True, "Passed"

def process_corpus(input_dir):
    converter = DocumentConverter()
    pdf_files = list(Path(input_dir).glob("*.pdf"))
    
    quarantine_report = []
    
    for pdf_path in pdf_files:
        print(f"Processing: {pdf_path.name}...")
        try:
            result = converter.convert(str(pdf_path))
            markdown_content = result.document.export_to_markdown()
            
            # Run Quality Gate
            is_valid, reason = parse_quality_gate(markdown_content)
            
            if not is_valid:
                print(f" [!] Quarantined: {pdf_path.name} -> Reason: {reason}")
                quarantine_report.append({
                    "source_uri": str(pdf_path),
                    "status": "Rejected",
                    "reason": reason
                })
                continue
                
            # Save valid Markdown output with metadata
            output_file = Path("output_markdown") / f"{pdf_path.stem}.md"
            output_file.write_text(markdown_content, encoding="utf-8")
            
            print(f" [✓] Success: Saved to {output_file}")
            
        except Exception as e:
            quarantine_report.append({
                "source_uri": str(pdf_path),
                "status": "Error",
                "reason": str(e)
            })

    # Save Quarantine Report
    with open("quarantine_report.json", "w", encoding="utf-8") as f:
        json.dump(quarantine_report, f, indent=4)
    print("\nProcessing complete! Quarantine report generated.")

if __name__ == "__main__":
    process_corpus("hard_pdfs")
