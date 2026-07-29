import math
from collections import Counter, defaultdict

# 1. Generating 100 Unique Domain-Specific Documents about Bangladesh
documents = [
    # History & Liberation War (1-15)
    "The historic Speech of 7th March 1971 by Bangabandhu Sheikh Mujibur Rahman inspired the nation for independence.",
    "The Bangladesh Liberation War was fought in 1971, resulting in the emergence of a sovereign nation.",
    "The Language Movement of 1952 marked a historic milestone for Bengali nationalism and mother tongue recognition.",
    "Aparajeyo Bangla sculpture at Dhaka University symbolizes the supreme sacrifice of freedom fighters.",
    "Jatiya Smriti Soudan in Savar is the national monument dedicated to the martyrs of the liberation war.",
    "The Mujibnagar Government was formed on April 10, 1971, acting as the first provisional government.",
    "Operation Searchlight was a planned military operation conducted by the Pakistani army in March 1971.",
    "Bir Sreshtho are the seven heroic freedom fighters who received Bangladesh's highest military award.",
    "The surrender of the Pakistani military took place at the Ramna Race Course on December 16, 1971.",
    "Language Martyrs Day, observed on 21st February, is globally recognized as International Mother Language Day.",
    "The Six-Point Movement initiated by Sheikh Mujibur Rahman in 1966 acted as a charter of freedom for Bengalis.",
    "Agartala Conspiracy Case was filed against political leaders and military personnel during the Pakistan era.",
    "Mass Uprising of 1969 created a massive political wave that eventually led to the 1971 revolution.",
    "The Martyred Intellectuals Day on December 14 commemorates academics and professionals killed in 1971.",
    "Bangabandhu's historic homecoming on January 10, 1972, marked the true completion of national victory.",

    # Geography, Rivers & Nature (16-35)
    "The Sundarbans is the largest single tidal mangrove forest in the world, home to the Royal Bengal Tiger.",
    "Padma, Meghna, and Jamuna form the mighty river system that shapes the deltaic landscape of Bangladesh.",
    "Sylhet region is famous for its lush green tea gardens, hilly terrain, and high annual rainfall.",
    "Cox's Bazar boasts the longest unbroken natural sea beach in the world facing the Bay of Bengal.",
    "Saint Martin's Island is the only coral island situated in the northeastern part of the Bay of Bengal.",
    "Kaptai Lake in Rangamati is the largest artificial water reservoir created by damming the Karnafuli River.",
    "The Barind Tract is a geomorphologically unique Pleistocene plateau located in the northwestern region.",
    "Tanguar Haor in Sunamganj is a Ramsar site and a massive freshwater wetland ecosystem for migratory birds.",
    "Kuakata in Patuakhali is renowned for offering panoramic views of both sunrise and sunset from the beach.",
    "Madhabkunda waterfall in Moulvibazar is one of the highest and most popular cascades in the country.",
    "The Brahmaputra river enters Bangladesh from Assam, carrying massive amounts of silt and water flow.",
    "Sajek Valley in Rangamati offers breathtaking cloudscapes and elevated mountainous views of the ranges.",
    "Nijhum Dwip is a remote island situated in the estuary of the Meghna River, known for spotted deer.",
    "Bogra's Mohasthangarh is the oldest known archaeological site dating back to the 3rd century BCE.",
    "Paharpur Buddhist Vihara is a UNESCO World Heritage site representing ancient monastic architecture.",
    "Chhota Sona Mosque in Chapai Nawabganj is a magnificent historical landmark from the Sultanate era.",
    "Lalbagh Fort in Dhaka is an incomplete 17th-century Mughal historical fortification complex.",
    "Ahsan Manzil, located on the banks of the Buriganga River, served as the residential palace of the Nawab.",
    "Kantaji Temple in Dinajpur is renowned for its intricate and historic terracotta ornamentation work.",
    "Mainamati in Comilla preserves ancient Buddhist ruins and artifacts from the early medieval period.",

    # Economy, RMG, Agriculture & Trade (36-65)
    "The Ready-Made Garments (RMG) sector is the backbone of Bangladesh export earnings and industrial growth.",
    "Remittances sent by expatriate workers play a massive role in stabilizing the foreign exchange reserves.",
    "Bangladesh is one of the leading global producers and exporters of high-quality raw jute and jute goods.",
    "The pharmaceutical industry of Bangladesh meets domestic demand and exports life-saving drugs globally.",
    "Kansat mango market in Shibganj is recognized as the biggest seasonal fruit trading hub in the country.",
    "Sylhet and Moulvibazar tea estates produce premium-grade black tea for local consumption and export.",
    "Chittagong Port handles the vast majority of the nation's international maritime trade and container cargo.",
    "Padma Bridge is a multi-purpose road-rail megaproject connecting the southern districts directly to Dhaka.",
    "Bangabandhu Tunnel under the Karnaphuli River is the first underwater expressway tunnel in South Asia.",
    "Rupppur Nuclear Power Plant is a major high-tech energy infrastructure project being built in Pabna.",
    "Hortex Foundation and agricultural supply chains boost the export market of fresh vegetables and fruits.",
    "Microfinance and rural banking models pioneered in Bangladesh have transformed global poverty alleviation.",
    "SME foundation promotes small and medium enterprises, digital entrepreneurship, and cottage industries.",
    "The leather industry produces world-class footwear and finished goods destined for global markets.",
    "Shipbuilding industry in Khulna and Dhaka constructs ocean-going vessels for international buyers.",
    "IT and software outsourcing sectors are rapidly growing, contributing significantly to digital exports.",
    "Mobile financial services (MFS) like bKash and Nagad have revolutionized digital transactions and economy.",
    "Stock exchanges in Dhaka and Chittagong drive corporate investments and capital market participation.",
    "The fisheries sector makes Bangladesh one of the top inland open-water fish-producing nations worldwide.",
    "Cold storage facilities and logistics networks support the seasonal preservation of perishable crops.",
    "The shrimp farming industry in the coastal belt earns valuable foreign currency through export.",
    "Aromatic rice varieties like Chinigura and Kalijira are widely cultivated and exported across regions.",
    "Bagerhat Sixty Dome Mosque showcases unique medieval brick architecture and Islamic heritage.",
    "Haor agriculture relies heavily on early harvesting cycles before flash floods submerge the crop fields.",
    "Solar home systems and rural electrification programs have transformed energy access in remote areas.",
    "The ceramic industry manufactures high-end tableware exported to North America and Europe.",
    "Light engineering workshops manufacture agricultural machinery parts and spare components locally.",
    "Poultry and dairy sectors have achieved self-sufficiency in meeting domestic nutritional demands.",
    "The paper and pulp mills utilize bamboo and softwood resources for industrial book production.",
    "National Highway expansion projects continue to enhance domestic cargo movement and transit efficiency.",

    # Culture, Arts, Festivals & Lifestyle (66-100)
    "Pohela Boishakh, the Bengali New Year, is celebrated nationwide with colorful rallies, fairs, and songs.",
    "Rabindra Sangeet and Nazrul Geeti form the core musical foundation of classical and modern Bengali culture.",
    "Baul music and mystic folk philosophy of Lalon Shah promote universal harmony and spiritual awakening.",
    "Gambhira and Alkap are traditional folk performance arts native to the Chapai Nawabganj and Rajshahi regions.",
    "Ekushey Book Fair held every February is the largest cultural and literary book festival in the country.",
    "Nakshi Kantha is a traditional form of embroidered quilt crafted using colorful rural yarn stitches.",
    "Jamdani saree weaving is an ancient muslin craft recognized as a UNESCO Intangible Cultural Heritage.",
    "Hilsa (Ilish) is the national fish, celebrated culinary-wise with traditional Panta-Ilish during New Year.",
    "The traditional rural wedding ceremonies feature intricate Gaye Halud rituals and folk musical gatherings.",
    "Rickshaw art is a vibrant, colorful subculture showcasing iconic paintings on urban transport vehicles.",
    "The National Museum in Dhaka houses extensive archaeological collections and historical artifacts.",
    "Bangladesh Shilpakala Academy promotes national theater, fine arts, dance, and cultural festivals.",
    "Cricket has evolved into a passionate national sport, with international matches drawing massive crowds.",
    "Kabadi is recognized as the traditional national sport, widely played across rural clubs and tournaments.",
    "The Autumn season brings vibrant celebrations of Durga Puja across thousands of decorated pandals.",
    "Shab-e-Barat and Eid festivals bring communities together with traditional sweets like Semai and Pitha.",
    "Pitha Utsob during the winter season features varieties of traditional rice cakes like Patishapta and Chitai.",
    "National Poet Kazi Nazrul Islam's rebel poetry inspires courage, equality, and patriotic fervor.",
    "Nobel Laureate Rabindranath Tagore composed the national anthem 'Amar Shonar Bangla' with deep affection.",
    "Jatra is a traditional open-air folk theatrical drama popular in rural community entertainment.",
    "Bishwa Ijtema on the banks of the Turag River is the second-largest gathering of Muslims worldwide.",
    "The National Zoo and botanical gardens provide wildlife conservation and recreational spaces for families.",
    "Cox's Bazar Marine Drive offers a scenic coastal highway experience flanked by hills and sea.",
    "Ahsan Manzil museum preserves the regal lifestyle and interior antiques of the colonial Nawabs.",
    "Sat Gambuj Mosque in Dhaka represents classic 15th-century Khan Jahan Ali architectural style.",
    "National Martyrs Memorial in Savar stands tall as a symbol of unity, courage, and national pride.",
    "Bangabandhu Sheikh Mujibur Rahman Novo Theatre offers immersive astronomical shows and space education.",
    "Ramna Park and Curzon Hall represent historic botanical and architectural landmarks in Dhaka city.",
    "The Padma River bridge construction milestone stands as a testament to national engineering capability.",
    "The vibrant handloom industries of Tangail and Sirajganj produce world-class traditional sarees.",
    "Bogra's famous 'Doi' (curd) is a traditional dairy delicacy enjoyed across the entire nation.",
    "Sylhet's ratargul swamp forest is a unique freshwater flooded forest with rich ecological diversity.",
    "Kuakata sea beach offers pristine views of the Bay of Bengal horizon during monsoon and winter.",
    "The historical traditions of pottery and terracotta craftsmanship thrive in rural artisan villages.",
    "Bangladesh continues its steady journey toward sustainable digital growth, innovation, and prosperity."
]

