tilt = 0
# 초기 상태 - 두 LED 모두 꺼짐
pins.digital_write_pin(DigitalPin.P1, 0)
pins.digital_write_pin(DigitalPin.P2, 0)

def on_forever():
    global tilt
    # x축 가속도 값 읽기 (기울기)
    tilt = input.acceleration(Dimension.X)
    
    # 좌우 기울기에 따라 LED 제어
    if tilt < -200:  # 왼쪽으로 기울임
        pins.digital_write_pin(DigitalPin.P1, 1)  # P1 LED 켜기
        pins.digital_write_pin(DigitalPin.P2, 0)  # P2 LED 끄기
    elif tilt > 200:  # 오른쪽으로 기울임
        pins.digital_write_pin(DigitalPin.P1, 0)  # P1 LED 끄기
        pins.digital_write_pin(DigitalPin.P2, 1)  # P2 LED 켜기
    else:  # 평평한 상태
        # 기울기가 충분하지 않으면 두 LED 모두 끄기
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
    
    basic.pause(100)  # 반응성 조절을 위한 대기 시간
    
basic.forever(on_forever)