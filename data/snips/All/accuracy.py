from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ---------- 1️⃣ Intent Accuracy ----------
true_intent_file = "true_intents.txt"
pred_intent_file = "final_predictions_intents.txt"

with open(true_intent_file, "r") as f:
    true_intents = [line.strip() for line in f if line.strip()]

with open(pred_intent_file, "r") as f:
    pred_intents = [line.strip() for line in f if line.strip()]

intent_accuracy = accuracy_score(true_intents, pred_intents)
print(f"Intent Accuracy: {intent_accuracy:.4f}")

# ---------- 2️⃣ Slot Metrics (Precision, Recall, F1) ----------
true_slots_file = "true_slots.txt"
pred_slots_file = "final_predictions_slots.txt"

with open(true_slots_file, "r") as f:
    true_slots = [line.strip().split() for line in f if line.strip()]

with open(pred_slots_file, "r") as f:
    pred_slots = [line.strip().split() for line in f if line.strip()]

# ---- Debug mismatched lengths ----
mismatch_found = False
for i, (true_sent, pred_sent) in enumerate(zip(true_slots, pred_slots)):
    if len(true_sent) != len(pred_sent):
        mismatch_found = True
        print(f"\n⚠️ Sentence {i+1} has mismatched token counts:")
        print(f"  True length = {len(true_sent)} | Pred length = {len(pred_sent)}")
        print(f"  True slots: {' '.join(true_sent)}")
        print(f"  Pred slots: {' '.join(pred_sent)}")

if mismatch_found:
    print("\n❌ Some sentences have mismatched slot lengths — please fix them before evaluation.")
    exit(1)

# ---- Continue only if all lengths match ----
true_flat = [slot for sent in true_slots for slot in sent]
pred_flat = [slot for sent in pred_slots for slot in sent]

slot_precision = precision_score(true_flat, pred_flat, average='micro', zero_division=0)
slot_recall = recall_score(true_flat, pred_flat, average='micro', zero_division=0)
slot_f1 = f1_score(true_flat, pred_flat, average='micro', zero_division=0)

print(f"\nSlot Precision: {slot_precision:.4f}")
print(f"Slot Recall:    {slot_recall:.4f}")
print(f"Slot F1:        {slot_f1:.4f}")
