import hashlib
import json
import os
import time

FOLDER_DANG = "."

def tinh_md5(noi_dung_text):
    noi_dung_chuan = noi_dung_text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.md5(noi_dung_chuan.encode("utf-8")).hexdigest()

def tao_manifest():
    # TRẢ LẠI ĐÚNG CẤU TRÚC DICT ({}) NHƯ FILE GỐC CỦA BẠN
    manifest = {
        "version": int(time.time()),
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "files": {}, 
    }

    count = 0
    for fname in os.listdir(FOLDER_DANG):
        if fname.startswith("dang") and fname.endswith(".py"):
            fpath = os.path.join(FOLDER_DANG, fname)
            key = fname[:-3]  # Lấy tên dạng, ví dụ: dang10_p1_b1_c1_ds9
            
            try:
                # Mở và đọc nội dung code bên trong file
                with open(fpath, "r", encoding="utf-8") as f:
                    noi_dung_text = f.read()
            except Exception as e:
                print(f"[Lỗi] {fname}: {e}")
                continue

            # Lưu vào từ điển
            manifest["files"][key] = tinh_md5(noi_dung_text)
            count += 1

    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"[Hoàn tất] Đã tạo mã băm cho {count} file vào 'manifest.json'.")

if __name__ == "__main__":
    tao_manifest()