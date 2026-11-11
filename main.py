import json
import os

def load_kb(filepath="kb_cybersecurity.json"):
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} tidak ditemukan!")
        exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def forward_chaining(kb, user_facts):
    memory = set(user_facts)
    executed_rules = []
    
    while True:
        new_inference = False
        for rule in kb["aturan"]:
            rule_id = rule["id"]
            if rule_id in [r["id"] for r in executed_rules]:
                continue
            
            conditions = rule["jika"]
            mode = rule["mode"]
            target = rule["maka"]
            
            if mode == "dan":
                satisfied = all(cond in memory for cond in conditions)
            elif mode == "atau":
                satisfied = any(cond in memory for cond in conditions)
            else:
                satisfied = False
                
            if satisfied and target not in memory:
                memory.add(target)
                executed_rules.append({
                    "id": rule_id,
                    "maka": target,
                    "jika": conditions,
                    "mode": mode
                })
                new_inference = True
                break
                
        if not new_inference:
            break
            
    return memory, executed_rules

def main():
    kb = load_kb()
    
    print("=" * 70)
    print(f"   {kb['judul'].upper()}")
    print("=" * 70)
    print("Jawab indikator insiden berikut dengan 'y' (Ya) atau 't' (Tidak):\n")
    
    all_targets = {rule["maka"] for rule in kb["aturan"]}
    askable_facts = set()
    for rule in kb["aturan"]:
        for cond in rule["jika"]:
            if cond not in all_targets:
                askable_facts.add(cond)
                
    askable_facts = sorted(list(askable_facts))
    user_facts = []
    
    for idx, fact in enumerate(askable_facts, 1):
        ans = input(f"{idx}. Apakah {fact}? (y/t) > ").strip().lower()
        if ans == 'y':
            user_facts.append(fact)
            
    print("\n" + "-" * 70)
    print("FAKTA AWAL:", ", ".join(user_facts) if user_facts else "Tidak ada indikator yang dipilih")
    print("-" * 70)
    
    memory, executed_rules = forward_chaining(kb, user_facts)
    
    print("\nPROSES INFERENSI (FORWARD CHAINING):")
    if not executed_rules:
        print(" -> Tidak ada aturan baru yang terpicu.")
    else:
        for idx, rule in enumerate(executed_rules, 1):
            print(f" Siklus {idx}: {rule['id']} -> {rule['maka']}")
            
    final_diagnoses = [target for target in memory if target in all_targets and not target.startswith("indikasi")]
    
    print("\n" + "=" * 70)
    print("KESIMPULAN DIAGNOSA INSIDEN:")
    if final_diagnoses:
        for diag in final_diagnoses:
            print(f" [!] TERDETEKSI: {diag}")
    else:
        print(" [?] Tidak dapat menyimpulkan jenis serangan (Kasus Negatif / Indikator Tidak Cukup).")
        
    print("\nALASAN & RANTAI ATURAN (RATIONALE):")
    if executed_rules:
        for rule in reversed(executed_rules):
            conds_str = f" {rule['mode'].upper()} ".join(rule['jika'])
            print(f"  • {rule['maka']}  <- {rule['id']} ({conds_str})")
    else:
        print("  • Tidak ada aturan yang terpicu.")
        
    print("\nBATAS KEBERLAKUAN SISTEM:")
    print(f" {kb['batas']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
