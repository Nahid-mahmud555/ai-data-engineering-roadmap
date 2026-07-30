import os
import hashlib

# 1. Stable ID Generator (Based on Contract: Source + Section + Paragraph Offset)
def generate_stable_id(source_uri, section_title, content_snippet):
    raw_string = f"{source_uri}_{section_title}_{content_snippet[:30]}"
    return hashlib.md5(raw_string.encode('utf-8')).hexdigest()[:10]

class RAGPipelineSimulator:
    def __init__(self, data_folder="."):
        self.data_folder = data_folder
        self.index_database = []

    # Task 1 & 4: Ingest docs, split three ways, and build Parent-Child linkage with Stable IDs
    def process_documents(self):
        print("[*] Processing documents and building hierarchical chunks...")
        
        for i in range(1, 11):
            filename = f"Doc_{i:02d}.txt"
            filepath = os.path.join(self.data_folder, filename)
            
            if not os.path.exists(filepath):
                print(f"[-] Warning: {filename} not found, skipping...")
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Level 1: Whole Document
            whole_doc_id = generate_stable_id(filename, "Whole_Doc", content)
            
            # Level 2 & 3: Splitting into Sections and Paragraphs
            sections = content.split("\n\n")
            for sec_idx, sec_text in enumerate(sections):
                if not sec_text.strip():
                    continue
                
                # Extract a pseudo section title from the first line
                lines = sec_text.split("\n")
                section_title = lines[0] if len(lines) > 0 else f"Section_{sec_idx}"
                parent_id = generate_stable_id(filename, section_title, sec_text)
                
                # Treat each paragraph/line block as a child chunk
                paragraphs = [p.strip() for p in lines[1:] if p.strip()] if len(lines) > 1 else [sec_text]
                
                for p_idx, para in enumerate(paragraphs):
                    child_id = generate_stable_id(filename, f"{section_title}_p{p_idx}", para)
                    
                    # Store in our simulated vector/metadata database
                    self.index_database.append({
                        "child_id": child_id,
                        "parent_id": parent_id,
                        "source_uri": filename,
                        "section": section_title,
                        "content": para,
                        "granularity": "Paragraph"
                    })
                    
        print(f"[+] Successfully indexed {len(self.index_database)} child chunks with Parent-Child linkages and Stable IDs!\n")

    # Search / Retrieval Interface (Interactive Input Box Simulation)
    def interactive_search(self):
        print("="*60)
        print(" RAG PIPELINE SEARCH INTERFACE (Task 2 & 4 Simulation) ")
        print("="*60)
        print("Type a keyword or question to search the index (type 'exit' to quit):\n")
        
        while True:
            query = input("🔍 Search Query -> ").strip()
            if query.lower() == 'exit':
                print("Exiting search interface. Good luck with your assignment!")
                break
            
            if not query:
                continue

            # Simple keyword matching retrieval simulation
            matched_results = []
            for item in self.index_database:
                if query.lower() in item["content"].lower() or query.lower() in item["section"].lower():
                    matched_results.append(item)

            if matched_results:
                print(f"\n[Found {len(matched_results)} matching chunks]:")
                for idx, res in enumerate(matched_results[:3], 1):  # Show top 3 results
                    print(f"\n  --- Result {idx} ---")
                    print(f"  * Source File     : {res['source_uri']}")
                    print(f"  * Section Title   : {res['section']}")
                    print(f"  * Child Chunk ID  : {res['child_id']} (Stable ID)")
                    print(f"  * Parent Chunk ID : {res['parent_id']}")
                    print(f"  * Retrieved Text  : \"{res['content']}\"")
                print("-" * 60 + "\n")
            else:
                print("\n❌ No exact matches found for your query. Try another keyword (e.g., 'AI', 'Cloud', 'Cybersecurity').\n")

if __name__ == "__main__":
    pipeline = RAGPipelineSimulator()
    pipeline.process_documents()
    pipeline.interactive_search()