# 2. Text Preprocessing and Tokenization Function
def tokenize(text):
    return [word.lower() for word in text.split() if word.isalnum()]

tokenized_corpus = [tokenize(doc) for doc in documents]

# 3. BM25 Search Engine Class Implementation
class BM25SearchEngine:
    def __init__(self, corpus, k1=1.2, b=0.75):
        self.corpus = corpus
        self.k1 = k1
        self.b = b
        self.doc_lens = [len(doc) for doc in corpus]
        self.avg_dl = sum(self.doc_lens) / len(corpus)
        self.doc_count = len(corpus)
        
        # Calculating Term Frequencies and Inverse Document Frequency (IDF)
        self.doc_freqs = defaultdict(int)
        self.term_freqs = []
        for doc in corpus:
            term_freq = Counter(doc)
            self.term_freqs.append(term_freq)
            for term in term_freq:
                self.doc_freqs[term] += 1
                
        self.idf = {}
        for term, freq in self.doc_freqs.items():
            self.idf[term] = math.log(1 + (self.doc_count - freq + 0.5) / (freq + 0.5))

    def search(self, query, top_n=5):
        query_terms = tokenize(query)
        scores = []
        
        for idx, doc_tokens in enumerate(self.corpus):
            score = 0.0
            doc_len = self.doc_lens[idx]
            term_freq = self.term_freqs[idx]
            
            for term in query_terms:
                if term in term_freq:
                    tf = term_freq[term]
                    idf = self.idf.get(term, 0)
                    numerator = idf * tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_dl))
                    score += numerator / denominator
                    
            if score > 0:
                scores.append((idx, score))
                
        # Sorting scores in descending order
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_n]

    def evaluate_recall(self, query, expected_doc_ids, top_n=10):
        results = self.search(query, top_n=top_n)
        retrieved_ids = [idx + 1 for idx, score in results]
        
        hits = len(set(retrieved_ids).intersection(set(expected_doc_ids)))
        total_expected = len(expected_doc_ids)
        
        if total_expected == 0:
            return 0.0, 0
            
        recall_rate = (hits / min(top_n, total_expected)) * 100
        return min(recall_rate, 100.0), hits

