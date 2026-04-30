"""부스용 QR 코드 생성 스크립트
응답자용 만족도조사 URL을 QR로 변환해 PNG 파일로 저장.
실행: python generate_qr.py
"""
import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://lalaseohyun.github.io/jeonju-livinglab/?mode=respond"

# 인쇄·부스 환경 가독성 우선
# error_correction=H: 30%까지 손상돼도 인식 가능 (스티커 가장자리 흠집 대비)
# box_size=20, border=4: 총 픽셀 약 1000~1200 → 부스 큰 안내판에 인쇄해도 선명
qr = qrcode.QRCode(
    version=None,                 # URL 길이에 맞춰 자동
    error_correction=ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

# 메인 — 단순 흑백 (가장 안정적)
img = qr.make_image(fill_color="#1A1A1A", back_color="white")
img.save("qr-respond.png")
print(f"[OK] qr-respond.png saved (size: {img.size[0]}x{img.size[1]})")

# 컨셉 컬러 — 비비드 레드 (#FF0000)
# 일부 구형 스캐너는 어두운 색 외엔 인식률이 떨어질 수 있음 → 보조용으로만 사용
img_red = qr.make_image(fill_color="#FF0000", back_color="white")
img_red.save("qr-respond-red.png")
print(f"[OK] qr-respond-red.png saved (vivid red #FF0000)")

print(f"\nURL: {URL}")
