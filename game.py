import time
import sys
import os

def print_slow(text):
    """ฟังก์ชันทำให้ข้อความค่อยๆ ปรากฏขึ้น"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def load_high_score():
    """โหลดคะแนนสูงสุดจากไฟล์"""
    if not os.path.exists("highscore.txt"):
        return "ไม่มี", 0
    try:
        with open("highscore.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                name = lines[0].strip()
                score = int(lines[1].strip())
                return name, score
    except:
        pass
    return "ไม่มี", 0

def save_high_score(name, score):
    """บันทึกคะแนนสูงสุดลงไฟล์"""
    with open("highscore.txt", "w", encoding="utf-8") as f:
        f.write(f"{name}\n{score}")

def get_rank(score):
    if score >= 90: return "🏆 Rank S (ปรมาจารย์ระบบปัสสาวะ)"
    elif score >= 75: return "🥇 Rank A (ผู้เชี่ยวชาญร่างกาย)"
    elif score >= 60: return "🥈 Rank B (นักศึกษาแพทย์ฝึกหัด)"
    elif score >= 40: return "🥉 Rank C (ผ่านเกณฑ์หวุดหวิด)"
    else: return "☠️ Rank F (ต้องกลับไปเรียนใหม่นะ!)"

def play_game():
    hp = 3
    base_score = 0
    hs_name, hs_score = load_high_score()
    
    print("=" * 60)
    print("🌟 ยินดีต้อนรับสู่เกม: ผจญภัยในระบบปัสสาวะ! 🌟")
    print("=" * 60)
    print(f"🔥 คะแนนสูงสุดตอนนี้: {hs_score} โดยคุณ [{hs_name}]")
    print("-" * 60)
    
    player_name = input("กรุณาใส่ชื่อของคุณ: ").strip() or "ผู้เล่นนิรนาม"
    
    print_slow(f"\nเริ่มเกม! คุณคือ 'โมเลกุลน้ำ' มี HP: {hp}")
    start_time = time.time()

    # --- ด่านที่ 1 ---
    print("\n--- ด่านที่ 1: ไต (Kidney) ---")
    print("คำถาม: ไตทำหน้าที่อะไร? A) ย่อยอาหาร | B) กรองของเสีย | C) ปั๊มเลือด")
    if input("ตอบ (A/B/C): ").strip().upper() == 'B':
        print("✨ ถูกต้อง! +25 คะแนน")
        base_score += 25
    else:
        hp -= 1
        print(f"❌ ผิด! HP เหลือ: {hp}")
    
    if hp <= 0: return # จบเกมถ้า HP หมด

    # --- ด่านที่ 2 ---
    print("\n--- ด่านที่ 2: ท่อไต (Ureter) ---")
    print("คำถาม: ท่อที่นำปัสสาวะจากไตลงสู่กระเพาะปัสสาวะคือ? A) ท่อไต | B) หลอดอาหาร | C) หลอดลม")
    if input("ตอบ (A/B/C): ").strip().upper() == 'A':
        print("✨ ถูกต้อง! +25 คะแนน")
        base_score += 25
    else:
        hp -= 1
        print(f"❌ ผิด! HP เหลือ: {hp}")

    if hp <= 0: return

    # --- ด่านที่ 3 ---
    print("\n--- ด่านที่ 3: กระเพาะปัสสาวะ (Urinary Bladder) ---")
    print("คำถาม: กระเพาะปัสสาวะทำหน้าที่อะไร? A) ย่อย | B) ผลิตฮอร์โมน | C) กักเก็บปัสสาวะ")
    if input("ตอบ (A/B/C): ").strip().upper() == 'C':
        print("✨ ถูกต้อง! +25 คะแนน")
        base_score += 25
    else:
        hp -= 1
        print(f"❌ ผิด! HP เหลือ: {hp}")

    if hp <= 0: return

    # --- ด่านที่ 4 ---
    print("\n--- ด่านที่ 4: ท่อปัสสาวะ (Urethra) ---")
    print("คำถาม: ท่อที่นำปัสสาวะออกนอกร่างกายคือ? A) ท่อปัสสาวะ | B) ลำไส้ | C) เส้นเลือด")
    if input("ตอบ (A/B/C): ").strip().upper() == 'A':
        print("✨ ถูกต้อง! +25 คะแนน")
        base_score += 25
    else:
        hp -= 1
        print(f"❌ ผิด! HP เหลือ: {hp}")

    # --- สรุปผล ---
    total_time = round(time.time() - start_time, 2)
    final_score = base_score + (hp * 5) + max(0, 15 - int(total_time))
    
    print(f"\n📊 คะแนนรวมของคุณ: {final_score}")
    print(f"🏅 แรงกิ้ง: {get_rank(final_score)}")
    
    if final_score > hs_score:
        print("🥳 คุณทำลายสถิติใหม่แล้ว!")
        save_high_score(player_name, final_score)

if __name__ == "__main__":
  python game.py