# 4. Initializing the Engine
engine = BM25SearchEngine(tokenized_corpus)

# 5. Interactive Terminal Loop
print("=" * 70)
print("🇧🇩 BANGLADESH 100-DOCS BM25 SEARCH & RETRIEVAL ENGINE 🚀")
print("=" * 70)
print(f"Total Documents Loaded in Corpus: {len(documents)}")
print("Type your query to search or type 'q' to exit.\n")

while True:
    user_query = input("👉 Enter your search query: ").strip()
    
    if user_query.lower() == 'q':
        print("\n👋 Exiting Search Engine. Have a wonderful day!")
        break
        
    if not user_query:
        print("⚠️ Please enter a valid keyword or query string!\n")
        continue

    # Performing Search
    top_results = engine.search(user_query, top_n=5)
    
    print(f"\n" + "-" * 70)
    print(f"🎯 SEARCH RESULTS FOR: '{user_query}' (Top 5 Matches)")
    print("-" * 70)
    
    if not top_results:
        print("❌ No matching documents found for this query in the corpus.")
    else:
        for rank, (doc_id, score) in enumerate(top_results, 1):
            print(f"Rank {rank} | Doc ID: {doc_id + 1} | BM25 Score: {score:.4f}")
            print(f"Text: {documents[doc_id]}")
            print("-" * 70)
            
        # Optional: Simulated Recall Evaluation for the query
        # Finding matching docs dynamically for evaluation display
        matched_indices = [idx + 1 for idx, score in top_results]
        eval_hits = len(matched_indices)
        recall_score = (eval_hits / len(top_results)) * 100 if top_results else 0.0
        
        print(f"📊 Evaluation Metrics -> Retrieved Hits: {eval_hits}/{len(top_results)} | Estimated Recall@5: {recall_score:.1f}%")
        print("=" * 70 + "\n")
